import csv
import re
import shutil
from pathlib import Path, PurePath

from jinja2 import Template

import unidecode


def normalize_name(original, limit=0):
    low = original.lower()
    low = unidecode.unidecode(low)
    low = re.sub(r"[^A-Za-z0-9\s]", "", low)
    low = re.sub(r"\s+", " ", low)

    if limit > 0:
        low = " ".join(low.split()[:limit])
    low = re.sub(r"\s+", "-", low)
    return low


def convert_csv_to_dict(csv_line):
    author=csv_line[1]
    title=csv_line[2]
    return dict(
        id=csv_line[0],
        author=author,
        title=title,
        slides=csv_line[3],
        title_normalized=normalize_name(title, 5),
        author_normalized=normalize_name(author, 3)
    )


def load_talks(csv_fp):
    talks = {}
    for talk_line in csv.reader(csv_fp):
        talk = convert_csv_to_dict(talk_line)
        talks[talk["id"]] = talk
    return talks


def load_slides_files(root_path):
    slides_index = {}
    id_rex = re.compile(r"^\s*(\d+)")
    for f in root_path.iterdir():
        if f.is_file():
            slide_id = id_rex.search(f.name)
            if slide_id:
                slides_index[slide_id.group(1)] = f.absolute()
    return slides_index


def load_template(filename):
    template_path = Path() / "templates" / filename
    return Template(template_path.read_text())


def render_index_readme(talks):
    template = load_template("README.md")
    return template.render(talks=talks)


def render_talk_readme(talk, talk_dir):
    talk_template = load_template("talk.md")

    talk_content = talk_template.render(talk=talk)

    readme_path = talk_dir / "README.md"
    readme_path.write_text(talk_content)


def render_slides_filename(talk):
    suffix = talk["slides_file"].suffix

    author = talk['author_normalized']
    title = talk['title_normalized']
    return f"pybr2019-{author}-{title}{suffix}"


def merge_talks_and_slides(talks_index, slides_index):
    for key, slide_file in slides_index.items():
        if key in talks_index:
            talk = talks_index[key]
            talk["slides_file"] = slide_file
            talk["slides_file_normalized"] = render_slides_filename(talk)

    return talks_index


def prepare_talks(talks_file, slides_dir):
    # create json with all normalized talks data
    talks_index = load_talks(talks_file)

    # create slides files index
    slides_index = load_slides_files(slides_dir)

    talks_index = merge_talks_and_slides(talks_index, slides_index)

    return talks_index


def copy_slides_file_to_talk_folder(talk, talk_dir):
    from_slides_file = str(talk["slides_file"])
    to_slides_file = talk_dir / talk["slides_file_normalized"]

    shutil.copy(from_slides_file, to_slides_file)


def create_talks_files(talks, output_dir):
    output_folder = Path(output_dir)

    # generate folders and talk file
    for talk_id, talk in talks.items():
        talk_dir = output_folder / talk["title_normalized"]
        talk_dir.mkdir(exist_ok=True)

        talks_readme = render_talk_readme(talk, talk_dir)
        if "slides_file" in talk:
            copy_slides_file_to_talk_folder(talk, talk_dir)


def process(talks_csv, slides_dir, output_dir):
    talks = prepare_talks(
        talks_file=talks_csv,
        slides_dir=slides_dir
    )

    create_talks_files(talks, output_dir)

    # generate index README
    index_readme = render_index_readme(talks.values())
    index_readme_file = output_dir / "README.md"
    index_readme_file.write_text(index_readme)


def fetch(input_args):
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--talks", dest="talks_csv", type=argparse.FileType("r"), required=True
    )
    parser.add_argument(
        "-s", "--slides", dest="slides_dir", type=str, required=True
    )
    parser.add_argument("-o", "--out", dest="output_dir", default="-")

    return parser.parse_args(input_args)


def main(input_args):
    in_args = fetch(input_args)
    slides_dir = Path(in_args.slides_dir)
    output_dir = Path(in_args.output_dir)
    process(talks_csv=in_args.talks_csv, slides_dir=slides_dir, output_dir=output_dir)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])

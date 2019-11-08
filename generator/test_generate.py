import csv
from io import StringIO
from pathlib import Path, PurePath

import pytest

from generate import normalize_name, convert_csv_to_dict, load_talks, load_slides_files, merge_talks_and_slides, prepare_talks, copy_slides_file_to_talk_folder


@pytest.fixture
def talks_fp():
    content = '48,Author Autor,Title Título,https://drive.google.com/file/d/1s609lBPVVB81OHfTxxMxH-1879xXYHse/view?usp=sharing,Avaliador,2019-10-19,'
    return StringIO(content)


@pytest.fixture
def talks_csv_line(talks_fp):
    reader = csv.reader(talks_fp)
    return list(reader).pop()


def test_convert_csv_into_dict(talks_csv_line):
    json_line = convert_csv_to_dict(talks_csv_line)
    assert {"id", "title", "slides", "author", "title_normalized", "author_normalized"} == set(json_line.keys())


def test_load_talks_dict_index_by_id(talks_fp):
    talks =  load_talks(talks_fp)
    assert isinstance(talks, dict)
    talks_fp.seek(0)
    assert set(talks.keys())


@pytest.fixture
def slides_dir():
     return Path() / "slides"


def test_load_slides_files(slides_dir):
    slides_files = load_slides_files(slides_dir)
    assert isinstance(slides_files, dict)
    assert all(map(int, slides_files.keys()))


def test_merge_talks_with_slides_files(talks_fp, slides_dir):
    talks_index = load_talks(talks_fp)
    slides_index = load_slides_files(slides_dir)
    talks = merge_talks_and_slides(talks_index, slides_index)

    for talk in talks_index.values():
        assert "slides_file" in talk


def test_copy_slides_file_to_talk_folder(talks_fp, slides_dir, tmpdir):
    slide_file = tmpdir / "40 - somerandomfile.txt"
    slide_file.write_text("test", encoding="utf8")

    talk = {"title_normalized": "nome-da-talk", "author_normalized": "autor-nome", "slides_file": slide_file, "slides_file_normalized": "pybr2019-autor-nome-nome-da-talk.txt"}

    talk_dir = tmpdir / talk["title_normalized"]
    talk_dir.mkdir()

    final_slide_file = copy_slides_file_to_talk_folder(talk=talk, talk_dir=talk_dir)

    file_name = f"pybr2019-{talk['author_normalized']}-{talk['title_normalized']}.txt"
    file_path = talk_dir / file_name
    assert file_path.exists()


@pytest.mark.parametrize(
    "original,expected",
    [
        ("Título", "titulo"),
        ("Título Composto", "titulo-composto"),
        ("Título Composto 'Aspas'", "titulo-composto-aspas")
    ]
)
def test_render_clean_folder(original, expected):
    assert expected == normalize_name(original)

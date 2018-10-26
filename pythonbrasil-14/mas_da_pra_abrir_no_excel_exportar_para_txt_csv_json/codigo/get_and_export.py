#!/bin/env python3

"""
get_and_export.py    Version 1    October, 2018.

@copyright (C) 2018, Renata D'Avila https://rsip22.github.io/blog
@license: GPL v2

Get a list of cities from DjangoGirls.org/events and export it to txt, csv or JSON.
When creating a txt, it also outputs the processing of the items to the terminal.

<Usage>
optional arguments:
  --txt       export to TXT format
  --csv       export to CSV format
  --json      export to JSON format
If no format is selected, the data will be exported to one file in each format.

Example:
$ pipenv run python get_and_export.py --json

<License>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse
import csv
import json
import os
import sys
from contextlib import redirect_stdout

import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import data_source as website

def get_cities():
    """ Get a list of cities from the website """

    driver = webdriver.Firefox()
    driver.get(website.data['url'])
    delay = 60

    locations_list = list()

    try:
        get_city = WebDriverWait(driver,
                                 delay).until(
                                     lambda x:
                                     x.find_elements_by_class_name("overlay"))
        for item in get_city:
            item_text = item.text.splitlines()
            print(item_text)
            try:
                city, date = item_text[0], item_text[1]
                locations_list.append((city, date))
            except IndexError:
                continue

        driver.close()

        return locations_list

    except selenium.common.exceptions.NoSuchElementException:
        print('Element not found .')


def create_txt(locations):
    """
    Save a txt to local machine with the locations info
    Args:
        location: list of tuples
    """

    file_path = os.getcwd() + '/' + website.data['file_name'] + '.txt'

    # print('TXT file path:', file_path)

    stdout_fd = sys.stdout.fileno()
    count = 0

    with open(file_path, 'w') as txtfile:
        with redirect_stdout(txtfile): # Use it to redirect the whole standout to file
            for item in locations:
                count = count + 1
                os.write(stdout_fd, bytes('{}'.format(count)
                                          + f' - {item[0]} {item[1]}' '\n',
                                          'utf8'))
                txtfile.write('\n'+ item[0] + ' ' + item[1])
        os.write(stdout_fd, bytes('Total cities: {}'.format(count) + '\n', 'utf8'))

    os.write(stdout_fd, bytes('TXT file path:' + file_path  + '\n', 'utf8'))


def create_csv(locations):
    """
    Save a CSV file to local machine with the locations info
    Args:
        location: list of tuples
    """

    file_path = os.getcwd() + '/' + website.data['file_name'] + '.csv'

    print('CSV file path:', file_path)

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['City', 'Date']
        writer = csv.DictWriter(csvfile,
                                delimiter=';',
                                fieldnames=fieldnames,
                                extrasaction='ignore')

        writer.writeheader()

        for item in locations:
            writer.writerow({'City': item[0], 'Date': item[1]})

def create_json(locations):
    """
    Save a JSON file to local machine with the locations info.
    Args:
        location: list of tuples
    """

    file_path = os.getcwd() + '/' + website.data['file_name'] + '.json'

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(locations, json_file, ensure_ascii=False, indent=1)

    print('JSON file path:', file_path)


if __name__ == '__main__':
    LOCATIONS_LIST = get_cities()

    ARG_PARSER = argparse.ArgumentParser()

    ARG_PARSER.add_argument('--txt',
                            help='export to TXT format',
                            action='store_true')
    ARG_PARSER.add_argument('--csv',
                            help='export to CSV format',
                            action='store_true')
    ARG_PARSER.add_argument('--json',
                            help='export to JSON format',
                            action='store_true')

    ARGS = ARG_PARSER.parse_args()

    if ARGS.txt:
        create_txt(LOCATIONS_LIST)
    elif ARGS.csv:
        create_csv(LOCATIONS_LIST)
    elif ARGS.json:
        create_json(LOCATIONS_LIST)
    else:
        create_txt(LOCATIONS_LIST)
        create_csv(LOCATIONS_LIST)
        create_json(LOCATIONS_LIST)

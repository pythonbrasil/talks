import json
import os

locations = [('PUNE', '20th October 2018'),
             ('Sao Leopoldo', '20th October 2018'),
             ('Oko , Anambra', '3rd November 2018'),
             ('Abeokuta, Ogun', '3rd November 2018')]

file_path = os.getcwd() + '/' + 'test_django_girls' + '.json'

with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(locations, json_file, indent=1)

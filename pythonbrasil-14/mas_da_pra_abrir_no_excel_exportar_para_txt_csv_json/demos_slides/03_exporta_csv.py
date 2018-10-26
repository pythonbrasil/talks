import csv

locations = [('PUNE', '20th October 2018'),
             ('Sao Leopoldo', '20th October 2018'),
             ('Oko , Anambra', '3rd November 2018'),
             ('Abeokuta, Ogun', '3rd November 2018')]

filename = 'django_girls.csv'

with open(filename, 'w', newline='') as csvfile:
    write_location = csv.writer(csvfile, delimiter=';', dialect='excel')

    for city in locations:
        write_location.writerow(city)

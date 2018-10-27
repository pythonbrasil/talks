import csv

locations = [{'City': 'PUNE', 'Date': '20th October 2018'},
             {'City': 'Sao Leopoldo', 'Date': '20th October 2018'},
             {'City': 'Oko , Anambra', 'Date': '3rd November 2018'},
             {'City': 'Ensenada', 'Date': '23rd May 2015', 'Photo credit': 'Gregg Erickson (CC)'}]

with open('django_girls.csv', 'w', newline='') as csvfile:
    fieldnames = ['City',
                  'Date']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(locations)

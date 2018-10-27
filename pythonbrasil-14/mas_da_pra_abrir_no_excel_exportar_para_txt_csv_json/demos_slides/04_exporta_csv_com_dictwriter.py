import csv

locations = {'PUNE': '20th October 2018',
             'Sao Leopoldo': '20th October 2018',
             'Malate, Ilorin': '26th October 2018',
             'Douala': '26th October 2018',
             'Kuwait City': '26th October 2018',
             'Lafia, Nasarawa': '27th October 2018',
             'Delta': '28th October 2017'}

with open('dg_2018.csv', 'w', newline='') as csvfile:
    fieldnames = ['City', 'Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for name in locations.items():
        writer.writerow({'City': name[0], 'Date': name[1]})

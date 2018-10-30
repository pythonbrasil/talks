import csv
import pandas as pd
import selenium as sl
from selenium.webdriver.support.wait import WebDriverWait

driver = sl.webdriver.Firefox()
driver.get('https://djangogirls.org/events/')
delay = 60
locations_and_dates = dict()

get_city = WebDriverWait(driver,
                         delay).until(
                             lambda x:
                             x.find_elements_by_class_name("overlay"))

count = 0

for item in get_city:
    count = count + 1
    item_text = item.text.splitlines()
    try:
        city, date = item_text[0], item_text[1]
        locations_and_dates[city] = date
    except IndexError:
        continue

new_dic_dg = list()

for name, value in locations_and_dates.items():
    new_dic_dg.append({"city": name, "date": value})

new_df = pd.DataFrame(new_dic_dg).to_csv('dg_with_pandas.csv', index=False, sep=';')

driver.close()

import pandas as pd
from pandas import ExcelWriter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# pandas ValueError Arrays Must be All Same Length function fix
def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list


browser = webdriver.Chrome(ChromeDriverManager().install())

for day in range(1, 8):
    url = f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-noiembrie-ora-13-00-2/'
    browser.get(url)

    table_path = '/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr/td'
    table = browser.find_elements(By.XPATH, table_path)
    table_list = []

    for item in table:
        table_list.append(item.text)
    print(table_list)

    header_path = '/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td'
    header = browser.find_elements(By.XPATH, header_path)
    header_list = []

    for item in header:
        header_list.append(item.text)
    print(header_list)

    table_dict = {i: [] for i in header_list}

    for i in range(0, len(header_list)):
        for j in range(len(header_list) + int(i), len(table_list), len(header_list)):
            table_dict[header_list[int(i)]].append(table_list[j])
    print(table_dict)

    final_table_dict = pad_dict_list(table_dict, ' ')
    print(final_table_dict)

    data_frame = pd.DataFrame(final_table_dict)

    if day == 1:
        data_frame.to_excel('informare_covid.xlsx')
    else:
        with ExcelWriter('informare_covid.xlsx', mode='a', engine='openpyxl') as writer:
            data_frame.to_excel(writer, sheet_name=f'Sheet{day}')

    time.sleep(5)

browser.exit()

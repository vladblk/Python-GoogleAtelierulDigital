from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element(By.XPATH, '//*[@id="Data_table"]')

table_text = table.text
lista = table_text.split('\n')
print(lista)

header = browser.find_element(By.XPATH, '//*[@id="Data_table"]/table/thead/tr').text.split('\n')

dictionar = {i: [] for i in header}
# print(dictionar)

for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
print(dictionar)

data_frame = pd.DataFrame(dictionar)
data_frame.to_csv('BNR_ALL_DATA.csv')

time.sleep(3)
browser.close()

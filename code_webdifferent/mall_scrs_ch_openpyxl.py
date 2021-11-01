from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_op
import pandas as pd 
import csv
import os
import re 

name = "you need to name"
csv_file =  "C:\programing\Atom_collection\code_webdifferent\\fix_data.csv"
save_file = "C:\programing\Atom_collection\screenshot_programing\scrs_" + name

path = "C:\chrome\chromedriver.exe"

dispID_dict = {}
name_dict = {}

df = pd.read_csv(csv_file,encoding='cp932')

for index in range(len(df)):
    dispID_dict[df.ソフィア開発環境[index]]=df.画面ID[index]
    name_dict[df.ソフィア開発環境[index]]=df.名前[index]

URL = dispID_dict.keys()

options = chrome_op()
options.add_argument('-headless')
driver = webdriver.Chrome(executable_path=path,options=options)

if not os.path.exists(save_file):
    os.mkdir(save_file)

for url in URL:
    driver.get(url)

    # page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(750, page_height)

    # print(page_width, page_height)
    driver.save_screenshot(save_file + "\\[ch]_" + name_dict[url] + "(" + dispID_dict[url] + ")" + ".png")

driver.quit()
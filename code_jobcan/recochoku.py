import os
from selenium import webdriver
import time

device = os.name

if device == 'nt':
    path = "C:\chrome\chromedriver.exe"  
else:
    path = "/usr/bin/choromedriver"

driver = webdriver.Chrome(executable_path=path)
driver.get("https://recochoku.jp/ranking/single/daily/?affiliate=4305070016")

driver.find_element_by_xpath('//*[@id="unit"]/table/tbody/tr[1]/td[2]/a[3]/img').click()

for index in range(0,5):
    number = str(index)
    ID =  '//*[@id="abd_' + number + '"]/a/img'
    try:
        driver.find_element_by_xpath(ID).click()
    except:
        pass


time.sleep(5)

driver.close()

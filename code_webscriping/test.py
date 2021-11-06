import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://www.jcbasimul.com/radio/1249/"
path = "../driver/chromedriver_win90.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
time.sleep(5)
driver.find_element_by_class_name(
    'embeddable-player-pause').click()
print('push')
time.sleep(1)
#driver.find_element_by_xpath(
 #   '//*[@id="embeddable-player-playstop-bcbc43b2"]').click()
time.sleep(20)


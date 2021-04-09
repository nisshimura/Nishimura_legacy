from selenium import webdriver 
from selenium.webdriver.chrome.options import Options as chrome_op

path = "C:\webdriver\chromedriver86.exe"
url =  "https://ja.wikipedia.org/wiki/安倍晋三"

options = chrome_op()
options.add_argument('-headless')
driver = webdriver.Chrome(executable_path=path,options=options)

driver.get(url)

page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(page_width, page_height)

print(page_width, page_height)
driver.save_screenshot("C:\programing_photo\chrome_.png")

driver.quit()
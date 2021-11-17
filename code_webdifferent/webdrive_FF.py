from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FF_op

path = "C:\chrome\geckodriver.exe"
url =  "https://www.residia.jp/housing/top/31"

options = FF_op()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path=path,options=options)

driver.get(url)

page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(page_width, page_height)

print(page_width, page_height)
driver.save_screenshot("C:\programing\Atom_collection\screenshot_programing\FF_.png")

driver.quit()
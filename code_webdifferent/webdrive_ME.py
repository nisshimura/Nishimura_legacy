from selenium import webdriver
from selenium.webdriver.edge.options import Options
from msedge.selenium_tools import Edge, EdgeOptions
import time

# path = "C:\\Users\\ntaka\\workspace\\sophia_webcap\\external\\edgedriver_win83.exe"
url =  "https://www.youtube.com/?gl=JP&hl=ja"

options = EdgeOptions()
options.use_chromium = True
# options.add_argument('headless')
# options.add_argument('disable-gpu')
options.add_argument("ms:inPrivate")
driver = Edge(options=options)

driver.set_window_size(1980, 1080)
driver.get(url)
time.sleep(2)

page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')
print(page_width, page_height)

driver.set_window_size(page_width, page_height)
driver.save_screenshot("C:\programing\Atom_collection\screenshot_programing\ME_.png")

driver.quit()
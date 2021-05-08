from selenium import webdriver

path = '../driver/chromedriver_win90.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=path,options=options)    

driver.get('http://www.boatrace-db.net/stadium/index/')

links = {}

stadiums = driver.find_elements_by_class_name('stadiumSelect_item')

for stadium in stadiums:
    aTag = stadium.find_element_by_tag_name('a')
    link = aTag.get_attribute('href')
    links[stadium.text] = link
    print(link)

print(links)
driver.close()

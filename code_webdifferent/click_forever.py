from selenium import webdriver 

path = "C:\chrome\chromedriver.exe"
url = "http://www.grand-tree.jp/web/index.html"

driver = webdriver.Chrome(executable_path=path)
driver.get(url)

elems = driver.find_elements_by_xpath("//a[@href]")

list_http = []

for elem in elems:
    http = elem.get_attribute("href")
    list_http.append(http)

print(list_http)
for i in list_http:
    driver.get(i)



driver.quit()






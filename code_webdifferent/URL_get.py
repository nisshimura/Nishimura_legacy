from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = []
<<<<<<< HEAD
path = ".\code_jobcan\Jobcan_re\chromedriver.exe"
=======
path = "C:\Users\github\workspace\jobcan_autotool\code_webdifferent\chromedriver_win83.exe"
>>>>>>> 6bcaa64c4264a24f8169d0e53f7dba2f9a2de0a1
url = 'https://suumo.jp/ms/chuko/tokyo/sc_meguro/oz_13110020/'

# options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=path)#,options=options)

driver.get(url)

for index in range(1,5):
    driver.find_element_by_xpath('//*[@id="js-bukkenList"]/div[' + str(index) + ']/div[2]/div[1]/h2/a').click()
    driver.close()
    driver.switch_to_window(driver.window_handles[-1])
    URL.append(driver.current_url)
    driver.get(url)

print(URL)

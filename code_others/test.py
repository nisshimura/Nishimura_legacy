from selenium import webdriver
import xlrd
import pprint
import time
import pyautogui

path = "C:\\Users\\ntaka\\workspace\\jobcan_autotool\\code_others\\chromedriver1.exe"
expath = "C:\\Users\\ntaka\\OneDrive\\ドキュメント\\Book1.xlsx"

wb = xlrd.open_workbook(expath)
print(type(wb))
print(wb.sheet_names())
sheet = wb.sheet_by_name('Sheet1')

driver = webdriver.Chrome(executable_path=path)
driver.get('https://quizlet.com/latest')

user_name = driver.find_element_by_xpath('//*[@id="username"]')
user_pass = driver.find_element_by_xpath('//*[@id="password"]')

user_name.send_keys('Nishimura_Takayuki')
user_pass.send_keys('Takayuki1763')

button = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/form/button')
button.click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="DashboardPageTarget"]/div/section[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/a').click()
time.sleep(8)

count = 0

for i in range(332, 340):
    jap = sheet.cell(i, 0)
    futu = sheet.cell(i, 1)
    j = driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[2]/div[2]/div/div[1]/div/div[1]/div[' + str(5 + count*2) + ']/div/div[3]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/p')
    f = driver.find_element_by_xpath('//*[@id = "SetPageTarget"]/div/div[2]/div[2]/div/div[1]/div/div[1]/div[' + str(5 + count*2) + ']/div/div[3]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/p')
    j.send_keys(jap.value)
    pyautogui.keyDown('tab')
    f.send_keys(futu.value)
    pyautogui.keyDown('tab')
    count += 1

time.sleep(1000)


from selenium import webdriver
import time

path = "C:\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path = path)
driver.get("https://id.jobcan.jp/users/sign_in?app_key=atd")

user_name = driver.find_element_by_id('user_email')
user_password = driver.find_element_by_id('user_password')

user_name.send_keys('t-sakoda@sophia-s.co.jp')
user_password.send_keys('sophia2019')

driver.find_element_by_class_name('form__login').click()

driver.find_element_by_id('adit-button-push').click()
driver.get("https://id.jobcan.jp/users/sign_in?app_key=atd")



time.sleep(5)

driver.close()
driver.quit()

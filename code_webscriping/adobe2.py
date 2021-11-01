import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class adobe_trial():
    def __init__(self):
        self.url = "https://account.adobe.com/plans/4552B659FED96B82A33A/cancel-plan"
        self.wait_time = 10
        self.path = "../driver/chromedriver_win90.exe"
        self.login_id = "ntakayki01@mineo.jp"
        self.login_pw = "Melton1763"
        self.driver = webdriver.Chrome(executable_path=self.path)

    def login(self):
        driver = self.driver
        driver.get(self.url)
        
        ### IDを入力
        login_id_xpath = '//*[@id="EmailPage-EmailField"]'
        continue_botton_path = '//*[@id="EmailForm"]/section[2]/div[2]/button/span'
        
        WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.XPATH, login_id_xpath)))
        driver.find_element_by_xpath(login_id_xpath).send_keys(self.login_id)
        WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.XPATH, continue_botton_path)))
        driver.find_element_by_xpath(continue_botton_path).click()

        try:
            ### パスワードを入力
            login_pw_xpath = '//*[@id="PasswordPage-PasswordField"]'
            continue_botton_path2 = '//*[@id="PasswordForm"]/section[2]/div[2]/button/span'
            # xpathの要素が見つかるまで待機します。
            WebDriverWait(driver, self.wait_time).until(
                EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
            driver.find_element_by_name("password").send_keys(self.login_pw)
            time.sleep(1)  # クリックされずに処理が終わるのを防ぐために追加。
            WebDriverWait(driver, self.wait_time).until(
                EC.presence_of_element_located((By.XPATH, continue_botton_path2)))
            driver.find_element_by_xpath(continue_botton_path2).click()
            return True

        except:
            driver.close()
            time.sleep(3600)
            return False

    def get_trial(self):
        driver = self.driver
        ##checkbox
        check_box_path = 'spectrum-Checkbox-input'
        WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, check_box_path)))
        driver.find_element_by_class_name(check_box_path).click()

        ##checkbox_continue
        continue_path = 'spectrum-Button-label'
        WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, continue_path)))
        bottons = driver.find_elements_by_class_name(continue_path)
        for botton in bottons:
            if botton.text == '続行':
                botton.click()
                break

        ##詳細continue
        try:
            continue_path2 = 'spectrum-Button-label'
            WebDriverWait(driver, self.wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, continue_path2)))
            footer_bottons = driver.find_elements_by_class_name(continue_path2)
            for botton in footer_bottons:
                if botton.text == '続行':
                    botton.click()
                    break

        except:
            time.sleep(2)
            self.popup()
            continue_path2 = 'spectrum-Button-label'
            WebDriverWait(driver, self.wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, continue_path2)))
            footer_bottons = driver.find_elements_by_class_name(continue_path2)
            for botton in footer_bottons:
                if botton.text == '続行':
                    botton.click()
                    break

        ##特典を受け取る    
        get_path = 'spectrum-Button-label'
        WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, get_path)))
        tokuten_bottons = driver.find_elements_by_class_name(get_path)
        for botton in tokuten_bottons:
            if botton.text == '特典を受け取る':
                botton.click()
                break
        time.sleep(3)

        ##完了
        driver.get(self.url)

    def popup(self):
        try:
            popup_path = 'spectrum-Button-label'
            WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, popup_path)))
            popup_bottons = self.driver.find_elements_by_class_name(popup_path)
            for botton in popup_bottons:
                if botton.text == '解約の確認へ':
                    botton.click()
                    break
            time.sleep(5)
        except:
            pass

        
def main():
    work = adobe_trial()
    count = 0

    while True:
        ans = work.login()
        for i in range(40):
            if ans == True:
                work.get_trial()
                count += 1
            else:
                pass
            print(count)

if __name__ == '__main__':
    main()

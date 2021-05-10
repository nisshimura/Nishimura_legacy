import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class adobe_trial():
    def __init__(self):
        self.wait_time = 5
        self.path = "../driver/chromedriver_win90.exe"
        self.login_id = "ntakayki01@mineo.jp"
        self.login_pw = "Melton1763"

    def login(self):
        driver = webdriver.Chrome(executable_path=self.path)
        driver.get("https://account.adobe.com/plans/60D0061FE73898D77CDA/plans/60D0061FE73898D77CDA")
        
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
            return driver, True

        except:
            driver.close()
            time.sleep(3600)
            return False

    def get_trial(self, driver):
        ##プランを管理
            try:
                plan_path = 'card-footer'
                tag_path = 'a'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, plan_path)))
                fotter = driver.find_elements_by_class_name(plan_path)
                aTag = fotter.find_element_by_tag_name(tag_path)
                aTag.find_element_by_class_name(
                    'spectrum-Button--quiet spectrum-Button spectrum-Button--primary').click()

            except:
                plan_path = '//*[@id="app"]/div/div/div[3]/main/div/div[2]/div/div[2]/div/div[1]/div/div[2]/a[1]'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.XPATH, plan_path)))
                driver.find_element_by_xpath(plan_path).click()
        ##プランを解約        
            try:
                kaiyaku_path = 'spectrum-Button--quiet spectrum-Button spectrum-Button--primary nowrap-text'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, kaiyaku_path)))
                driver.find_element_by_class_name(kaiyaku_path).click()
            except:
                kaiyaku_path = '//*[@id="app"]/div/div/div[3]/main/div/div[2]/div/div[2]/div/div[1]/div/div[2]/a[1]'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.XPATH, kaiyaku_path)))
                driver.find_element_by_xpath(kaiyaku_path).click()
        ##checkbox
            try:
                check_box_path = 'spectrum-Checkbox-input'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, check_box_path)))
                driver.find_element_by_class_name(check_box_path).click()
            except:
                check_box_path = '//*[@id="app"]/div/div/main/div/div[2]/div[2]/div/div[1]/div/div[1]/label[1]/input'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.XPATH, check_box_path)))
                driver.find_element_by_xpath(check_box_path).click()
        ##checkbox_continue
            try:
                continue_path = 'spectrum-Button-label'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, continue_path)))
                driver.find_element_by_class_name(continue_path).click()
            except:
                continue_path = '//*[@id="app"]/div/div/main/div/div[2]/div[3]/div/button[2]/span'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.XPATH, continue_path)))
                driver.find_element_by_xpath(continue_path).click()
        ##popup
            try:
                popup_path = '//*[@id="react-spectrum-62"]/div[3]/button[1]/span'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.XPATH, popup_path)))
                driver.find_element_by_xpath(popup_path).click()
            except:
                popup_path = 'spectrum-Button spectrum-Button--secondary'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, popup_path)))
                driver.find_element_by_class_name(popup_path).click()
        ##詳細continue
            try:
                continue_path2 = 'spectrum-Button-label'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, continue_path2)))
                driver.find_element_by_class_name(continue_path2).click()
            except:
                continue_path2 = '//*[@id="app"]/div/div/main/div/div[2]/div[2]/div[2]/div/button[3]/span'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.XPATH, continue_path2)))
                driver.find_element_by_xpath(continue_path2).click()
        ##得点を受け取る    
            try:
                get_path = 'spectrum-Button-label'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, get_path)))
                driver.find_element_by_class_name(get_path).click()
                time.sleep(3)
            except:
                get_path = '//*[@id="app"]/div/div/main/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[3]/button/span'
                WebDriverWait(driver, self.wait_time).until(
                    EC.presence_of_element_located((By.XPATH, get_path)))
                driver.find_element_by_xpath(get_path).click()
                time.sleep(3)
        ##完了
            driver.get('https://account.adobe.com/plans')
            # try:
            #     comp_path = '//*[@id="react-spectrum-70"]/div[4]/div/button/span'
            #     WebDriverWait(driver, 20).until(
            #         EC.presence_of_element_located((By.XPATH, comp_path)))
            #     driver.find_element_by_xpath(comp_path).click()
            # except:
            #     comp_path = '//*[@id = "react-spectrum-69"]/div[4]/div/button/span'
            #     WebDriverWait(driver, 20).until(
            #         EC.presence_of_element_located((By.XPATH, comp_path)))
            #     driver.find_element_by_xpath(comp_path).click()
        
def main():
    work = adobe_trial()
    count = 0
    driver, ans = work.login()
    while True:
        if ans == True:
            work.get_trial(driver)
            count += 1
        else:
            pass
        print(count)

if __name__ == '__main__':
    main()

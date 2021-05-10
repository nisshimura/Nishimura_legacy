import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def get_adebe_trial():
    path = "../driver/chromedriver_win90.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get(
        "https://account.adobe.com/plans/60D0061FE73898D77CDA/plans/60D0061FE73898D77CDA")

    #最大待機時間（秒）
    wait_time = 5

    login_id = "ntakayki01@mineo.jp"
    login_pw = "Melton1763"

    ### IDを入力
    login_id_xpath = '//*[@id="EmailPage-EmailField"]'
    continue_botton_path = '//*[@id="EmailForm"]/section[2]/div[2]/button/span'

    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_xpath(login_id_xpath).send_keys(login_id)
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, continue_botton_path)))
    driver.find_element_by_xpath(continue_botton_path).click()

    try:
        ### パスワードを入力
        login_pw_xpath = '//*[@id="PasswordPage-PasswordField"]'
        continue_botton_path2 = '//*[@id="PasswordForm"]/section[2]/div[2]/button/span'
        # xpathの要素が見つかるまで待機します。
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
        driver.find_element_by_name("password").send_keys(login_pw)
        time.sleep(1)  # クリックされずに処理が終わるのを防ぐために追加。
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, continue_botton_path2)))
        driver.find_element_by_xpath(continue_botton_path2).click()

        skip_path = '//*[@id="App"]/div/div/section/div/div/section/div/section/div/div/section[2]/footer/div/button/span'
        try:
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, skip_path)))
            driver.find_element_by_xpath(skip_path).click()
        except:
            pass
        plan_path = '//*[@id="app"]/div/div/div[3]/main/div/div[2]/div/ul/li/div/div[3]/a[1]'
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, plan_path)))
        driver.find_element_by_xpath(plan_path).click()

        kaiyaku_path = '//*[@id="app"]/div/div/div[3]/main/div/div[2]/div/div[2]/div/div[1]/div/div[2]/a[1]'
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, kaiyaku_path)))
        driver.find_element_by_xpath(kaiyaku_path).click()

        check_box_path = '//*[@id="app"]/div/div/main/div/div[2]/div[2]/div/div[1]/div/div[1]/label[1]/input'
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, check_box_path)))
        driver.find_element_by_xpath(check_box_path).click()

        continue_path = '//*[@id="app"]/div/div/main/div/div[2]/div[3]/div/button[2]/span'
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, continue_path)))
        driver.find_element_by_xpath(continue_path).click()
        kakunin_path = '//*[@id="react-spectrum-62"]/div[3]/button[1]/span'

        try:
            # 操作できる画面の一覧を取得(Popup後に処理)
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, kakunin_path)))
            driver.find_element_by_xpath(kakunin_path).click()
            continue3_path = '//*[@id="app"]/div/div/main/div/div[2]/div[2]/div[2]/div/button[3]/span'
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, continue3_path)))
            driver.find_element_by_xpath(continue3_path).click()

        except:
            continue_path2 = '//*[@id="app"]/div/div/main/div/div[2]/div[2]/div[2]/div/button[3]/span'
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, continue_path2)))
            driver.find_element_by_xpath(continue_path2).click()

        get_path = '//*[@id="app"]/div/div/main/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[3]/button/span'
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, get_path)))
        driver.find_element_by_xpath(get_path).click()
        time.sleep(3)
        driver.close()
        return True
    except:
        driver.close()
        time.sleep(600)
        return False

count = 0
while True:
    if get_adebe_trial() == True:
        count += 1
    else:
        pass
    print(count)

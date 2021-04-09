from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import os 
import shutil
import pathlib
import wx
import threading
from selenium.webdriver.chrome.options import Options as chrome_op
import os 

class Jobcanget():
    
    
    dawnloadfile = os.path.abspath('./dawnload')

    def startcheckfile(self):
        if not os.path.exists(pathlib.Path(self.dawnloadfile)):
            os.mkdir(pathlib.Path(self.dawnloadfile))
        list_dir = os.listdir(str(pathlib.Path(self.dawnloadfile)))    
        self.list_dir = list_dir
    
    def endcheckfile(self):
        list_dirend = os.listdir(str(pathlib.Path(self.dawnloadfile)))
        return list_dirend

    def make_driver(self, path):
        options = chrome_op()
        #options.add_argument('headless')
        prefs = {"download.default_directory" : self.dawnloadfile, 
        "download.prompt_for_download": False, 
        "download.directory_upgrade": True}
        options.add_experimental_option("prefs",prefs)

        driver = webdriver.Chrome(executable_path = str(pathlib.Path(path)),options=options)
        driver.get("https://ssl.jobcan.jp/client/man-hour-manage/csv")
        self.driver = driver

    def login(self, id_co, id_ps, password):
        driver = self.driver

        user_co = driver.find_element_by_id('client_login_id')
        user_ps = driver.find_element_by_id('client_manager_login_id')
        user_password = driver.find_element_by_id('client_login_password')

        user_co.send_keys(id_co)
        user_ps.send_keys(id_ps)
        user_password.send_keys(password)

        driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[5]/button').click()
    
    def get_csv(self,from_year,from_month,from_day,savefile):
        driver = self.driver
        start_year = driver.find_element_by_id('from_year')
        start_month = driver.find_element_by_id('from_month')
        start_day = driver.find_element_by_id('from_day')


        start_year = Select(start_year)
        start_month = Select(start_month)
        start_day = Select(start_day)


        start_year.select_by_value(from_year)
        start_month.select_by_value(from_month)
        start_day.select_by_value(from_day)

        driver.find_element_by_xpath('//*[@id="csv-download"]/td/button').click()
        
        for i in range(200):
            num = self.endcheckfile()
            if len(num) == len(self.list_dir):
                time.sleep(5)
                print('dawnloading...')
                pass
            else:
                new_file = list(set(num) - set(self.list_dir))
                shutil.move(pathlib.Path(self.dawnloadfile + '/'+ str(new_file[0])), pathlib.Path(savefile + '/' + str(new_file[0])))
                if i == 199:
                    print('WE COULD NOT GET DATAS')
                break
                
    def finish(self):
        driver = self.driver
        driver.close()
        driver.quit()

def main():
    path = './external/chromedriver_win87.exe'

    id_co = 'sophia3434'
    id_ps = 't-sakoda'
    password = 'sophia2020'

    from_year = '2020'
    from_month = '4'
    from_day = '1'

    savefile = './jobcancsv'
    
    work = Jobcanget()
    work.startcheckfile()
    work.make_driver(path)
    work.login(id_co, id_ps, password)
    work.get_csv(from_year,from_month,from_day,savefile)
    work.finish()
    print('SUCCESS')

if __name__ == "__main__":
    main()
    
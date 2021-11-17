from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_op
import os
import re 
import datetime
import threading
import time 

class scrs():
    
    def __init__(self,path_A,path_B,path_C,Range,excel_file,save_file,sheet_NO,page_Weight):
        
        options = chrome_op()
        options.add_argument('-headless')
        
        self.driver_A = webdriver.Chrome(executable_path=path_A,options=options)
        self.driver_B = webdriver.Chrome(executable_path=path_B,options=options)
        self.driver_C = webdriver.Chrome(executable_path=path_C,options=options)
        
        self.path_A = path_A                                                                            # path = "C:\chrome\chromedriver.exe"
        self.path_B = path_B
        self.path_C = path_C

        self.Range = Range                                                                              # Range = "B5:G68"
        self.excel_file = excel_file                                                                    # excel_file = "C:\programing\Atom_collection\code_webdifferent\【&mall】2020年3月リニューアル静的ページ一覧 (3).xlsx"
        self.save_file = save_file + '\\[parallel][Ch]' + re.sub(' |:','',str(datetime.datetime.now())) # save_file = "C:\programing\Atom_collection\screenshot_programing\scrs_"
        self.sheet_NO = sheet_NO                                                                        # 1からスタート
        self.page_weight = page_Weight

        if not os.path.exists(self.save_file):
            os.mkdir(self.save_file)

        self.large_list = []

    def get_data(self):
        
        workbook = load_workbook(filename=self.excel_file,read_only=False)
        sheet = workbook.get_sheet_names()

        target = workbook[sheet[self.sheet_NO]]

        extent = target[self.Range]

        for row in extent:
            
            small_list = [i.value for i in row]
            
            self.large_list.append(small_list)
            

            

        return self.large_list

    def get_capture_A(self):
        
        save_file_A = self.save_file + "\\ソフィア開発環境"
        if not os.path.exists(save_file_A):
            os.mkdir(save_file_A)
        
        driver = self.driver_A
        
        for i in self.large_list:
            name_A = 'A' + '_' + str(i[0]) + '_' + str(i[1]) + '_' + str(i[2])
            
            try:
                url = re.search(r"(?<=\").*?(?=\")", i[3]).group()
                driver.get(url)
            except:
                print('failed to match A NO' + str(i[0]) + '(空欄or範囲に列名含んでる)')
                
            # page_width = driver.execute_script('return document.body.scrollWidth')
            page_height = driver.execute_script('return document.body.scrollHeight')
            driver.set_window_size(self.page_weight, page_height)

            driver.save_screenshot(save_file_A + "\\[Ch]" + name_A + ".png")
            

    def get_capture_B(self):
        
        save_file_B = self.save_file + "\\検証環境3URL"
        if not os.path.exists(save_file_B):
            os.mkdir(save_file_B)

        driver = self.driver_B
        
        for i in self.large_list:
            name_B = 'B' + '_' + str(i[0]) + '_' + str(i[1]) + '_' + str(i[2])
            
           
            try:
                url = re.search(r"(?<=\").*?(?=\")", i[4]).group()
                time.sleep(0)
                driver.get(url)
            except:
                print('failed to match B NO' + str(i[0]) + '(空欄or範囲に列名含んでる)')
                
            # page_width = driver.execute_script('return document.body.scrollWidth')
            try:
                page_height = driver.execute_script('return document.body.scrollHeight')
            except:
                time.sleep(15)
                page_height = driver.execute_script('return document.body.scrollHeight')
                
            driver.set_window_size(self.page_weight, page_height)

            driver.save_screenshot(save_file_B + "\\[Ch]" + name_B + ".png")
    
    
    def get_capture_C(self):
        
        save_file_C = self.save_file + "\\本番用URL"
        if not os.path.exists(save_file_C):
            os.mkdir(save_file_C)

        driver = self.driver_C

        for i in self.large_list:
            name_C = 'C' + '_' + str(i[0]) + '_' + str(i[1]) + '_' + str(i[2])
            

            try:
                url = re.search(r"(?<=\").*?(?=\")", i[5]).group()
                driver.get(url)
            except:
                print('failed to match C NO' + str(i[0]) + '(空欄or範囲に列名含んでる)')
               
            # page_width = driver.execute_script('return document.body.scrollWidth')
            page_height = driver.execute_script('return document.body.scrollHeight')
            driver.set_window_size(self.page_weight, page_height)

            driver.save_screenshot(save_file_C + "\\[Ch]" + name_C + ".png")
            
    def end(self):
        self.driver_A.quit()
        self.driver_B.quit()
        self.driver_C.quit()

def main_series():              #直列処理
    work = scrs(
        "C:\chrome\chromedriver.exe",
        "C:\chrome\chromedriver - コピー.exe",
        "C:\chrome\chromedriver - コピー (2).exe",
        "B5:G100",
        "C:\programing\Atom_collection\code_webdifferent\【&mall】2020年3月リニューアル静的ページ一覧_20200309.xlsx",
        "C:\programing\Atom_collection\screenshot_programing",
        2,
        750
        )
    
    work.get_data()
    work.get_capture_A()
    work.get_capture_B()
    work.get_capture_C()
    work.end()


def main_parallel():                #並列処理
    work = scrs(
        "C:\chrome\chromedriver.exe",
        "C:\chrome\chromedriver - コピー.exe",
        "C:\chrome\chromedriver - コピー (2).exe",
        "B5:G403",
        "C:\programing\Atom_collection\code_webdifferent\【&mall】2020年3月リニューアル静的ページ一覧_20200309.xlsx",
        "C:\programing\Atom_collection\screenshot_programing",
        2,
        750
        )
    
    work.get_data()
    
    threadA = threading.Thread(target=work.get_capture_A)
    threadB = threading.Thread(target=work.get_capture_B)
    threadC = threading.Thread(target=work.get_capture_C)　　　　　#capture_Cも同時に並列処理するとBが先走り、タイムアウトになることがある
    
    threadA.start()
    threadB.start()
    threadC.start()                                               　#capture_Cも同時に並列処理するとBが先走り、タイムアウトになることがある
    
    threadA.join()
    threadB.join()
    threadC.join()                                                  #capture_Cも同時に並列処理するとBが先走り、タイムアウトになることがある
    
    # work.get_capture_A()
    # work.get_capture_B()
    # work.get_capture_C()            

    work.end()


if __name__ == "__main__":
    main_parallel()
    #main_series()
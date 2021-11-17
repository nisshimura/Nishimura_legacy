from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_op
import os
import re 
import datetime

sheet_num = 1

Range_1 = "B142:G145"
Range_2 = "B5:G402"

Name_A = "ソフィア開発環境"
Name_B = "検証環境3URL"
Name_C = "本番用URL"

excel_file = "C:\programing\Atom_collection\code_webdifferent\【&mall】2020年3月リニューアル静的ページ一覧_20200309.xlsx"
save_file = "C:\\programing\\Atom_collection\\screenshot_programing\\[series][Ch]" + re.sub(' |:','',str(datetime.datetime.now()))


path = "C:\chrome\chromedriver.exe"

options = chrome_op()
options.add_argument('-headless')
driver = webdriver.Chrome(executable_path=path,options=options)

workbook = load_workbook(filename=excel_file,read_only=False)
sheet = workbook.get_sheet_names()



large_list = []

for j in range(sheet_num):
    
    number = j + 1

    save_file_A = save_file + "\\" + "(" + str(number) + ")"+ Name_A
    save_file_B = save_file + "\\" + "(" + str(number) + ")"+ Name_B
    save_file_C = save_file + "\\" + "(" + str(number) + ")"+ Name_C

    if not os.path.exists(save_file):
        os.mkdir(save_file)
    if not os.path.exists(save_file_A):
        os.mkdir(save_file_A)
    if not os.path.exists(save_file_B):
        os.mkdir(save_file_B)
    if not os.path.exists(save_file_C):
        os.mkdir(save_file_C)
    target = workbook[sheet[number]]

    if number == 1:
        extent = target[Range_1]
    elif number ==2:
        extent = target[Range_2]

    

    for row in extent:
        name = [cell.value for cell in row]
        large_list.append(name)


    for i in large_list:
    
        name_A ='A_' + str(i[0]) + '_' + str(i[1]) + '_' + str(i[2])
        name_B ='B_' + str(i[0]) + '_' + str(i[1]) + '_' + str(i[2])
        name_C ='C_' + str(i[0]) + '_' + str(i[1]) + '_' + str(i[2])

        for index in [i[3],i[4],i[5]]:
            try:
                url = re.search(r"(?<=\").*?(?=\")", index).group()
                driver.get(url)

                # page_width = driver.execute_script('return document.body.scrollWidth')
                page_height = driver.execute_script('return document.body.scrollHeight')
                driver.set_window_size(750, page_height)

                if index == i[3]:
                    driver.save_screenshot(save_file_A + "\\" + name_A + ".png")

                elif index == i[4]:
                    driver.save_screenshot(save_file_B + "\\" + name_B + ".png")
                    
                elif index == i[5]:
                    driver.save_screenshot(save_file_C + "\\" + name_C + ".png")
            
            except:
                print('failed to match URL NO' + str(i[0]))


                

driver.quit()



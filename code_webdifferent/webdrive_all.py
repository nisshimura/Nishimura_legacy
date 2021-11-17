from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_op
from selenium.webdriver.firefox.options import Options as FF_op
import os
import re
import time
from PIL import Image
import math

class disp_cap():

        chrome_path = "C:\chrome\chromedriver.exe"
        ME_path = "C:\chrome\msedgedriver.exe"
        FF_path = "C:\chrome\geckodriver.exe"
        IE_path = "C:\chrome\IEDriverServer.exe"
        Old_ME_path = "MicrosoftWebDriver.exe"

        save_file = "C:\programing\Atom_collection\screenshot_programing"
        url =  "http://www.grand-tree.jp/web/index.htm"

        s = re.match("https?://w*[^/]+/",url)
        st = re.sub("/","",s.group())
        new_url = re.sub("https?:","",st)

        File = save_file + '\\' + new_url



        if not os.path.exists(File):
            os.mkdir(File)

        def chrome_s(self):
            
            chrome_list_http = [self.url]
            count = 0

            path = self.chrome_path
            options = chrome_op()
            options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path=path, options=options)

            driver.get(self.url)

            elems = driver.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                http = elem.get_attribute("href")
                chrome_list_http.append(http)
            
            chrome_list_url = [s for s in chrome_list_http if s.startswith('http')]
            chrome_list_url = set(chrome_list_url)
            print(chrome_list_url)
            # print(chrome_list_http)
            
            for i in chrome_list_url:
                driver.get(i)

                page_width = driver.execute_script('return document.body.scrollWidth')
                page_height = driver.execute_script('return document.body.scrollHeight')
                driver.set_window_size(page_width, page_height)
                # print(page_width, page_height)
                
                driver.save_screenshot(self.File + "\chrome_" + str(count) + ".png")
                
                count += 1


            driver.quit()

        def ME_s(self):
            
            ME_list_http = [self.url]
            count = 0
            
            path = self.ME_path
            options = chrome_op()
            options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path=path,options=options)

            driver.get(self.url)

            elems = driver.find_elements_by_xpath("//a[@href]")

            for elem in elems:
                http = elem.get_attribute("href")
                ME_list_http.append(http)
            
            # print(ME_list_http)
            
            ME_list_url = [s for s in ME_list_http if s.startswith('http')]
            ME_list_url = set(ME_list_url)
            # print(ME_list)
            
            for i in ME_list_url:
                driver.get(i)
                page_width = driver.execute_script('return document.body.scrollWidth')
                page_height = driver.execute_script('return document.body.scrollHeight')
                driver.set_window_size(page_width, page_height)
                #print(page_width, page_height)
                
                driver.save_screenshot(self.File + "\ME_" + str(count) + ".png")
                
                count += 1

            driver.quit()

        def FF_s(self):
            
            FF_list_http = [self.url]
            count = 0

            options = FF_op()
            options.add_argument('-headless')
            path = self.FF_path
            driver = webdriver.Firefox(executable_path=path,options=options)

            driver.get(self.url)

            elems = driver.find_elements_by_xpath("//a[@href]")

            for elem in elems:
                http = elem.get_attribute("href")
                FF_list_http.append(http)
            
            # print(FF_list_http)

            FF_list_url = [s for s in FF_list_http if s.startswith('http')]
            FF_list_url = set(FF_list_url)
            # print(FF_list)

            for i in FF_list_url:
                driver.get(i)

                page_width = driver.execute_script('return document.body.scrollWidth')
                page_height = driver.execute_script('return document.body.scrollHeight')
                driver.set_window_size(page_width, page_height)
                #print(page_width, page_height)
                
                driver.save_screenshot(self.File + "\FF_" + str(count) + ".png")
                
                count += 1

            driver.quit()

        def IE_s(self):
            
            IE_list_http =[self.url]
            count = 0
            
            path = self.IE_path
            driver = webdriver.Ie(executable_path=path)
            driver.get(self.url)
            
            elems = driver.find_elements_by_xpath("//a[@href]")

            for elem in elems:
                http = elem.get_attribute("href")
                IE_list_http.append(http)

            IE_list_url = [s for s in IE_list_http if s.startswith(self.s.group())]
            IE_list_url = set(IE_list_url)
            
            # driver.execute_script('window.scrollTo(0,0);')
            for i in IE_list_url:
                driver.get(i)
                # driver.maximize_window()
                
                page_width = driver.execute_script('return document.body.scrollWidth')
                page_height = driver.execute_script('return document.body.scrollHeight')

                # size = driver.get_window_rect()
                # view_width = size['width']
                # view_height = size['height']
                
                driver.save_screenshot(self.File + "\IE_ex_" + str(count) + ".png")
                ex_photo = Image.open(self.File + "\IE_ex_" + str(count) + ".png")

                ex_width = ex_photo.width
                ex_height = ex_photo.height
                ex_photo.close()
                os.remove(self.File + "\IE_ex_" + str(count) + ".png")

                times_width = math.ceil(page_width / ex_width)#
                times_height = math.ceil(page_height / ex_height)#

                background = Image.new('RGB',(ex_width,page_height))

                for i in range (times_height):
                    folder = self.File + "\IE_" + str(i) +".png"
                    driver.execute_script('window.scrollTo(0,' + str(ex_height*i) +')')        
                    time.sleep(0)
                    driver.save_screenshot(folder)
                    photo = Image.open(folder)

                    if i == times_height-1:    
                        photo = photo.crop((0,ex_height-page_height%ex_height,ex_width,ex_height))
                        background.paste(photo,(0,ex_height*i))
                        os.remove(folder)
                    else:    
                        background.paste(photo,(0,ex_height*i))
                        os.remove(folder)

                background.save(self.File + "\IE_" + str(count) + ".png")
                count += 1
                
            driver.quit()

        def Old_ME_s(self):
            
            Old_ME_list_http =[self.url]
            count = 0
            
            path = self.Old_ME_path
            driver = webdriver.Edge(executable_path=path)
            driver.get(self.url)
            
            elems = driver.find_elements_by_xpath("//a[@href]")

            for elem in elems:
                http = elem.get_attribute("href")
                Old_ME_list_http.append(http)

            Old_ME_list_url = [s for s in Old_ME_list_http if s.startswith('http')]
            Old_ME_list_url = set(Old_ME_list_url)

            # driver.execute_script('window.scrollTo(0,0);')
            for i in Old_ME_list_url:
                driver.get(i)
                driver.maximize_window()

                page_width = driver.execute_script('return document.body.scrollWidth')
                page_height = driver.execute_script('return document.body.scrollHeight')

                size = driver.get_window_rect()
                view_width = size['width']
                view_height = size['height']

                driver.save_screenshot(self.File + "\Old_ME_ex_" + str(count) + ".png")
                ex_photo = Image.open(self.File + "\Old_ME_ex_" + str(count) + ".png")

                ex_width = ex_photo.width
                ex_height = ex_photo.height
                ex_photo.close()
                #os.remove(save_file + '\ex.png')

                times_width = math.ceil(page_width / ex_width)#
                times_height = math.ceil(page_height / ex_height)#

                background = Image.new('RGB',(ex_width,page_height))

                # for index in range (times_width):
                #     for i in range (times_height):
                #         file = save_file + "\IE_" + str(index) + '_' + str(i) +".png"
                #         driver.execute_script('window.scrollTo(' + str(view_width*index) + ',' + str(ex_height*i) +')')          
                #         driver.save_screenshot(file)
                #         photo = Image.open(file)

                #         if i == times_height-1:    
                #             photo = photo.crop((0,ex_height-page_height%ex_height,ex_width,ex_height))
                #             background.paste(photo,(view_width*index,ex_height*i))
                #             os.remove(file)
                #         else:    
                #             background.paste(photo,(view_width*index,ex_height*i))
                        # os.remove(file)


                for i in range (times_height):
                    folder = self.File + "\Old_ME_" + str(i) +".png"
                    driver.execute_script('window.scrollTo(0,' + str(ex_height*i) +')')        
                    time.sleep(0)
                    driver.save_screenshot(folder)
                    photo = Image.open(folder)

                    if i == times_height-1:    
                        photo = photo.crop((0,ex_height-page_height%ex_height,ex_width,ex_height))
                        background.paste(photo,(0,ex_height*i))
                        os.remove(folder)
                    else:    
                        background.paste(photo,(0,ex_height*i))
                        os.remove(folder)

                    background.save(self.File + "\Old_ME_" + str(count) + ".png")
                    count += 1
                
                driver.quit()

def main():
    work = disp_cap()
    work.chrome_s()    
    work.ME_s()
    work.FF_s()
    work.IE_s()
    # work.Old_ME_s()

if __name__ == "__main__":
    main()









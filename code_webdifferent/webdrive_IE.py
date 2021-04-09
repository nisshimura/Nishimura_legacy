from selenium import webdriver 
from PIL import Image
import time
import math 
import os 

path = "C:\chrome\IEDriverServer.exe"
url =  "http://www.grand-tree.jp/web/index.htm"
save_file = "C:\programing\Atom_collection\screenshot_programing"

driver = webdriver.Ie(executable_path=path)
driver.get(url)

driver.maximize_window()

driver.execute_script('window.scrollTo(0,0);')

page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')

size = driver.get_window_rect()
view_width = size['width']
view_height = size['height']

#driver.set_window_size(view_width,view_height)

print(driver.get_window_rect())
print(page_width, page_height)
print(view_width, view_height)

driver.save_screenshot(save_file + '\ex.png')
ex_photo = Image.open(save_file + '\ex.png')

print(ex_photo.size)

ex_width = ex_photo.width
ex_height = ex_photo.height
ex_photo.close()
os.remove(save_file + '\ex.png')

times_width = math.ceil(page_width / ex_width)#
times_height = math.ceil(page_height / ex_height)#

print(times_width, times_height)

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
    file = save_file + "\IE_" + str(i) +".png"
    driver.execute_script('window.scrollTo(0,' + str(ex_height*i) +')')        
    time.sleep(0)
    driver.save_screenshot(file)
    photo = Image.open(file)

    if i == times_height-1:    
        photo = photo.crop((0,ex_height-page_height%ex_height,ex_width,ex_height))
        background.paste(photo,(0,ex_height*i))
        os.remove(file)
    else:    
        background.paste(photo,(0,ex_height*i))
        os.remove(file)

background.save("C:\programing\Atom_collection\screenshot_programing\IE_.png")
driver.quit()





from selenium import webdriver
import subprocess
import os
import shutil
import datetime
import time

class GetRadio():
    
    def __init__(self):
        self.url = 'https://www.jcbasimul.com/radio/1249/'
        self.driver_path = '/home/pi/university/prokiso/chromedriver'
        
        self.ogvpath = '/home/pi/university/prokiso/videos_ogv'

        
    def initialize(self):
        shutil.rmtree(self.ogvpath)
        os.mkdir(self.ogvpath)
        
        t = str(datetime.date.today())
        t = t.replace('-','')
        self.date = t
        
        ogvpath = '/home/pi/university/prokiso/videos_ogv'
        self.ogvpath = ogvpath + '/'+self.date+'.ogv'
    def get_web(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.url)
        time.sleep(10)
        
        self.driver.find_element_by_class_name('embeddable-player-pause').click()
        time.sleep(10)
        
    def end_web(self):
        self.driver.close()

    def start_capture(self):
        cmd = 'recordmydesktop -o '+self.ogvpath+' --device pulse'
        subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        
    def end_capture(self):
        num = subprocess.run('pidof recordmydesktop',encoding='utf-8',stdout=subprocess.PIPE,shell=True)
        print(num)
        subprocess.run('kill {}'.format(num.stdout),shell=True)
        
def main():
    work = GetRadio()
    print('start....')
    work.initialize()
    work.get_web()
    work.start_capture()
    print('Start capturing')
    time.sleep(10)
    work.end_capture()
    work.end_web()
    print('finish cap ....')

if __name__ == "__main__":
    main()
    
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
        self.mp4path = '/home/pi/university/prokiso/videos_mp4'

        
    def initialize(self):
        shutil.rmtree(self.ogvpath)
        os.mkdir(self.ogvpath)
        
        shutil.rmtree(self.mp4path)
        os.mkdir(self.mp4path)
        
        t = str(datetime.date.today())
        t = t.replace('-','')
        self.date = t
        
        mp3path = '/home/pi/university/prokiso/videos_mp3'
        self.mp3path = mp3path + '/'+self.date+'.mp3'
    def get_web(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.url)
        time.sleep(10)
        
        self.driver.find_element_by_class_name('embeddable-player-pause').click()
        time.sleep(10)
        
    def end_web(self):
        self.driver.close()

    def convert_to_mp4(self):
        cmd = 'ffmpeg -i '+self.ogvpath+'/out.ogv -f mp4 -s 1280x720 -r 29.97 -vcodec mpeg4 -b 3000k -acodec aac -ab 320k '+self.mp4path+'/out.mp4'
        subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        
    def convert_to_mp3(self):
        cmd2 = 'ffmpeg -i '+self.mp4path+'/out.mp4'+' -r 60 '+self.mp3path
        subprocess.Popen(cmd2,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        
    def start_capture(self):
        cmd = 'recordmydesktop -o /home/pi/university/prokiso/videos_ogv/out.ogv --device pulse'
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
    while not os.path.isfile('/home/pi/university/prokiso/videos_ogv/out.ogv'):
        time.sleep(10)
    print('start convert to mp4')    
    work.convert_to_mp4()
    while not os.path.isfile('/home/pi/university/prokiso/videos_mp4/out.mp4'):
        time.sleep(10)
    print('start convert to mp3')
    work.convert_to_mp3()

if __name__ == "__main__":
    main()
        #
        #
        ]ffmpeg -i /home/pi/university/prokiso/videos_ogv/out.ogv -f mp4 -s 1280x720 -r 29.97 -vcodec mpeg4 -b 3000k -acodec aac -ab 320k /home/pi/university/prokiso/videos_mp4/out.mp4
        
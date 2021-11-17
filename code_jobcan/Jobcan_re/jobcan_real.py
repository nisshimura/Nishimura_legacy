import random
import nfc
import binascii
import time 
import pygame.mixer 
import os 
import pandas as pd 
import csv
import threading
from selenium import webdriver

class jobCan():
        


    def __init__(self):
        self.music_list = []

        self.UserMail = {}
        self.UserPass = {}
        self.win_csv = ".\\code_jobcan\\Jobcan_re\\CSV_data\\sophia.csv"
        self.ras_csv = "sophia.csv"

        self.win_path1 = ".\code_jobcan\Jobcan_re\chromedriver1.exe"
        self.win_path2 = ".\code_jobcan\Jobcan_re\chromedriver2.exe"
        self.ras_path = "/usr/bin/choromedriver"

        self.device = os.name

        if self.device == "nt":
            df = pd.read_csv(self.win_csv, encoding='cp932')
        else:
            df = pd.read_csv(self.ras_csv, encoding='cp932')

        try:
            for index in range(10):
                self.UserMail[df.IDM[index].encode()] = df.userID[index]
                self.UserPass[df.IDM[index].encode()] = df.password[index]
        except:
            print('we have no users')
            pass
        
    
    def get_idm(self):
        
        clf = nfc.ContactlessFrontend('usb')
                                      
        print('カードをタッチしてください')
        tag = clf.connect(rdwr={'on-connect': lambda tag : False})
        clf.close()
        self.idm = binascii.hexlify(tag.idm)    #print(idm)
        print(self.idm)
    
    def confirm(self):
        if self.idm in self.UserMail and self.UserPass:
            self.ID = self.UserMail[self.idm] 
            self.Password = self.UserPass[self.idm]
            self.play_music_Accept()
            return True

        else:
            self.play_music_False()
            return False

    def webdrive(self):
        
        if self.device == 'nt':
<<<<<<< HEAD:code_jobcan/Jobcan_re/jobcan_real.py
            path =  self.win_path1   
=======
            path = ".\external\chromedriver_win83.exe"  
>>>>>>> 6bcaa64c4264a24f8169d0e53f7dba2f9a2de0a1:code_jobcan/jobcan_real.py
        else:
            path =  self.ras_path
        
        driver = webdriver.Chrome(executable_path=path)
        driver.get("https://id.jobcan.jp/users/sign_in?app_key=atd")

        user_name = driver.find_element_by_id('user_email')
        user_password = driver.find_element_by_id('user_password')

        user_name.send_keys(self.ID)
        user_password.send_keys(self.Password)

        driver.find_element_by_class_name('form__login').click()

        time.sleep(1)

        driver.find_element_by_id('adit-button-push').click()
        time.sleep(1)
        driver.close()

    def play_music_Accept(self):
        
        pygame.mixer.init()
        
        if self.device == 'nt':
<<<<<<< HEAD:code_jobcan/Jobcan_re/jobcan_real.py
            path = ".\code_jobcan\Jobcan_re\pi.mp3"
=======
            path = ".\sound\decision1.mp3"
>>>>>>> 6bcaa64c4264a24f8169d0e53f7dba2f9a2de0a1:code_jobcan/jobcan_real.py
        else:
            path = "/home/pi/nishhimura/music/Doorbell-Melody01-.mp3"
        
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(1)
        time.sleep(1)
        pygame.mixer.music.stop()

    def play_music_True(self):
        if self.device == 'nt':
<<<<<<< HEAD:code_jobcan/Jobcan_re/jobcan_real.py
            path = self.win_path2
=======
            path = ".\external\chromedriver_win83.exe"
>>>>>>> 6bcaa64c4264a24f8169d0e53f7dba2f9a2de0a1:code_jobcan/jobcan_real.py
        else:
            path = self.ras_path

        driver = webdriver.Chrome(executable_path=path)
<<<<<<< HEAD:code_jobcan/Jobcan_re/jobcan_real.py
        
        driver.get('https://recochoku.jp/ranking/single/daily')
        driver.find_element_by_xpath(
            '//*[@id = "rankingContents"]/div[1]/div[2]/button').click()
=======
        driver.get("https://recochoku.jp/ranking/single/daily")

        driver.find_element_by_xpath('//*[@id="rankingContents"]/div[1]/div[2]/button').click()

>>>>>>> 6bcaa64c4264a24f8169d0e53f7dba2f9a2de0a1:code_jobcan/jobcan_real.py

        time.sleep(5)

        driver.close()


    def play_music_False(self):
        pygame.mixer.init()
        
        if self.device == 'nt':
<<<<<<< HEAD:code_jobcan/Jobcan_re/jobcan_real.py
            path = ".\\code_jobcan\\Jobcan_re\\batsu.mp3"
=======
            path = ".\sound\incorrect1.mp3"
>>>>>>> 6bcaa64c4264a24f8169d0e53f7dba2f9a2de0a1:code_jobcan/jobcan_real.py
        else:
            path = "/home/pi/nishhimura/sound/symphony7.mp3"
        
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(1)
        time.sleep(1)
        pygame.mixer.music.stop()
        main()
    
def main():
    while True:
        work = jobCan()
<<<<<<< HEAD:code_jobcan/Jobcan_re/jobcan_real.py
        work.get_idm()
        work.confirm()
        print(work.confirm())
        t1 = threading.Thread(target=work.webdrive())
        t2 = threading.Thread(target=work.play_music_True())
        
        if work.confirm() == True:
            t1.start()
            t2.start()
        else:
            work.play_music_False()
=======
        # work.get_idm()
        # work.webdrive()
        work.play_music_True()
>>>>>>> 6bcaa64c4264a24f8169d0e53f7dba2f9a2de0a1:code_jobcan/jobcan_real.py

if __name__ == "__main__":
    main()
    

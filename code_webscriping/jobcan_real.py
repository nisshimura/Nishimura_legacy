import nfc
import binascii
from selenium import webdriver
import time 
import pygame.mixer 
import os 
import pandas as pd 
import csv

class jobCan():
        
    UserMail = {}
    UserPass = {}
    
    df = pd.read_csv('sophia.csv', encoding='cp932')
    
    try:
        for index in range(10):
            UserMail[df.IDM[index].encode()]=df.userID[index]
            UserPass[df.IDM[index].encode()]=df.password[index]
    except:
        pass

    def __init__(self):
        
        self.device = os.name
    
    def get_idm(self):
        
        clf = nfc.ContactlessFrontend('usb')
        print('カードをタッチしてください')
        tag = clf.connect(rdwr={'on-connect': lambda tag : False})
        clf.close()
        self.idm = binascii.hexlify(tag.idm)    #print(idm)

    def webdrive(self):
        
        if self.idm  in self.UserMail and self.UserPass:
            ID = self.UserMail[self.idm] 
            Password = self.UserPass[self.idm]
            self.play_music_Accept()
        else:
            self.play_music_False()

        
        if self.device == 'nt':
            path = "C:\chrome\chromedriver.exe"  
        else:
            path = "/usr/bin/choromedriver"
        
        driver = webdriver.Chrome(executable_path=path)
        driver.get("https://id.jobcan.jp/users/sign_in?app_key=atd")

        user_name = driver.find_element_by_id('user_email')
        user_password = driver.find_element_by_id('user_password')

        user_name.send_keys(ID)
        user_password.send_keys(Password)

        driver.find_element_by_class_name('form__login').click()

        time.sleep(1)

        driver.find_element_by_id('adit-button-push').click()
        time.sleep(1)
        driver.close()

    def play_music_Accept(self):
        
        pygame.mixer.init()
        
        if self.device == 'nt':
            path = "C:\sound\Doorbell-Melody01-mp3\Doorbell-Melody01-1.mp3"
        else:
            path = "/home/pi/nishhimura/music/Doorbell-Melody01-.mp3"
        
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(1)
        time.sleep(2)
        pygame.mixer.music.stop()

    def play_music_True(self):
        if self.device == 'nt':
            path = "C:\chrome\chromedriver.exe"  
        else:
            path = "/usr/bin/choromedriver"

        driver = webdriver.Chrome(executable_path=path)
        driver.get("https://recochoku.jp/ranking/single/daily/?affiliate=4305070016")

        driver.find_element_by_xpath('//*[@id="unit"]/table/tbody/tr[1]/td[2]/a[3]/img').click()

        try:
            driver.find_element_by_xpath('//*[@id="abd_0"]/a/img').click()
            driver.find_element_by_xpath('//*[@id="abd_1"]/a/img').click()
            driver.find_element_by_xpath('//*[@id="abd_2"]/a/img').click()
            driver.find_element_by_xpath('//*[@id="abd_3"]/a/img').click()
            driver.find_element_by_xpath('//*[@id="abd_4"]/a/img').click()
        except:
            self.play_music_False()

        time.sleep(5)

        driver.close()


    def play_music_False(self):
        pygame.mixer.init()
        
        if self.device == 'nt':
            path = "C:\sound\incorrect1.mp3"
        else:
            path = "/home/pi/nishhimura/sound/symphony7.mp3"
        
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(1)
        time.sleep(2)
        pygame.mixer.music.stop()
        main()
    
def main():
    while True:
        work = jobCan()
        work.get_idm()
        work.webdrive()
        work.play_music_True()

if __name__ == "__main__":
    main()
    




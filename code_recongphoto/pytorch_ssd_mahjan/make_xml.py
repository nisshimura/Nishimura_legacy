import re
import cv2 
import os 
import random
import math
import time
import pathlib
import xml.etree.ElementTree as ET

class MakeXML():
    def __init__(self):
        self.args = {'bgfile': './VOCdevkit/BCCD/background/mahjan_background.jpg',
                     'origin_hais': './VOCdevkit/BCCD/hai/',
                     'rsize_hais': './VOCdevkit/BCCD/resizehai/',
                     'testset': './VOCdevkit/BCCD/JPEGImages/train/',
                     'anotation_sample': './VOCdevkit/BCCD/Anotatinos_sample/sample.xml',
                     'anotation_folder': './VOCdevkit/BCCD/Annotations/',
                     'trainval_text': './VOCdevkit/BCCD/ImageSets/Main/trainval.txt',
                     'test_text': './VOCdevkit/BCCD/ImageSets/Main/test.txt',
                     'num_xml': 30
                    }
        self.hai_tuple = ('1pin', '2pin', '3pin', '4pin', '5pin', '6pin', '7pin', '8pin', '9pin', '1sou', '2sou', '3sou', '4sou', '5sou',
                    '6sou', '7sou', '8sou', '9sou', '1wan', '2wan', '3wan', '4wan', '5wan', '6wan', '7wan', '8wan', '9wan', 'ton', 'nan', 'sha', 'pe', 'haku', 'hatsu', 'chun')
    
        path = pathlib.Path(self.args['origin_hais'])
        self.origin_list = os.listdir(path)

    def randomhai(self):
        args = self.args
        hai_tuple = self.hai_tuple
        self.controlhai()
        rand = random.randint(0, 33)
        haifile = args['rsize_hais'] + hai_tuple[rand] + '.jpg'
        return haifile, hai_tuple[rand]

    def pastebackground(self,num):
        args = self.args
        bg = cv2.imread(args['bgfile'])

        details = []

        s_list = [570, 650]
        e_list = []

        angle = 15

        for i in range(14):
            haifile, hainame = self.randomhai()
            hai = cv2.imread(haifile)

            height = hai.shape[0]
            width = hai.shape[1]
            
            e_list = [s_list[0]+height, s_list[1]+width]
            bg[int(s_list[0]) : int(e_list[0]), int(s_list[1]) : int(e_list[1])] = hai

            details.append([hainame, s_list, e_list])
            
            s_list = [e_list[0]-height-width*math.tan(math.radians(angle)), e_list[1]]
        
        cv2.imwrite(args['testset']+ 'mahjan' + str(num) + '.jpg', bg)
        # cv2.imshow('image', bg)
        # cv2.waitKey(0)
        self.details = details

    def change_brightness(self, img):
        view = random.uniform(0.6, 1)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        img_hsv[:, :, (1)] = img_hsv[:, :, (1)]*view
        img_hsv[:, :, (2)] = img_hsv[:, :, (2)]*view
        img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        return img_bgr

    def resize(self, img):
        height = img.shape[0]
        width = img.shape[1]
        seed = random.uniform(1.6, 2)
        img = cv2.resize(img, dsize=(int(width*seed), int(height*seed)))
        return img

    def flip(self, img):
        if random.randint(0, 8) == 0:
            img = cv2.flip(img, 0)
        return img

    def controlhai(self):
        args = self.args
        origin_list = self.origin_list

        for i in origin_list:
            img = cv2.imread(args['origin_hais'] + i)

            img = self.resize(img)
            img = self.flip(img)
            img = self.change_brightness(img)

            cv2.imwrite(args['rsize_hais'] + i, img)
    
    def addxml(self, num):
        details = self.details
        args = self.args
        tree = ET.parse(args['anotation_sample'])

        root = tree.getroot()
        for obj in root.iter('filename'):
            obj.text = 'mahjan' + str(num) + '.jpg'
        for i, object in enumerate(root.iter('object')):
            for name in object.iter('name'):
                name.text = details[i][0]
            for bndbox in object.iter('bndbox'):             
                for xmin in bndbox.iter('xmin'):
                    xmin.text = str(round(details[i][1][0]))
                for ymin in bndbox.iter('ymin'):
                    ymin.text = str(details[i][1][1])
                for xmax in bndbox.iter('xmax'):
                    xmax.text = str(round(details[i][2][0]))
                for ymax in bndbox.iter('ymax'):
                    ymax.text = str(details[i][2][1])

        tree.write(args['anotation_folder'] + 'mahjan' + str(num) + '.xml')
    
    def make_text(self):
        args = self.args
        f = open(args['trainval_text'], 'w')
        xmllist = os.listdir(args['anotation_folder'])
        for i in xmllist:
            f.write(re.sub('.xml', '', str(i)) + '\n')

##hais = {('1pin''3pin'):[[1,23,4,5],[2,3,45,6]]}
def main():
    work = MakeXML()
    for i in range(work.args['num_xml']):
        work.pastebackground(i)
        work.addxml(i)
    work.make_text()
    

if __name__ == "__main__":
    main()

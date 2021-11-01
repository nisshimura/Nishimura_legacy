import cv2 
import os 
import pathlib 
import time 

path = pathlib.Path('./make_hai/hai')
img_list = os.listdir(path)
for i in img_list:
    img = cv2.imread(str(path) + '/' + i)
    height = img.shape[0]
    width = img.shape[1]
    center = (int(width/2), int(height/2))
    #img = img[290 : 700, 630 : 1580] #ymin : ymax, xmin : xmax
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    img = cv2.resize(img, dsize=(width*2, height*2))
    print(img.shape[0], img.shape[1])
    cv2.imwrite('./make_hai/resizehai' + '/' + i, img)



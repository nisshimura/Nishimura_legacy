import dlib
import cv2
import sys
import glob
import os

if __name__ == "__main__":

    detector = dlib.simple_object_detector(
        './code_recongphoto/beer-detector/beer.svm')
    files = glob.glob('./code_recongphoto/beer-detector/images/detection/*.jpg')

    loop = 1
    for file in files:
        print('[Detecting]: '+ file)
        img = cv2.imread(file)
        rectangles = detector(img)

        for rect in rectangles:
            print('Found beer!')
            print(rect)
            print(rect.labele())
            x = rect.left()
            y = rect.top()
            w = rect.width()
            h = rect.height()
            cv2.imwrite('./code_recongphoto/beer-detector/result/' + 'lets-drink-'+ str(loop) +'.jpg', img[y:y+h, x:x+w])
            loop += 1

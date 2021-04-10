import dlib
import cv2
import sys
import glob
import os

if __name__ == "__main__":
    param = sys.argv
    detector = dlib.simple_object_detector('./code_recongphoto/mahjan-detecter/mahjan.svm')
    files = glob.glob('./code_recongphoto/mahjan-detecter/images/detection/*.jpg')

    loop = 1
    for file in files:
        print('[Detecting]: '+ file)
        img = cv2.imread(file)
        rectangles = detector(img)
        
        for rect in rectangles:
            print('Found mahjan!')
            print(rect);
            x = rect.left()
            y = rect.top()
            w = rect.width()
            h = rect.height()
                     
            cv2.rectangle(img, (rect.left(), rect.top()),(rect.right(), rect.bottom()), (147, 20, 255), 2)

            #cv2.imshow("image", img)          
            
            cv2.destroyAllWindows()
            
        
        cv2.imwrite('./code_recongphoto/mahjan-detecter/result/mahjan' +
                    str(loop) + '.jpg', img)  # , img[y:y+h, x:x+w]
        
        loop += 1
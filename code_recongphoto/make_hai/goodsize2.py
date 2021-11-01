from PIL import Image
import os 
import random
import cv2

origin_file = "code_mahjan/hai"
resizerotate_file = "code_mahjan/resizehai"
test_file = "code_mahjan/testset"

class Mahjan():
    def startcheckfile(self):
        if not os.path.exists(pathlib.Path(self.resizerotate_file)):
            os.mkdir(pathlib.Path(self.resizerotate_file))
        list_dir = os.listdir(str(pathlib.Path(self.resizerotate_file)))    
        self.list_dir = list_dir

    def openimg(self):
        for index in range(10):
            for i in self.listdir:
                img = Image.open(origin_file + '/' + str(i))

                ransu_over = random.randint(0,10)
                ransu_under = random.randint(0,10)

                ransu_ = random.randint(1,100)
                ransu2 = random.randint(1,100)
                
                img_resize_lanczos = img.resize((300 + ransu1, 300 + ransu2), Image.LANCZOS)
                img_resize_lanczos = img_resize_lanczos.rotate(ransu, expand=True)

                img_resize_lanczos.save(resizerotate_file + '/' + str(ransu1) + '_' + str(ransu2) + '_' + str(ransu) + '_' + str(i))

        resizerotate_listdir = os.listdir(resizerotate_file)

        for index in range(10):
            for i in resizerotate_listdir:
                sat_rand = random.uniform(0.7, 1)
                val_rand = random.uniform(0.7, 1)

                img = cv2.imread(resizerotate_file + '/' + str(i))
                
                img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)  # 色空間をBGRからHSVに変換
                s_magnification = sat_rand
                v_magnification = val_rand

                img_hsv[:,:,(1)] = img_hsv[:,:,(1)]*s_magnification  # 彩度の計算
                img_hsv[:,:,(2)] = img_hsv[:,:,(2)]*v_magnification  # 明度の計算
                img_bgr = cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)  # 色空間をHSVからBGRに変換

                cv2.imwrite(test_file + '/' + str(sat_rand + val_rand) + str(i),img_bgr)  # 画像の保存


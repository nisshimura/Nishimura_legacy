#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# conda install pillow
import os
import glob
from PIL import Image
import re
import shutil

def main(trainonly=True):
    filepath_list = glob.glob(input_path + '/*.png')  # .pngファイルをリストで取得する
    for index, filepath in enumerate(filepath_list):
        basename = os.path.basename(filepath)  # ファイルパスからファイル名を取得
        save_filepath = out_path + '/' + 'test' + str(index) + '.jpg'  # 保存ファイルパスを作成
        img = Image.open(filepath)
        img = img.convert('RGB')  # RGBA(png)→RGB(jpg)へ変換
        img.save(save_filepath, "JPEG", quality=95)
        print(filepath, '->', save_filepath)
        if flag_delete_original_files:
            os.remove(filepath)
            print('delete', filepath)
    
    make_text(trainonly=True)

def make_text(trainonly=True):
    f = open(text_path, 'w')
    xmllist = os.listdir(out_path)
    for index, i in enumerate(xmllist):
        f.write('test' + str(index) + '\n')
    if trainonly == False:
        g = open(trainval_path, 'w')
        xmllist_train = os.path.splitext(os.path.basename(train_path))[0]
        for index in xmllist_train:
            g.write(str(index) + '\n')

if __name__ == '__main__':
    input_path = './VOCdevkit/BCCD/PNGImages'  # オリジナルpngファイルがあるフォルダを指定
    out_path = './VOCdevkit/BCCD/JPEGImages/detect'  # 変換先のフォルダを指定
    train_path = './VOCdevkit/BCCD/JPEGImages/train'
    text_path = './VOCdevkit/BCCD/ImageSets/Main/test.txt'
    trainval_path = './VOCdevkit/BCCD/ImageSets/Main/trainval.txt'

    flag_delete_original_files = False  # 元ファイルを削除する場合は、True指定

    main(trainonly=True)

import keras
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os 
import re

temp_img = load_img('./code_recongphoto/mahjan-detecter/images/train/mahjan1.jpg', target_size=(64, 64))
temp_img_array = img_to_array(temp_img)

# フォルダの中にある画像を順次読み込む
# カテゴリーは0から始める

X = []
Y = []

def list_pictures(directory, ext='jpg|jpeg|bmp|png|ppm'):
    return [os.path.join(root, f)
            for root, _, files in os.walk(directory) for f in files
            if re.match(r'([\w]+\.(?:' + ext + '))', f.lower())]

# 対象Aの画像
for picture in list_pictures('./code_recongphoto/mahjan-detecter/images/train/'):
    img = img_to_array(load_img(picture, target_size=(64, 64)))
    X.append(img)

    Y.append(0)


# 対象Bの画像
for picture in list_pictures('./code_recongphoto/mahjan-detecter/images/detection/'):
    img = img_to_array(load_img(picture, target_size=(64, 64)))
    X.append(img)

    Y.append(1)


# arrayに変換
X = np.asarray(X)
Y = np.asarray(Y)

# 画素値を0から1の範囲に変換
X = X.astype('float32')
X = X / 255.0

# クラスの形式を変換
Y = np_utils.to_categorical(Y, 2)

# 学習用データとテストデータ
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.33, random_state=111)

model = Sequential()

model.add(Dense(34, input_dim=34, activation='sigmoid', padding='same'))
model.add(Dropout(0.5))
model.add(Dense(17, activation='sigmoid', padding='same'))
model.add(Dropout(0.5))
model.add(Dense(27, activation='sigmoid', padding='same'))
model.add(Dropout(0.5))
model.add(Dense(34, activation='softmax', padding='same'))

model.compile(optimizer='rmsprop', loss='categolical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=5, epochs=200, validation_data=(X_test, y_test), verbose=0)

# テストデータに適用
predict_classes = model.predict_classes(X_test)

# マージ。yのデータは元に戻す
mg_df = pd.DataFrame(
    {'predict': predict_classes, 'class': np.argmax(y_test, axis=1)})

# confusion matrix
pd.crosstab(mg_df['class'], mg_df['predict'])

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

# フォルダの中にある画像を順次読み込む
# カテゴリーは0から始める

X = []
Y = []

def list_pictures(directory, ext='jpg|jpeg|bmp|png|ppm'):
    return [os.path.join(root, f)
            for root, _, files in os.walk(directory) for f in files
            if re.match(r'([\w]+\.(?:' + ext + '))', f.lower())]

# ビール
for picture in list_pictures('./code_recongphoto/beer&coke-detecter/beer/'):
    img = img_to_array(load_img(picture, target_size=(64, 64)))
    X.append(img)

    Y.append(0)

# コーラ
for picture in list_pictures('./code_recongphoto/beer&coke-detecter/coke/'):
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


############################

model = Sequential()

model.add(Dense(2, input_dim=2, activation='softmax', input_shape=X_train.shape[1:]))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))  
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))  #relu, sigmoid

model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])       #categorical_crossentropy, binary_crossentropy

history = model.fit(X_train, y_train, batch_size=5, epochs=20, validation_data=(X_test, y_test), verbose=1)

############################

model = Sequential()
model.add(Conv2D(28,(3,3)), padding='same', input_shape=(64, 64, 3), activation='relu') #(3,3)はフィルター　(64*64, 3(カラー)1(グレースケール))
model.

# # テストデータに適用
# predict_classes = model.predict_classes(X_test)

# # マージ。yのデータは元に戻す
# mg_df = pd.DataFrame(
#     {'predict': predict_classes, 'class': np.argmax(y_test, axis=1)})

# # confusion matrix
# pd.crosstab(mg_df['class'], mg_df['predict'])



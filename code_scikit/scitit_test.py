
from sklearn import datasets

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, recall_score, precision_score

from sklearn.pipeline import Pipeline
from sklearn.model_selection import learning_curve, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier, RandomForestRegressor

# データの読み込み
iris = datasets.load_iris()

x, y = iris.data,iris.target

# トレーニングデータとテストデータに分ける
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2)

# モデルの選択
#教師あり
model = LogisticRegression()
# model = SVC()
# model = KNeighborsClassifier(n_neighbors=3)
# model = RandomForestRegressor()
# model = GradientBoostingClassifier()


#学習
model.fit(x_train, y_train)

train_size_abs, train_accuracy, test_accuracy = learning_curve(
    model, x_train, y_train, train_sizes=np.linspace(0.1, 1, 10), random_state=1, shuffle=True)

#学習正解曲線

train_accuracy_mean = np.mean(train_accuracy, axis=1)
train_accuracy_std = np.std(train_accuracy, axis=1)
test_accuracy_mean = np.mean(test_accuracy, axis=1)
test_accuracy_std = np.std(test_accuracy, axis=1)

plt.figure()
plt.title("Learning Curve")
plt.xlabel("Training examples")
plt.ylabel("Accuracy")

# Traing score と Test score をプロット
plt.plot(train_size_abs, train_accuracy_mean, 'o-',
         color="r", label="Training score")
plt.plot(train_size_abs, test_accuracy_mean, 'o-', color="g", label="Test score")

# 標準偏差の範囲を色付け
plt.fill_between(train_size_abs, train_accuracy_mean - train_accuracy_std,
                 train_accuracy_mean + train_accuracy_std, color="r", alpha=0.2)
plt.fill_between(train_size_abs, test_accuracy_mean - test_accuracy_std,
                 test_accuracy_mean + test_accuracy_std, color="g", alpha=0.2)

plt.ylim(0.85, 1.0)
plt.legend(loc="best")
plt.show()

# 評価
y_pred = model.predict(x_test)

#混同行列
cmatrix = confusion_matrix(y_test,y_pred)
df = pd.DataFrame(cmatrix, columns=[["predict", "", ""], [0, 1, 2]], index=[
                  ["actual", "", ""], [0, 1, 2]])
print(df)

#正解率　TP＋TN/ALL
print('Accuracy:', accuracy_score(y_test, y_pred))

#適合率　精度 TP/TP+FP
print('Precision:', precision_score(y_test, y_pred,average='micro'))

#再現率　取りこぼし TP/TP+FN
print('Recall:', recall_score(y_test, y_pred,average="micro"))

#F値 2(適合率*再現率)/(適合率+再現率))
print('F1 score:', f1_score(y_test, y_pred, average="micro"))  # 0.67
# 学習済みモデルを使う
# print(model.predict([[1.4, 3.5, 5.1, 0.2], [6.5, 2.6, 4.4, 1.4], [5.9, 3.0, 5.2, 1.5]])





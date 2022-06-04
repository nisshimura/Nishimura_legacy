
from tkinter import N
from sklearn import datasets
from sklearn.model_selection import learning_curve, train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd
# データの読み込み
iris = datasets.load_iris()

x, y = iris.data,iris.target

print(f"x{len(x)}")
print(f"x{list(map(list,set(map(tuple,x))))}")
# トレーニングデータとテストデータに分ける
#x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2)

#print(len(x_train),len(y_train))
# モデルの選択
model = LogisticRegression()
#model = svm.SVC()
train_sizes = np.arange(5, 120, 5)
model.fit(x, y)

train_size_abs, train_scores, test_scores = learning_curve(
     model, x, y, train_sizes=train_sizes, shuffle=True)

print(f"train_size_abs\n{train_size_abs}\ntrain_scores\n{train_scores}\ntest_scores\n{test_scores}")
# 学習

#学習曲線





train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.figure()
plt.title("Learning Curve")
plt.xlabel("Training examples")
plt.ylabel("Score")

# Traing score と Test score をプロット
plt.plot(train_sizes, train_scores_mean, 'o-',
         color="r", label="Training score")
plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Test score")

# 標準偏差の範囲を色付け
# plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
#                  train_scores_mean + train_scores_std, color="r", alpha=0.2)
# plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
#                  test_scores_mean + test_scores_std, color="g", alpha=0.2)

plt.ylim(0.85, 1.0)
plt.legend(loc="best")

plt.show()


# 評価
pred = model.predict(x_test)
print(accuracy_score(y_test, pred))

# 学習済みモデルを使う
print(model.predict([[1.4, 3.5, 5.1, 0.2]]))

# 次のように、複数渡すことも可能です。
# print(model.predict([[1.4, 3.5, 5.1, 0.2], [6.5, 2.6, 4.4, 1.4], [5.9, 3.0, 5.2, 1.5]])





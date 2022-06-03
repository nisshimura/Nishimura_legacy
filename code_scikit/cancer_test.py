import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression

from sklearn import datasets
from sklearn.model_selection import learning_curve, train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

import pandas as pd
cancer = load_breast_cancer()
X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
y = cancer.target

estimator = LogisticRegression()

# 50から350まで50刻みで検証する
train_sizes = np.arange(50, 351, 50)

# cvにintを渡すと k-foldの「k」を指定できる
# ↓では3にしているので、3-fold法を使用する。
train_sizes, train_scores, test_scores = learning_curve(
    estimator, X, y, cv=3, train_sizes=train_sizes, random_state=42, shuffle=True
)

print("train_sizes(検証したサンプル数): {}".format(train_sizes))
print("------------")
print("train_scores(各サンプル数でのトレーニングスコア): \n{}".format(train_scores))
print("------------")
print("test_scores(各サンプル数でのバリデーションスコア): \n{}".format(test_scores))


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
plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, color="r", alpha=0.2)
plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, color="g", alpha=0.2)

plt.ylim(0.85, 1.0)
plt.legend(loc="best")

plt.show()

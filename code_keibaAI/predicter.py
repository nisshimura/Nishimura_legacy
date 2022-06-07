from matplotlib.pyplot import axis
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


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

results = pd.read_pickle("./data/Pickel/2019_orthoped.pickle")

def preprocess(results):
    df = results.copy()
    df["rank"]=df["着順"].map(lambda x:x if x<4 else 4)
    df.drop(["着順","馬名"],axis=1,inplace=True)
    df_d = pd.get_dummies(df)
    print(df_d)
    return df_d


def make_model(results):
    df = results.copy()
    X = df.drop(["rank"],axis=1)
    y = df["rank"]
    x_train, x_test, y_train, y_test = train_test_split(X, y, stratify=y,test_size=0.3,random_state=2)
    model = LogisticRegression()

    #学習
    model.fit(x_train, y_train)

    train_size_abs, train_accuracy, test_accuracy = learning_curve(
        model, x_train, y_train, train_sizes=np.linspace(0.1, 1, 1000), random_state=1, shuffle=True)

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
    plt.plot(train_size_abs, test_accuracy_mean,
            'o-', color="g", label="Test score")

    # 標準偏差の範囲を色付け
    # plt.fill_between(train_size_abs, train_accuracy_mean - train_accuracy_std,
    #                 train_accuracy_mean + train_accuracy_std, color="r", alpha=0.2)
    # plt.fill_between(train_size_abs, test_accuracy_mean - test_accuracy_std,
    #                 test_accuracy_mean + test_accuracy_std, color="g", alpha=0.2)

    plt.ylim(0.85, 1.0)
    plt.legend(loc="best")
    plt.show()

    # # 評価
    # y_pred = model.predict(x_test)

    # #混同行列
    # cmatrix = confusion_matrix(y_test, y_pred)
    # df = pd.DataFrame(cmatrix, columns=[["predict", "", ""], [0, 1, 2]], index=[
    #                 ["actual", "", ""], [0, 1, 2]])
    # print(df)

    # #正解率　TP＋TN/ALL
    # print('Accuracy:', accuracy_score(y_test, y_pred))

    # #適合率　精度 TP/TP+FP
    # print('Precision:', precision_score(y_test, y_pred, average='micro'))

    # #再現率　取りこぼし TP/TP+FN
    # print('Recall:', recall_score(y_test, y_pred, average="micro"))

    # #F値 2(適合率*再現率)/(適合率+再現率))
    # print('F1 score:', f1_score(y_test, y_pred, average="micro"))



df_d = preprocess(results)
make_model(df_d)


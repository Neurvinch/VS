from sklearn import datasets

from sklearn.model_selection import train_test_split

from sklearn.svm import SVC, SVR

from sklearn.metrics import accuracy_score, mean_squared_error , classification_report


iris = datasets.load_iris()

X_cls = iris.data

y_cls = iris.target

X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(X_cls, y_cls, test_size=0.3, random_state=42)

svm_classifier = SVC(kernel=    'linear')

svm_classifier.fit(X_train_cls, y_train_cls)

y_pred_cls = svm_classifier.predict(X_test_cls)

accuracy = accuracy_score(y_test_cls, y_pred_cls)

print("SVM Classifier Accuracy:", accuracy)


import numpy as np

from sklearn.datasets import make_regression

x_reg ,y_reg = make_regression(n_smaples = 100 , n_features= 1, noise= 15)

X_train_cls, X_test_reg, y_train_reg, y_test_reg = train_test_split(x_reg, y_reg, test_size=0.3, random_state=42)

svm_regressor = SVR(kernel='rbf')

svm_regressor.fit(X_train_cls, y_train_reg)

y_pred_reg = svm_regressor.predict(X_test_reg)

mse = mean_squared_error(y_test_reg, y_pred_reg)


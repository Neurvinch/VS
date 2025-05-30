import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler , LabelBinarizer

from tensorflow.keras.model import Sequential

from tensorflow.keras.layers import Dense


iris = load_iris()

X= iris.data
y = iris.target


encoder = LabelBinarizer()

y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

x_test = scaler.transform(X_test)

model = Sequential()

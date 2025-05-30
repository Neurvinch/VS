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

model.add(Dense(16,activation = "relu"))
model.add(Dense(12,activation = "relu"))
model.add(Dense(3,activation = "softmax"))


model.compile(optimizer = 'adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])
              
model.fit(X_train, y_train, epochs=100, batch_size=5, verbose=1)

loss , accuracy = model.evaluate(X_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")
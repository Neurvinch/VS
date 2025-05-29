import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score

x = np.array([[1], [2], [3], [4], [5]])

y = np.array([1, 2, 3, 4, 5])


model = LinearRegression()

model.fit(x, y)

y_pred = model.predict(x)

model.conef_[0]
model.intercept_
mean_squared_error(y, y_pred)
r2_score(y,y_pred)


plt.scatter(x, y , color='blue', label='Data Points')
plt.plot(x, y_pred, color= 'red', label='Regression Line')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression Example')

plt.legend()

plt.show()
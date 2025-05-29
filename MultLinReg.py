import numpy as np

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error, r2_score


x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])

y = np.array([1, 2, 3, 4, 5])

model = LinearRegression()

model.fit(x, y)

y_pred= model.predict(x)

model.intercept_

model.coef_

mean_absolute_error(y, y_pred)
r2_score(y, y_pred)
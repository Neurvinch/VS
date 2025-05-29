from sklearn.datasets import load_iris

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier


iris = load_iris()
X = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


dt_model = DecisionTreeClassifier()

dt_model.fit(x_train, y_train)

dt_pred = dt_model.predict(x_test)


rf_model = RandomForestClassifier()

rf_model.fit(x_train, y_train)

rf_pred = rf_model.predict(x_test)
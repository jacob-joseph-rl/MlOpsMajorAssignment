from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

data = fetch_olivetti_faces()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print(f"Accuracy: {round(model.score(X_test, y_test), 2)}")
joblib.dump((X_test, y_test), 'test_data.joblib')
print('Test data saved')
joblib.dump(model, 'savedmodel.pth')
print('Model Saved')
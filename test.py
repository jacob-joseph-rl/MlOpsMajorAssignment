import joblib

model = joblib.load('model.joblib')
X_test, y_test = joblib.load('test_data.joblib')
prediction = model.predict(X_test)
score = model.score(X_test, y_test)
print(f"Model Accuracy on test data: {round(score, 2)}")
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib  # For saving models
from preprocess import loadData

"""
We fist extract our training and testing data sets for features and targets (X/Y)
we are then inializing a random forset classifier and training it on X Y training set,
and then we are testing it on the X test set. The same then happens for XGboost model
"""
# load loadData
X_train, X_test, y_train, y_test = loadData()

# Train / predict random forest
randomForestModel = RandomForestClassifier(random_state=42)
randomForestModel.fit(X_train, y_train)
randomForestPredictions = randomForestModel.predict(X_test)

print("Random Forest Results")
print(classification_report(y_test, randomForestPredictions)) # includes precision, recall, and F1-score
print(f"Random Forest Accuracy: {accuracy_score(y_test, randomForestPredictions)}") # overall accuracy of the model

# Train / predict xg boost 
xgbModel = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
xgbModel.fit(X_train, y_train)
xgbPredictions = xgbModel.predict(X_test)

print("XGBoost Results")
print(classification_report(y_test, xgbPredictions)) # includes precision, recall, and F1-score
print(f"XGBoost Accuracy: {accuracy_score(y_test, xgbPredictions)}") # overall accuracy of the model

# Save Models
joblib.dump(randomForestModel, 'model/randomforestmodel.pkl')
joblib.dump(xgbModel, 'model/xgboostmodel.pkl')

# # # # # # # # # # # # # # # # # # # # #
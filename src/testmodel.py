from collections import Counter
import joblib
import pandas as pd

# Load saved models
model = joblib.load('model/randomforestmodel.pkl')

# Load data set
data = pd.read_csv('data/CreditCardFraud.csv')

# Features only
X_sample = data.drop('Class', axis=1)

# Make predictions
# 0 for genuine 1 for fradulent
predictions = model.predict(X_sample)
print("Predictions:", predictions)
print("Prediction Class Distribution:", Counter(predictions)) 
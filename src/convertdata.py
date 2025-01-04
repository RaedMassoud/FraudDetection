from scipy.io import arff
import pandas as pd

# converting / loading the data set
"""
We are using arff.loadarff() function from scipy to lead the data from the
European Credit Card Fraud Dataset (Citation and more info in README file). We're using this
format because our data has meta data too. We are then saving our digest to
a CSV file under data/
"""
data, meta = arff.loadarff('data/EuropeanCreditCardFraudDataset.arff')
dataFrame = pd.DataFrame(data)

# Save to cvs file 
dataFrame.to_csv('data/CreditCardFraud.csv', index=False)

# # # # # # # # # # # # # # # # # # # # #
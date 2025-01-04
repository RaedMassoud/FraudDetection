import pandas as pd
from sklearn.model_selection import train_test_split

# Clean and Prepare Data for Model Training 
"""
We read the csv file we just created using convertdata that has the cleaned data
we then use X Y Train X Y Test which are the features and target variables split 
into training and testing data sets.
"""
# Load
def loadData():
    # read CVS file
    dataFrame = pd.read_csv('data/CreditCardFraud.csv')

    # check missing values
    """
    The isnull() funtion creates a boolen value for missing values (T/F).
    The first sum adds those values for 1 column and then the second sum 
    adds the values accross all columns
    """
    print("Missing Values: ", dataFrame.isnull().sum().sum()) 

    # Strip Class from unwanted characters ("b'") and convert value to int
    dataFrame['Class'] = dataFrame['Class'].apply(lambda x: int(x.strip("b'")))
    print(dataFrame['Class'].head()) # print sample to cofirm convertion

    # Split features and target
    # we are droping the Class for the features and setting it as targert in y
    # axis=1 means to drop across all columns
    X = dataFrame.drop('Class', axis=1)
    y = dataFrame['Class']

    # Check if X and y still have rows
    ## This is just so that we make sure we have data to work with
    print(f"Number of rows in X: {X.shape[0]}")
    print(f"Number of rows in y: {y.shape[0]}")

    # X / Y Train - X / Y Test
    """
    The .2 indicates that we are splitting our data set into 
    80% training data and 20% test data
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    loadData()

# # # # # # # # # # # # # # # # # # # # #
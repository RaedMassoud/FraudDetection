## Fraud Detection in Financial Transaction  

## Overview
This project focuses on detecting fraudulent credit card transactions using machine learning techniques. The project using the European cardholders in September 2013. The primary objective is to classify transactions as `genuine` or `fraudulent`.

<br><br>
## Dataset
- **Features**: 28 anonymized numerical features (`V1` to `V28`), `Time`, and `Amount`.
- **Target**: `Class` (0 = genuine, 1 = fraudulent)

The dataset is highly imbalanced with fraudulent transactions constituting only 0.17% of the total transactions. [more info bellow](#dataset-details-and-citation)

<br><br>
## Dependencies ⚠️
- Python 3.10.6
- pandas
- scikit-learn
- xgboost
- joblib
- tqdm
- requests

⚠️⚠️⚠️ * * * * ⚠️⚠️⚠️ * * * * ⚠️⚠️⚠️ * * * * ⚠️⚠️⚠️   
Locate the `requirements.py` and run it first  
This will download all requirements AND the dataset  
You can also download the dataset independently from [`bellow`](#dataset-details-and-citation)

<br><br>
## Future Work
* Implement additional anomaly detection techniques
* Experiment with oversampling and undersampling methods
* Real-Time Fraud Detection Integration
Deploy the trained models in real-time systems to monitor and flag fraudulent transactions as they occur. For instance we can sugest integrating the model with banks such as BLOM Bank, Bank of Beirut, or BBAC in which the model could provide valuable support to their existing independent systems such as:

    * Anti-Financial Crime (AFC) systems, including:
        * Anti-Money Laundering (AML)
        * Countering the Financing of Terrorism (CFT)
        * Anti-Fraud
        * Anti-Bribery and Anti-Corruption
        * Tax Evasion Monitoring


* Enhancing Existing Fraud Detection Platforms
Collaborate with systems like the `Visa Risk Management` (VRM) platform used by the Bank of Beirut. The trained models could complement VRM by improving its ability to predict high-risk transactions and flagging them for further review when fraud probabilities exceed acceptable thresholds.

<br><br>
# Dataset details and citation  
`Author`: Andrea Dal Pozzolo, Olivier Caelen and Gianluca Bontempi  
`Source`: Credit card fraud detection - Date 25th of June 2015  
`Links`: https://www.openml.org - https://www.openml.org/d/1597  
`Direct Download`: https://www.openml.org/data/download/1673544/phpKo8OWT  
Please cite: Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. Calibrating Probability with Undersampling for Unbalanced Classification. In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015  

The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset present transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.  

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.  

The dataset has been collected and analysed during a research collaboration of Worldline and the Machine Learning Group (mlg.ulb.ac.be) of ULB (Université Libre de Bruxelles) on big data mining and fraud detection. More details on current and past projects on related topics are available on http://mlg.ulb.ac.be/BruFence and http://mlg.ulb.ac.be/ARTML.


<br><br>
# Project Details and References
Created on: `1/4/2025`  
Author: `Raed Massoud`  
Found on: `https://github.com/RaedMassoud`  
References:
- Intro to pd: https://madewithml.com/courses/foundations/pandas/  
- Arff to CSV: https://stackoverflow.com/questions/55653131/converting-arff-file-to-csv-using-python  
- RFD using scikit: https://www.geeksforgeeks.org/random-forest-classifier-using-scikit-learn/  
- XGBoost: https://xgboost.readthedocs.io/en/stable/python/python_intro.html  
- Joblib to save ML models: https://www.geeksforgeeks.org/saving-a-machine-learning-model/  
- Subprocess: https://www.geeksforgeeks.org/python-subprocess-module/  
- Progress with tqdm: https://www.geeksforgeeks.org/python-how-to-make-a-terminal-progress-bar-using-tqdm/
## Fraud Detection in Financial Transaction


## Overview
This project focuses on detecting fraudulent credit card transactions using machine learning techniques. The project using the European cardholders in September 2013. The primary objective is to classify transactions as `genuine` or `fraudulent`.

<br><br> 
## Dataset
- **Features**: 28 anonymized numerical features (`V1` to `V28`), `Time`, and `Amount`.
- **Target**: `Class` (0 = genuine, 1 = fraudulent)

The dataset is highly imbalanced with fraudulent transactions constituting only 0.17% of the total transactions. [more info bellow](#Dataset-details-and-citation)

<br><br> 
## Dependencies
- Python 3.10.6
- pandas
- numpy
- scikit-learn
- xgboost
- joblib

Install all dependencies using:
pip install -r requirements.txt

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
Please cite: Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. Calibrating Probability with Undersampling for Unbalanced Classification. In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015  

The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset present transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.  

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.  

The dataset has been collected and analysed during a research collaboration of Worldline and the Machine Learning Group (mlg.ulb.ac.be) of ULB (Université Libre de Bruxelles) on big data mining and fraud detection. More details on current and past projects on related topics are available on http://mlg.ulb.ac.be/BruFence and http://mlg.ulb.ac.be/ARTML.
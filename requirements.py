import subprocess
import sys
import os


def installRequirements():
     requiredPackages = [
        'requests',        # downloading datasets
        'tqdm',            # progress bar
        'scikit-learn',    # RandomForestClassifier, etc.
        'xgboost',         # XGBClassifier
        'joblib',          # saving models
        'pandas',          # data manipulation
        'numpy',           # data manipulation
        'scipy'            # reading .arff files
     ]

     for package in requiredPackages:
          try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
          except subprocess.CalledProcessError:
            print(f"Failed to install {package}, please install manually.")
    
     print(f"\n\n############### ALL REQUIREMENTS INSTALLED ###############")
     print(f"pandas, scipy, xgboost, scikit-learn, joblib, tqdm, requests\n")
     print(f"###################")
     

# Try importing
try:
    import requests
    from tqdm import tqdm
except ImportError:
    print("Required libraries not found. Installing them now...")
    installRequirements()  # Install missing libraries
    import requests  # Re import after installation
    from tqdm import tqdm  

# Downlaod dataset into data/
def downloadDataSet():
    url = 'https://www.openml.org/data/download/1673544/phpKo8OWT'
    destination = 'data/EuropeanCreditcardFraudDataset.arff'

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # error check 

        # get size
        size = int(response.headers.get('content-lenght', 0))
        # start download / progress bar
        with open(destination, 'wb') as file, tqdm(
            total = size, unit='B', unit_scale=True, desc='Downloading dataset') as bar:
                # Download file in chunks
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        bar.update(len(chunk)) # update length

        print(f"Data set downloaded successfully to {destination}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading dataset: {e}")

if __name__ == "__main__":
    installRequirements()
    downloadDataSet()

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

#Removes warnings and imporves asthenics
import warnings
warnings.filterwarnings("ignore")

from env import get_connection

"""
This is how you get rid of the Unnamed: 0 column:

#read_csv(filename, index_col=0)
#to_csv(filename, index=False)
"""


def wrangle_zillow():
    """
    This function reads the telco_churn data from Codeup db into a df.
    Changes the names to be more readable.
    Drops null values.
    """
    filename = "zillow_2017.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        
        # read the SQL query into a dataframe
        query = """
        SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet,
        taxvaluedollarcnt, yearbuilt, taxamount, fips
        FROM properties_2017
        LEFT JOIN propertylandusetype USING (propertylandusetypeid)
        WHERE  propertylandusedesc LIKE 'Single Family Residential';
        """
        df = pd.read_sql(query, get_connection('zillow'))
        
        # Remove NAs. No significant change to data. tax_values upper outliers were affected the most.
        df = df.dropna()
        df.rename(columns = {'bedroomcnt': 'bedrooms', 'bathroomcnt': 'bathrooms',
                             'calculatedfinishedsquarefeet': 'sqft', 'taxvaluedollarcnt':'tax_value',
                             'yearbuilt':'year_built', 'taxamount':'tax_amount'}, inplace=True)
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)
        
        # Return the dataframe to the calling code
        return df

def train_validate(df, stratify_col = None, random_seed=1969):
    """
    This function takes in a DataFrame and column name for the stratify argument (defualt is None).
    It will split the data into three parts for training, testing and validating.
    Note: DO NOT specify the target(stratify) column for continuous data. It will error.
    """
    #This is logic to set the stratify argument:
    stratify_arg = ''
    if stratify_col != None:
        stratify_arg = df[stratify_col]
    else:
        stratify_arg = None
    
    #This splits the DataFrame into 'train' and 'test':
    train, test = train_test_split(df, train_size=.7, stratify=stratify_arg, random_state = random_seed)
    
    #The length of the stratify column changed and needs to be adjusted:
    if stratify_col != None:
        stratify_arg = train[stratify_col]
        
    #This splits the larger 'train' DataFrame into a smaller 'train' and 'validate' DataFrames:
    train, validate = train_test_split(train, test_size=.2, stratify=stratify_arg, random_state = random_seed)
    return train, validate, test
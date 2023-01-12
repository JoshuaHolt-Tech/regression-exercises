import os
import pandas as pd
import numpy as np
from env import get_connection

"""
This is how you get rid of the Unnamed: 0 column:

#read_csv(filename, index_col=0)
#to_csv(filename, index=False)
"""


def wrangle_zillow():
    """
    This function reads the telco_churn data from Codeup db into a df.
    """
    filename = "zillow_2017.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        
        # read the SQL query into a dataframe
        query = """
        SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
        FROM properties_2017
        LEFT JOIN propertylandusetype USING (propertylandusetypeid)
        WHERE  propertylandusedesc LIKE 'Single Family Residential';
        """
        df = pd.read_sql(query, get_connection('zillow'))
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)

        # Remove NAs. No significant change to data. Upper outliers were affected the most.
        df = df.dropna()
        
        # Return the dataframe to the calling code
        return df


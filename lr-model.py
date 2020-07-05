import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import tabpy_client 

# Connect to TabPy server using the client library
connection = tabpy_client.Client('http://localhost:9004/')

# load the model from disk
def tableau_classifier(arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9):
    inputs_df = pd.DataFrame(
        {
            'Perf-Low': arg2,
            'Perf-Mid': arg3,
            'Perf-Mid-High': arg4,
            'Perf-Undet': arg5,
            'Ven-Low': arg6,
            'Ven-Mid': arg7,
            'Ven-Mid-High': arg8,
            'Ven-Undet': arg9
        }
    )

    loaded_model = pickle.load(open('/Users/arturoroman/Desktop/Udemy/lr_model.sav', 'rb'))
    return loaded_model.predict(inputs_df).tolist()

# Publish the tableau_classifier function to TabPy server so it can be used from Tableau
# Using the name DiagnosticsDemo and a short description of what it does
connection.deploy('EventCalssifier',
                  tableau_classifier,
                  'Return a classification for the events in profitable and not profitable given 9 Tableau Columns'
                  ,override=True)

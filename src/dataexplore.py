# Method to Explore the Main Libraries 

def main_libraries():
    import pandas as pd
    import numpy as np
    import warnings
    import re
    import matplotlib.pyplot as plt 
    import matplotlib
    import seaborn as sns




# Prints relevant info about specified columns 
def col_explore(dfcol):
    print(
    f'No of rows: {len(dfcol)} \n', 
    f'Column Type: {dfcol.dtype} \n',
    f'No of Unique: {dfcol.nunique()} \n', 
    f'Unique/Total ratio: {round(dfcol.nunique()/len(dfcol)*100, 2)} \n',
    f'Unique Values: {dfcol.unique()} \n',
    f'Sum of NaNs: {dfcol.isnull().sum()} \n', 
    f'% of NaNs: {round((dfcol.isnull().sum() / len(dfcol))*100, 2)} \n',
    f'Values counts / total sum of values: \n {round((dfcol.value_counts()/dfcol.value_counts().sum())*100, 2)} \n',
    ) 


# Compare Columns for further exploration.
# HOW TO USE: col_compare(dfName,["colName1","colName2","colName3"])
def col_compare(df, columns):
    
    # 1. COMPARE THE LENGTH OF SPECIFIED COLUMNS:
    col_lenghts = []
    for cells in columns:
        pass
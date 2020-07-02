import pandas as pd
import numpy as np

def extract_numeric(df):
    return df.select_dtypes(include=np.number)

def extract_non_numeric(df):
    return df.select_dtypes(exclude=np.number)
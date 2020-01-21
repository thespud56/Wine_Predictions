#  Import statements
import pandas as pd
import numpy as np
import missingno
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from IPython.display import display_html


def clean_df(raw_df):
    '''Function that removes duplicate wines, unwanted columns, naans, and wines above $100'''
    nodup_df = raw_df.drop_duplicates(subset='title', keep='first')
    nodup_df = nodup_df.drop(['region_1', 'region_2'], axis=1)
    nodup_df = nodup_df.dropna()
    df = nodup_df[nodup_df['price'] >= 300].index
    nodup_df = nodup_df.drop(df, inplace=True)
    return nodup_df



    


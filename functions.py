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
    nodup_df = raw_df.duplicated(subset='title', keep=False)
    nodup_df = raw_df[nodup_df].drop(['Unnamed: 0'], axis=1)
    nodup_df = nodup_df.dropna()
    return nodup_df



    


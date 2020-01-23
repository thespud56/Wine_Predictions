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
    nodup_df = raw_df.duplicated(subset='title', keep='first')
    nodup_df = raw_df[nodup_df].drop(['Unnamed: 0', 'designation', 'region_1', 'region_2'], axis=1)
    nodup_df = nodup_df.dropna()
    df = nodup_df[nodup_df['price'] >= 100 ].index
    nodup_df.drop(df, inplace=True)
    return nodup_df


def welch_ttest(x, y): 
    '''dof returns Degrees of Freedom, t, p return Welchs t-test and p-value respectivly'''
    dof = (x.var()/x.size + y.var()/y.size)**2 / ((x.var()/x.size)**2 / (x.size-1) + (y.var()/y.size)**2 / (y.size-1))
   
    t, p = stats.ttest_ind(x, y, equal_var = False)
    
    print("\n",
          f"Welch's t-test= {t:.4f}", "\n",
          f"p-value = {p:.4f}", "\n",
          f"Welch-Satterthwaite Degrees of Freedom = {dof:.4f}")    
    

def hyp2_plot(df, file_name):
    '''Display joinplot and saves image to file.'''
    g = sns.jointplot(x="points", y="price", data=df, kind="kde", color="m")
    g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
    g.ax_joint.collections[0].set_alpha(0)
    g.set_axis_labels("$Points$", "$Price$")
    plt.savefig(file_name, transparent=True, dpi=150, bbox_inches='tight')
    

    
    
    
    
    
    
    
    
#   def display_side_by_side(*args):
#     html_str=''
#     for df in args:
#         html_str+=df.to_html()
#     display_html(html_str.replace('table','table style="display:inline"'),raw=True)
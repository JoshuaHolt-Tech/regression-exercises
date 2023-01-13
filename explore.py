#Importing required packages and files
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns






#Make a function to print 
def cat_and_cont(df, target, cat_columns, quant_y_lim=0.85, sample_size=500):
    """
    This function takes in a DataFrame, 
    target column and list of categorical columns to plot.
    """
    for col in cat_columns:

        sns.swarmplot(x=col, y=target, data=df.sample(sample_size))
        plt.ylim(top=(df[target].quantile(q=quant_y_lim)), bottom=0)
        plt.show()
        
        sns.stripplot(x=col, y=target, data=df.sample(sample_size))
        plt.ylim(top=(df[target].quantile(q=quant_y_lim)), bottom=0)
        plt.show()

        
def lmplot_cont(df, target, cont_columns, sample_size=500):
    """
    Plots continuous versus continuous variable with regression line.
    """
    for col in cont_columns:
        sns.lmplot(x=col, y=target, data=df.sample(sample_size),
                   robust=True, scatter_kws = {'color':'tomato'},
                   line_kws = {'color':'blue'})
        #plt.xlim(left=0,right=5000)
        #plt.ylim(bottom=0, top=150000)
        
def finished_q3():
    print("Real Question 3 complete. (Question 5 on the Codeup site.)")
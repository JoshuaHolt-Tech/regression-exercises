#Importing required packages and files
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns



#Make a function to print 
def swarm_cat(df, target, cat_columns, quant_y_lim=0.85, sample_size=500):
    """
    This function takes in a DataFrame, 
    target column and list of categorical columns to plot.
    """

    for col in cat_columns:

        sns.swarmplot(x=col, y=target,
                      data=df.sample(sample_size))
        plt.title(f'Comparing {col} to {target} columns with a swarm plot')
        plt.show()

        
def strip_cat(df, target, cat_columns, quant_y_lim=0.90, sample_size=500):
    """
    This function takes in a DataFrame, 
    target column and list of categorical columns to plot.
    """
    
    for col in cat_columns:
    
        
        sns.stripplot(x=col, y=target,
                      data=df.sample(sample_size))
        plt.title(f'Comparing {col} to {target} columns with a strip plot')
        plt.show()

        
def lmplot_cont(df, target, cont_columns, sample_size=500):
    """
    Plots continuous versus continuous variable with regression line.
    """
  
    for col in cont_columns:
        sns.lmplot(x=col,
                   y=target, 
                   data=df.sample(sample_size), 
                   robust=True, scatter_kws = {'color':'gray'}, 
                   line_kws = {'color':'blue'}, 
                   markers = '.')
        plt.hlines(y=df[target].quantile(q=.25), 
                   color='red', alpha=0.6, xmin=min(df[col]),
                  xmax=len(df[col]), label='25%')
        plt.hlines(y=df[target].quantile(q=.5),
                   color='orange', alpha=0.6, xmin=min(df[col]),
                  xmax=len(df[col]), label='50%')
        plt.hlines(y=df[target].quantile(q=.75),
                   color='green', alpha=0.6, xmin=min(df[col]),
                  xmax=len(df[col]), label='75%')
        plt.xlim(left=df[col].quantile(q=0.05), 
                 right=df[col].quantile(q=0.85))
        plt.ylim(bottom = 0, top=df[target].quantile(q=0.85))
        
def finished_q3():
    print("Real Question 3 complete. (Question 5 on the Codeup site.)")
    
def strip_swarm(df, target, cont_columns, cat_columns, quant_y_lim=0.90, sample_size=500):

    
    lmplot_cont(df, target, cont_columns,
                sample_size=sample_size)
    
    #These are all screwed up. Unsure why
    swarm_cat(df, target, cat_columns,
              quant_y_lim=quant_y_lim,
              sample_size=sample_size)
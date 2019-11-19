# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:51:30 2019

@author: pc
"""

import pandas as pd 

df_red = pd.read_csv('winequality-red.csv',sep=';')
df_white = pd.read_csv('winequality-white.csv',sep=';')

# number of sipmples in each dataset
df_red.shape
df_white.shape

df_red.info()
df_white.info()

import sklearn
from sklearn import model_selection, linear_model
import pandas as pd
import os

#for visualizing
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

#Load the data from 'data/housing.csv' into a pandas frame called housing

#Print some info about the data set,you can delete this
#print(housing.head())
#print(housing.info())
#print(housing.describe())

#Start

# 1. use train_test_split to split the data
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html


# 2. Look for correlations using the standard correlation coefficient
# save these in a variable called 'corr_matrix'
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html
# https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/correlation-coefficient-r/v/correlation-coefficient-intuition-exampless

# 3. Compare these to the median house value

#print(corr_house_value)

# 4. Fix the total_bedrooms problem
    # Options: 
    # 1. remove data rows for which total_bedrooms is empty: housing.dropna(..)
    # 2. remove total_bedrooms attribute: housing.drop(..)
    # 3. Set the values to a certain value(zero, median, .. ): housing[..].fillna(median, inplace=True)


# 5. Use a Linear Regression model
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html


#6. Evaluate using Cross-Validation
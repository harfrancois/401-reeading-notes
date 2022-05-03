# Pandas
source = https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
import pandas as pd
Object creation

Creating a Series by passing a list of values, letting pandas create a default integer index
Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns
Creating a DataFrame by passing a dictionary of objects that can be converted into a series-like structure

DataFrame.to_numpy() gives a NumPy representation of the underlying data. Note that this can be an expensive operation
when your DataFrame has columns with different data types, which comes down to a fundamental difference between pandas
and NumPy: NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column. When
you call DataFrame.to_numpy(), pandas will find the NumPy dtype that can hold all of the dtypes in the DataFrame. This
may end up being object, which requires casting every value to a Python object.

isin() method for filtering

pandas primarily uses the value np.nan to represent missing data

Series is equipped with a set of string processing methods in the str attribute that make it easy to operate on each
element of the array, as in the code snippet below. Note that pattern-matching in str generally uses regular 
expressions by default

Concatenating pandas objects together with concat()
Grouping and then applying the sum() function to the resulting groups
The stack() method “compresses” a level in the DataFrame’s columns
unstack(), which by default unstacks the last level
The close() method is used to close a figure window
the plot() method is a convenience to plot all of the columns with labels

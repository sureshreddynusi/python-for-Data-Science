# -*- coding: utf-8 -*-
"""
@author: Suresh Reddy Nusi

#subject : Pandas
"""

"""
Pandas is an open source, BSD-licensed library providing high-performance, 
easy-to-use data structures and data analysis tools for the Python programming language.
"""
#pandas.Series is a one-dimensional ndarray where index can be labeled (including time series).

#Create series using python arrays
import pandas as pd
import numpy as np

#Create series using python arrays
labels = ['a', 'b', 'c'] #Define labels
my_list = [10, 20, 30] #Define python array

series_variable = pd.Series(data=my_list, index = labels) #Define pandas.series

print(series_variable)

#Create series using Python dict object
python_dict = {'a':15, 'b':42, 'c':36} #Define python dict

series_variable = pd.Series(python_dict) #Define pandas.series

print(series_variable) 

#If labels are not provided than index will be selected as integers starting from 0.

arr = np.array([55, 35, 22]) #Define a NumPy array

series_variable = pd.Series(data=arr) #Define pandas.series

print(series_variable)

"""
All basic mathematical operation (+, -, /, , *) can be applied between pandas.Series object based on their associated index values.
 They don’t need be of same length and the result will be the union of them.
"""

#Define pandas.Series
ser_1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
ser_2 = pd.Series([4, 5, 6, 7], index=['a', 'c', 'e', 'f'])

#Add two series
ser_res = ser_1 + ser_2

#print results
print(ser_res) 


"""
Pandas DataFrame

pandas.DataFrame is a two-dimensional tabular data structure with labeled axes (rows and columns). We can perform arithmetic operations on both row and column labels. 
It is a very powerful and mostly used object in Data Science.
"""
#Create pandas.DataFrame using Python dict object

#Create pandas.DataFrame using Python dict object
d = {'col1': [1, 2,3,4,5,6,7,8], 'col2': [3, 4,7,7,8,8,9,9]} #Define a dict object

df = pd.DataFrame(data=d) #Define pandas.DataFrame object

print(df)

#View top 5 rows of DataFrame
print(df.head())

#View bottom 5 rows of DataFrame
print(df.tail()) 

#Transposing your DataFrame
print(df.T)


#Sorting by an axix
print(df.sort_index(axis=1, ascending=False))

#Sorting by values
print(df.sort_values(by='col1'))

#Selecting a single column
print(df['col1'])

#Selecting a single row
print(df[0:1])

print(df.iloc[3:5,0:2])

print(df.iloc[1])


#Show all columns where values of column col1 is greater than zeros
print(df[df.col1 > 2])


#Add new column col3 as sum of col1 and col2.
df['col3'] = df['col1'] + df['col2']

print(df)

#Drop column col3, set inplace property to True to modify original DataFrame, set axis=1 for column
df.drop('col3', axis = 1, inplace=True)

print(df)

#Drop row 0, set inplace property to True to modify original DataFrame, set axis=0 for row
df.drop(0, axis = 0, inplace=True)

print('\n', df) #print after dropping the row


#summary or description of the dataframe

print( df.describe())

d1={"col4":['A','A','C','E','E','F','G','G']}

d.update(d1)

df=pd.DataFrame(d)


print( df["col4"].describe())


#Group data by column col4 and sum all values
print(df.groupby('col4').sum())

#Determine the mean of col4 by sum
print('\n', df.groupby("col4").mean())



#Create a DataFrame
df = pd.DataFrame({'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
'Sales':[200,120,340,124,243,350]})

print(df)

#Determine the mean of sales by each company
print('\n', df.groupby("Company").mean())

#Determine the number of employees and number of sales by each company
print('\n', df.groupby("Company").count())


#Create three DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']},
index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
'B': ['B4', 'B5', 'B6', 'B7'],
'C': ['C4', 'C5', 'C6', 'C7'],
'D': ['D4', 'D5', 'D6', 'D7']},
index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
'B': ['B8', 'B9', 'B10', 'B11'],
'C': ['C8', 'C9', 'C10', 'C11'],
'D': ['D8', 'D9', 'D10', 'D11']},
index=[8, 9, 10, 11])

#Concatenate on Row Level
print(pd.concat([df1, df2, df3]))











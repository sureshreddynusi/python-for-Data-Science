# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:49:20 2020

@author: Suresh Reddy Nusi
"""
import  pandas as pd
import numpy as np

d = {'col1': [1, 2,3,4,5,6,7,8], 'col2': [3, 4,7,7,8,8,9,9]} #Define a dict object

df = pd.DataFrame(data=d) #Define pandas.DataFrame object

print(df)

d1={"col4":['A','A','C','E','E','F','G','G']}

d.update(d1)

df=pd.DataFrame(d)

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

#Concatenate on Column Level
print(pd.concat([df1, df2, df3], axis = 1))

#Create a DataFrame
df = pd.DataFrame(np.random.randn(6,4), index= 'A B C D E F'.split(), columns=list('ABCD'))

#Add only three values to column E so that three values remain missing
df.loc[0:3,'E'] = 1

print(df)

#drop any rows that have missing data.
print(df.dropna(how='any'))
print(df)

#Filling missing data
print(df.fillna(value=5))

#forward fill data
print(df.ffill())


#Create a pivot table from ‘df’ DataFrame
#Create a DataFrame
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
'C' : np.random.randn(8),
'D' : np.random.randn(8)})

print(df)

#Create a pivot table from 'df' DataFrame
print('\n', pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))



#Merging the dataframes
#Create two DataFrames
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']})

#Join based on Column 'key'
print(pd.merge(left, right, how = 'inner', on='key'))


#Create two DataFrames
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
'key2': ['K0', 'K1', 'K0', 'K1'],
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
'key2': ['K0', 'K0', 'K0', 'K0'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']})

#Merge based on left
print(pd.merge(left, right))

#Create two DataFrames
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
'key2': ['K0', 'K1', 'K0', 'K1'],
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
'key2': ['K0', 'K0', 'K0', 'K0'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']})

#Merge based on right
print(pd.merge(right, left))

#Create two DataFrames
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
'key2': ['K0', 'K1', 'K0', 'K1'],
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
'key2': ['K0', 'K0', 'K0', 'K0'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']})

#Merge based on specific key
print(pd.merge(left, right, on =['key1']))
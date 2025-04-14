# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:39:00 2025

@author: marcj
"""

# %% Pandas # Imports
import numpy as np
import pandas as pd
import openpyxl
from sqlalchemy import create_engine
from numpy.random import randn

# %% Pandas Listen, NumPy Arrays oder Dictionaries in eine Series konvertieren:

labels = ["a","b","c"]
meine_liste = [10,20,30]
arr = np.array([10,20,30])
d = {"a":10,"b":20,"c":30}

print(labels)
print(meine_liste)
print(arr)
print(d)

# Listen nutzen
print(pd.Series(data=meine_liste))
print(pd.Series(data=meine_liste,index=labels))
# selbe, andere schreibweise
pd.Series(meine_liste,labels)

# Arrays 
print(pd.Series(arr))
# selbe, andere schreibweise
pd.Series(arr,labels)

# Dictionarys
print(pd.Series(d))

# Daten in einer Series
print(pd.Series(data=labels))

# Funktionen in Series
pd.Series([sum,print,len])

# %% Pandas Series 
ser1 = pd.Series([1,2,3,4],
                 index=["USA","Deutschland","Russland","Japan"])

ser2 = pd.Series([1,2,5,4],
                 index=["USA","Deutschland","Italien","Japan"])

print(ser1)
print(ser2)
print(ser1["USA"])
# %% Data Frames
# %% 

print(np.random.seed(101))
df = pd.DataFrame(randn(5,4),
                  index='A B C D E'.split(),
                  columns='W X Y Z'.split())

print(df)
# %% Pandas Indexieren
df["W"]
df[["W","Z"]]
type(df["W"])

# Neue Spalte erstellen 
df["neu"] = df["W"] + df["Y"]
df

# Spalte entfernen
df.drop('neu',axis=1,inplace=True)
df

# Zeilen entfernen
df.drop('E',axis=0)

# Zeile auswählen
df.loc['A'] 
df.iloc[2] # -> Position

# Subsets von zeilen und spalten wählen
df.loc['B','Y']

df.loc[['A','B'],['W','Y']]

# Bedingte Auswahl
df>0

df[df>0]

df[df['W']>0]

df[df['W']>0]['Y']

df[df['W']>0][['Y','X']]

df[(df['W']>0) & (df['Y'] > 1)]

# %% Pandas
# Standardindex zurücksetzen 
df.reset_index()

# neuen Index setzen
neuind = 'BY BW HH BB NW'.split()

df["Staaten"] = neuind

df

df.set_index('Staaten',inplace=True)

df
# %% Pandas Multi-Index und Index Hierarchie
außen = ['G1','G1','G1','G2','G2','G2']
innen = [1,2,3,1,2,3]
hier_index = list(zip(außen,innen))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df

# %%
df.loc['G1']

df.loc['G1'].loc[1]


# %% Daten Input & Output
# %%Pandas CSV Input & Output

df = pd.read_csv('Example.csv')
print(df)

df.to_csv('my_example.csv',index=False)

# %% Pandas Excel 
pd.read_excel('Excel_Sample.xlsx')

pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
print(df)

df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')

# %% Pandas HTML
df_html = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
df_html[0]

# %% Pandas SQL 
engine = create_engine('sqlite:///:memory:')

df.to_sql('data', engine)

sql_df = pd.read_sql('data',con=engine)
print(sql_df)



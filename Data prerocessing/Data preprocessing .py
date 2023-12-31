#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv', sep = '\t', engine = 'python', usecols = ['CanonicalizedReaction', 'Yield'])
df.head()

def delete_fuction(line):

    '''Function for deleting unnecessary condition between > and >'''

    first = line.find('>') + 1
    last = line.rfind('>')
    line = line[:first] + line[last:]
    return line

df['CanonicalizedReaction'] = np.vectorize(delete_fuction)(df['CanonicalizedReaction'])

# create a column where amount of reactants is presented
df['count_reactant'] = df['CanonicalizedReaction'].apply(lambda s: s.count('.')+1)
print('number of reactants:')
print(df['count_reactant'].value_counts())


# create a dataframe with 1 reagent
df1 = df[df['count_reactant']==1]
df1['reactant_1'] = df1['CanonicalizedReaction'].apply(lambda s: s.split('>>')[0])      
df1['reactant_2'] = 0
df1['product'] = df1['CanonicalizedReaction'].apply(lambda s: s.split('>>')[1])
df1= df1[['CanonicalizedReaction', 'reactant_1', 'reactant_2', 'product', 'Yield']]

# create a dataframe with 2 reagents
df2 = df[df['count_reactant']==2]
df2['reactant_1'] = df2['CanonicalizedReaction'].apply(lambda s: s.split('.')[0])      
df2['reactant_2'] = df2['CanonicalizedReaction'].apply(lambda s: s.split('.')[1].split('>>')[0])
df2['product'] = df2['CanonicalizedReaction'].apply(lambda s: s.split('>>')[1])
df2 = df2[['CanonicalizedReaction', 'reactant_1', 'reactant_2', 'product', 'Yield']]

# merge two dataframes with 1 reactant and 2 reactants
df3 = pd.concat([df1, df2], ignore_index = True)
df3['reactant_2'] = df3['reactant_2'].replace(0, None)
df3.to_csv('final_dataset.csv')

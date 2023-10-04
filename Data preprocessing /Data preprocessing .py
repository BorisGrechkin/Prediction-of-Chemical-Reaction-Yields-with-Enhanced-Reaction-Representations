#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np

df = pd.read_csv('D:\dataset.csv', sep = '\t', engine = 'python', usecols = ['CanonicalizedReaction', 'Yield'])
df.head()

def delete_fuction(line):
    first = line.find('>') + 1
    last = line.rfind('>')
    line = line[:first] + line[last:]
    return line

df['CanonicalizedReaction'] = np.vectorize(delete_fuction)(df['CanonicalizedReaction'])

df['count_reactant'] = df['CanonicalizedReaction'].apply(lambda s: s.count('.')+1)
print('number of reactants:')
print(df['count_reactant'].value_counts())

df = df[df['count_reactant']==2]
df['reactant_1'] = df['CanonicalizedReaction'].apply(lambda s: s.split('.')[0])      
df['reactant_2'] = df['CanonicalizedReaction'].apply(lambda s: s.split('.')[1].split('>>')[0])
df['product'] = df['CanonicalizedReaction'].apply(lambda s: s.split('>>')[1])
df = df[['reactant_1', 'reactant_2', 'product', 'Yield']]
print(df)
df.to_csv('final_df.csv, index=False')

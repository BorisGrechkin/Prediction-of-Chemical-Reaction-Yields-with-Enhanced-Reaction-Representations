#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np

df = pd.read_csv('final_dataset4.csv')
df_yield = pd.read_csv('final_dataset.csv', usecols = ['Yield'])

def delete_array(line):
    '''Deleting  unnecessary symbols from first column'''
    
    line = line[8:334].replace('\n', '').replace(' ','')
    res.append(line.split(','))
    
    return line

def split_lines(line):
    '''Split column for one symbol'''
    
    if type(line) == float: 
        res.append([None for x in range(100)])
    else:
        line = line.replace('\n', '').replace('[', '').replace(']', '')
        res.append(line.split(' '))

res = []
df['reaction_new'] = np.vectorize(delete_array)(df['reaction_new'])
reaction_new = pd.DataFrame(res[1:], columns = range(100))
reaction_new

res = []
np.vectorize(split_lines)(df['fingerprint_1'])
fingerprint_1 = pd.DataFrame(res[1:], columns = range(100))
fingerprint_1

res = []
np.vectorize(split_lines)(df['fingerprint_2'])
fingerprint_2 = pd.DataFrame(res[1:], columns = range(100))
fingerprint_2

res = []
np.vectorize(split_lines)(df['product_new'])
product_new = pd.DataFrame(res[1:], columns = range(100))
product_new

list_of_dfs = [reaction_new, fingerprint_1, fingerprint_2, product_new, df_yield]

res_df = pd.concat(list_of_dfs, axis=1) 

res_df.to_csv('result.csv', index=False)

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

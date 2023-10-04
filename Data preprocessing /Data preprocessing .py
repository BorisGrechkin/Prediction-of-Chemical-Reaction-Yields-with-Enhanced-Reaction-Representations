#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np


# In[59]:


df = pd.read_csv('D:\dataset.csv', sep = '\t', engine = 'python', usecols = ['CanonicalizedReaction', 'Yield'])
df.head()


# In[60]:


def delete_fuction(line):
    first = line.find('>') + 1
    last = line.rfind('>')
    line = line[:first] + line[last:]
    return line


# In[65]:


df['CanonicalizedReaction'] = np.vectorize(delete_fuction)(df['CanonicalizedReaction'])


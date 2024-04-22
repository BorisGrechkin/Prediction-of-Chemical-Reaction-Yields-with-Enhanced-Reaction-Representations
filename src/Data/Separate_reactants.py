import os

import pandas as pd

from Scripts.data_preprocess import Data_preprocess

os.chdir('../../')

if __name__ == "__main__":

    df = pd.read_csv('Data\dataset.csv', sep = '\t',
                     engine = 'python', usecols = ['CanonicalizedReaction', 'Yield'])

    res = Data_preprocess.find_reactants(df, 'CanonicalizedReaction')

    res.to_csv('Data/separated_reactants.csv', index=False)

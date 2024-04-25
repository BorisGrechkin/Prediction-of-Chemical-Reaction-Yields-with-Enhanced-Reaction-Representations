import os

import pandas as pd

from scripts.data_preprocess import Data_preprocess

os.chdir('../../')

if __name__ == "__main__":

    df = pd.read_csv('Data\separated_reactants.csv')

    df['product_new'] = df['product'].apply(Data_preprocess.vec)
    df = pd.concat([df['product_new'].apply(Data_preprocess.split_array_to_columns),
                    df.drop('product_new', axis=1)], axis=1)

    df['reactant1_new'] = df['reactant1'].apply(Data_preprocess.vec)
    df = pd.concat([df['reactant1_new'].apply(Data_preprocess.split_array_to_columns),
                    df.drop('reactant1_new', axis=1)], axis=1)

    df['reactant2_new'] = df['reactant2'].apply(Data_preprocess.vec)
    df = pd.concat([df['reactant2_new'].apply(Data_preprocess.split_array_to_columns),
                    df.drop('reactant2_new', axis=1)], axis=1)

    df.drop(['product', 'reactant1', 'reactant2', 'CanonicalizedReaction'], inplace=True, axis=1)

    df.to_csv('Data/prepeared_dataset.csv', index=False)

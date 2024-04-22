'''
Module for data preprocessing
'''

import pandas as pd

class Data_preprocess():

    '''
    Class for data preprocessing
    '''

    @staticmethod
    def find_reactants(df, column):

        '''
        Function to find 1 or 2 reactants
        with product of chemical reaction
        in USPTO organic reactions

        Parameters:

        df(pd.Dataframe): The dataframe to process.
        column(str): The column containing the reactions.

        Returns:
        A dataframe with the following columns:

        reactant1: The first reactant in the reaction.
        reactant2: The second reactant in the reaction (if any).
        pruduct: The product of the reaction.
        '''


        assert column in df.columns, ('No such column in DataFrame, '
                                      'enter another')

        df[column] = df[column].str.replace(r'>.*?>', '>>', regex=True)

        df['count_reactant'] = df[column].apply(lambda s: s.count('.') + 1)

        df1 = df[df['count_reactant'] == 1]
        split = df1[column].str.split('>>', expand=True)
        split['reactant2'] = None
        split = split.rename(columns={0: 'reactant1', 1: 'pruduct'})
        df1 = df1.join(split)

        df2 = df[df['count_reactant'] == 2]
        split = df2[column].str.split('>>', expand=True)
        split = split.rename(columns={0: 'reactant1', 1: 'pruduct'})
        split2 = split['reactant1'].str.split('.', expand=True)
        split2 = split2.rename(columns={1: 'reactant2'})
        df2 = df2.join([split, split2['reactant2']])

        df3 = pd.concat([df1, df2], ignore_index=True)
        df3.drop('count_reactant', axis=1, inplace=True)

        return df3
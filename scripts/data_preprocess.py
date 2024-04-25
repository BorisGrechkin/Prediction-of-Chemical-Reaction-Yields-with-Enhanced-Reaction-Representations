'''
Module for data preprocessing
'''

import pandas as pd
import numpy as np
from rdkit import Chem
import numpy as np
from rdkit.Chem import AllChem
from drfp import DrfpEncoder

class Data_preprocess():

    '''
    Class for data preprocessing
    '''

    @staticmethod
    def find_reactants(df, column):

        '''
        Function to find 1 or 2 reactants
        with the product of chemical reaction
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
        split['reactant2'] = np.nan
        split = split.rename(columns={0: 'reactant1', 1: 'product'})
        df1 = df1.join(split)

        df2 = df[df['count_reactant'] == 2]
        split = df2[column].str.split('>>', expand=True)
        split = split.rename(columns={0: 'reactant1', 1: 'product'})
        split2 = split['reactant1'].str.split('.', expand=True)
        split2 = split2.rename(columns={1: 'reactant2'})
        df2 = df2.join([split, split2['reactant2']])

        df3 = pd.concat([df1, df2], ignore_index=True)
        df3.drop('count_reactant', axis=1, inplace=True)

        return df3

    @staticmethod
    def vec(smiles, radius=2, nBits=100):
        """
        Converts a SMILES (Simplified Molecular Input Line Entry System)
        string into a fixed-size vector representation using Morgan fingerprint.

        Parameters:
        - smiles (str): A SMILES string representing a molecule.
        - radius (int, optional): The radius parameter for Morgan fingerprint generation. Default is 2.
        - nBits (int, optional): The number of bits for the fingerprint. Default is 100.

        Returns:
        - vec (numpy.ndarray or None): If the input SMILES is str
        and can be converted into a molecular representation,
        returns a numpy array representing the Morgan fingerprint of the molecule.
        If the input SMILES is not type of str, returns None.

        Note:
        The function uses the RDKit library to convert SMILES
        into a molecular representation and then generates
        Morgan fingerprints for the molecule.
        Morgan fingerprints are circular fingerprints that encode molecular
        structure information up to a certain radius around each atom.

        """
        if isinstance(smiles, str):

            mol = Chem.MolFromSmiles(smiles)
            fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=radius, nBits=nBits)
            vec = np.array(fp)
            return vec
        else:
            return None

    @staticmethod
    def encode_reaction(reaction_smiles, n_folded_length=100):

        '''
        Encodes a reaction SMILES (Simplified Molecular Input Line Entry System)
        string into a fixed-size vector representation using
        DRFP (Dense Random Forest Fingerprints) encoding.

        Parameters:
        - reaction_smiles (str): A reaction SMILES string representing a chemical reaction.
        - n_folded_length (int, optional): The desired length of the folded DRFP vector. Default is 100.

        Returns:
        - vec (numpy.ndarray): A numpy array representing the DRFP encoding of the reaction.

        Note:
        The function utilizes the DrfpEncoder to encode reaction SMILES
        into a fixed-size vector representation using DRFP encoding.
        DRFP encoding converts reaction SMILES into dense vectors
        suitable for machine learning tasks

        '''
        encoded = DrfpEncoder.encode(reaction_smiles,
                           n_folded_length=n_folded_length)

        print(type(encoded[0]))

        return encoded[0]
    @staticmethod
    def split_array_to_columns(arr):

        '''
        Splits a NumPy array into separate columns of a pandas DataFrame.

        Parameters:
        - arr (numpy.ndarray): The NumPy array to split into columns.

        Returns:
        - pandas.Series: A Series containing the elements of the input array.
        '''

        return pd.Series(arr, dtype=int)


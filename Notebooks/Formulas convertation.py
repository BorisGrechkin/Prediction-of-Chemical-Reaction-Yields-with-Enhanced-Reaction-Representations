# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np
from drfp import DrfpEncoder

data = pd.read_csv('/content/final_dataset3.csv')
df = pd.DataFrame(data)

smiles = df.at[0, 'reactant_1']

mol = Chem.MolFromSmiles(smiles)

rdkit.Chem.rdchem.Mol

fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=100)

vec = np.array(fp)

def vec(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=100)
        vec = np.array(fp)
        return vec
    else:
        return None

df['product_new'] = df['product'].apply(vec)
data

df['reactant_1_new'] = df['reactant_1'].apply(vec)

df['reactant_2_new'] = df['reactant_2'].apply(vec)

del data['reactant_1']

del data['reactant_2']

del data['product']

file_path = '/content/data.csv'  # Замените это на путь и имя вашего файла

# Save DataFrame to CSV
data.to_csv(file_path, index = False)

df = pd.DataFrame(data)

rxn_smiles = df.at[0, 'CanonicalizedReaction']

fps = DrfpEncoder.encode(rxn_smiles, n_folded_length=100)

def encode_reaction(reaction_smiles):
    drfp = DrfpEncoder.encode(reaction_smiles, n_folded_length=100)
    return drfp[0]

df['reaction_new'] = df['CanonicalizedReaction'].apply(encode_reaction)

del data['CanonicalizedReaction'], data['Yield']

df = pd.DataFrame(data)

df = df[['reaction_new', 'reactant_1_new', 'reactant_2_new', 'product_new', 'Yield']]

df = pd.DataFrame(df)

df['reaction_new'] = df['reaction_new'].astype(str)

# Разделяем каждую цифру 0 и 1 в строке на отдельные клетки
df['reaction_new'] = df['reaction_new'].apply(lambda x: ' '.join(list(x)))

# Теперь каждое 0 и 1 находится в отдельной клетке столбца

df['reactant_1_new'] = df['reactant_1_new'].astype(str)

df['reactant_1_new'] = df['reactant_1_new'].apply(lambda x: ' '.join(list(x)))

df['reactant_2_new'] = df['reactant_2_new'].astype(str)

df['reactant_2_new'] = df['reactant_2_new'].apply(lambda x: ' '.join(list(x)))

df['product_new'] = df['product_new'].astype(str)

df['product_new'] = df['product_new'].apply(lambda x: ' '.join(list(x)))
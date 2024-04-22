import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from yaml import load, Loader
import numpy as np

if __name__ == "__main__":

    df = pd.read_csv('Data\prepeared_dataset.csv')

    target = df[df.columns[-1]].values
    data = df[df.columns[:-1]].values

    with open("configs/train_config.yml", "r") as conf:
        train_config = load(conf, Loader=Loader)["train_config"]

    np.random.seed(train_config["seed"])

    X_train, X_test, y_train, y_test = train_test_split(data, target,
                                                     test_size=train_config["test_size"])


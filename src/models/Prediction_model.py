import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from yaml import load, Loader

os.chdir('../../')

if __name__ == "__main__":

    df = pd.read_csv('Data\prepeared_dataset.csv')

    target = df[df.columns[-1]].values
    data = df[df.columns[:-1]].values

    with open("Configs/train_config.yml", "r") as conf:
        train_config = load(conf, Loader=Loader)["train_config"]

    np.random.seed(train_config["seed"])

    X_train, X_test, y_train, y_test = train_test_split(data, target,
                                                     test_size=train_config["test_size"])

    xgb_model = xgb.XGBRegressor(random_state = train_config["seed"])

    xgb_model.fit(X_train, y_train)
    y_pred = xgb_model.predict(X_test)
    y_pred1 = xgb_model.predict(X_train)

    RMSE = mean_squared_error(y_test, y_pred, squared=False)
    R2 = r2_score(y_test, y_pred)

    fig = plt.figure(figsize=(10, 7))
    legend = ['Train', 'Test']
    plt.scatter(y_train, y_pred1, c='purple', s=10)
    plt.scatter(y_test, y_pred, c='pink', s=10)
    plt.legend(legend, loc='best')
    plt.xlabel("Y True")
    plt.ylabel("Y Predicted")
    plt.savefig('Vizualization/result.jpg')


    #with Live(save_dvc_exp=True) as live:
        #live.log_params(train_config)
        #live.log_artifact("%s/linear_model.pickle" % os.environ.get("MODELS_PATH"))
        #live.log_metric("train_R2", R2)
        #live.log_metric("test_RMSE", RMSE)

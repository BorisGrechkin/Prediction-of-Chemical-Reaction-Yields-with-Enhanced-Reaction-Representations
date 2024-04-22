import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from yaml import load, Loader
import numpy as np
from dvclive import Live

if __name__ == "__main__":

    df = pd.read_csv('Data\prepeared_dataset.csv')

    target = df[df.columns[-1]].values
    data = df[df.columns[:-1]].values

    with open("configs/train_config.yml", "r") as conf:
        train_config = load(conf, Loader=Loader)["train_config"]

    np.random.seed(train_config["seed"])

    X_train, X_test, y_train, y_test = train_test_split(data, target,
                                                     test_size=train_config["test_size"])

    xgb_model = xgb.XGBRegressor(random_state = train_config["seed"])

    xgb_model.fit(X_train, y_train)
    y_pred = xgb_model.predict(X_test)

    RMSE = mean_squared_error(y_test, y_pred, squared=False)
    R2 = r2_score(y_test, y_pred)

    with Live(save_dvc_exp=True) as live:
        live.log_params(train_config)
        #live.log_artifact("%s/linear_model.pickle" % os.environ.get("MODELS_PATH"))
        live.log_metric("train_R2", R2)
        live.log_metric("test_RMSE", RMSE)

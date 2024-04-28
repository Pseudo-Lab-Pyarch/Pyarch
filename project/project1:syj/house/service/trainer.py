import os
from datetime import date
from typing import Tuple

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from domain.house import House
from domain.model import Model

DATA_DIR = "data"
MODEL_DIR = "models"

def load_data(path):
    data = pd.read_csv(os.path.join(DATA_DIR, path))
    X = data.drop("SalePrice", axis=1)
    y = data["SalePrice"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    training_performance = model.score(X_train, y_train)
    model_type = "LinearRegression"
    storage_location = os.path.join(MODEL_DIR, f"{model_type}_{date.today().strftime('%Y%m%d')}.pkl")
    os.makedirs(MODEL_DIR, exist_ok=True)
    model.save(storage_location)
    return Model(model_type, training_performance, storage_location)

def train_and_save_model(path):
    X_train, _, y_train, _ = load_data(path)
    model = train_model(X_train, y_train)
    return model

if __name__ == "__main__":
    path = "train.csv"
    model = train_and_save_model(path)
import os
import pickle
from typing import Dict
from datetime import date

import pandas as pd

from domain.house import House
from domain.model import Model

MODEL_DIR = "models"

def load_latest_model():
    model_files = os.listdir(MODEL_DIR)

    latest_model_file = sorted(model_files, reverse=True)[0]
    model_path = os.path.join(MODEL_DIR, latest_model_file)

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    model_type, model_date = os.path.splitext(latest_model_file)[0].split("_")
    model_date = date.fromisoformat(model_date)

    return Model(model_path, model_type, model_date)

def make_prediction(house, model):
    X = pd.DataFrame([house.get_features()])
    prediction = model.predict(X)[0]
    return prediction

def get_house_price(house):
    model = load_latest_model()
    predicted_price = make_prediction(house, model)
    return {"predicted_price": predicted_price}

if __name__ == "__main__":
    house = House(1234, 2024, 10, 2)  # id, built year, 1stFlrSF, bedroom #
    price_info = get_house_price(house)
    print(price_info)
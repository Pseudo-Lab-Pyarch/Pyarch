import pandas as pd
from abc import ABCMeta, abstractmethod
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from src.house_price.domain.entity import TrainingModelData, ModelInfo
from typing import List


class HousePricePredictor(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def set_data(self, data: List[TrainingModelData]):
        pass

    @abstractmethod
    def set_model_info(self, model, name: str) -> None:
        pass

    @abstractmethod
    def preprocess_data(self) -> None:
        pass

    @abstractmethod
    def train_model(self) -> None:
        pass

    @abstractmethod
    def predict(self, x) -> list:
        pass

    @abstractmethod
    def get_model(self) -> ModelInfo:
        pass


class HousePricePredictorImpl(HousePricePredictor):
    def __init__(self):
        self.data = None
        self.model = None
        self.model_name = None
        self.scaler = StandardScaler()
        self.encoder = LabelEncoder()
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        super().__init__()

    def _check_data(self):
        if self.data is None:
            raise ValueError("Data not set. Please set data using `set_data()` method before proceeding.")

    def _check_training_data(self):
        if self.x_train is None or self.x_test is None or self.y_train is None or self.y_test is None:
            raise ValueError("Training data not set. Please preprocess data using `preprocess_data()` method before training.")

    def set_data(self, data: List[TrainingModelData]) -> None:
        self.data = pd.DataFrame([item.dict() for item in data])

    def set_model_info(self, model, name: str) -> None:
        self.model = model
        self.model_name = name

    def preprocess_data(self) -> None:
        self._check_data()
        train_y = self.data['SalePrice']
        train = self.data.drop(['SalePrice'], axis=1)

        for column in train.columns:
            typ = train[column].dtype
            if typ == "object":
                train[column] = train[column].fillna(train[column].mode()[0])
            else:
                train[column] = train[column].fillna(train[column].mean())

        for col in train.columns:
            if train[col].dtype == "object":
                train[col] = self.encoder.fit_transform(train[col]).astype(int)

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(train, train_y, test_size=0.2,
                                                                                random_state=42)
        self.x_train = self.scaler.fit_transform(self.x_train)
        self.x_test = self.scaler.transform(self.x_test)

    def train_model(self) -> None:
        self._check_training_data()
        self.model.fit(self.x_train, self.y_train)

    def predict(self, x) -> list:
        self._check_training_data()
        x = self.scaler.transform([x])
        return self.model.predict(x)

    def get_model(self) -> ModelInfo:
        return ModelInfo(model_name=self.model_name, model=self.model)

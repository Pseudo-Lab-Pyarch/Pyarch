from pydantic import BaseModel, field_validator
from pydantic.types import conint, PositiveInt
from sklearn.model_selection import train_test_split
from datetime import date


class HouseDataModel(BaseModel):
    overall_qual: conint(ge=1, le=10)
    gr_liv_area: PositiveInt
    second_flr_sf: int = 0
    total_bsmt_sf: int = 0
    garage_cars: int = 0
    price: float = 0
    date: date

    @field_validator('second_flr_sf', 'total_bsmt_sf', 'garage_cars')
    def check_non_negative(cls, value):
        if value < 0:
            raise ValueError("This field must be zero or positive")
        return value


class HouseModel:
    def __init__(self, model):
        self.model = model

    def train(self, features, targets):
        X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

        score = self.model.score(X_test, y_test)
        print(f"Model training completed. Test score: {score:.2f}")

    def predict(self, features):
        return self.model.predict(features)

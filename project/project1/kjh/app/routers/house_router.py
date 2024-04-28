from fastapi import APIRouter
from src.house_price.di import HousePriceContainer
from src.house_price.domain.entity import UpdateHouseData
from src.house_price.domain.model_entity import regression_models
from typing import List, Optional

router = APIRouter(
    prefix="/house",
    tags=["house"],
)

config = {
    "host": "localhost",
    "database": "pyarchitecture",
    "user": "root",
    "password": "Wjdgns1219@@"
}

container = HousePriceContainer(config=config).house_price_di()


@router.post("/house/add_data")
def add_data(param: List[UpdateHouseData]) -> None:
    print("test")
    container.add_house_data(param)

@router.post("/house/train_and_save_model")
def train_and_save_model(date_range: Optional[str], model: str, model_name: Optional[str]) -> None:
    container.train_and_save_model(date_range, regression_models[model], model_name)
    print("test")

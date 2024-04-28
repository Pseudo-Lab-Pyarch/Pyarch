from src.house_price.domain.service import HousePriceService
from src.house_price.domain.entity import UpdateHouseData
from typing import List, Optional


class HousePriceFacade:
    def __init__(self, house_price_servie: HousePriceService) -> None:
        self.house_price_servie = house_price_servie

    def train_and_save_model(self,
                             date_range: Optional[str],
                             model,
                             model_name: Optional[str]):
        self.house_price_servie.train_and_save_model(date_range, model, model_name)

    def add_house_data(self, data: List[UpdateHouseData]):
        return self.house_price_servie.add_house_data(data)

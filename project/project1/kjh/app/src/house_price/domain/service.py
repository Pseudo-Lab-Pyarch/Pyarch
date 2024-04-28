from abc import ABCMeta, abstractmethod
from src.house_price.domain.entity import UpdateHouseData
from src.house_price.infrastructure.model_training import HousePricePredictor
from src.house_price.adapters.repository import Repository
from typing import List, Optional


class HousePriceService(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def train_and_save_model(self,
                             date_range: Optional[str],
                             model,
                             model_name: Optional[str]) -> None:
        pass

    @abstractmethod
    def add_house_data(self, data: List[UpdateHouseData]):
        pass


class HousePriceServiceImpl(HousePriceService):
    def __init__(self,
                 repository: Repository,
                 house_price_predictor: HousePricePredictor) -> None:
        self.repository = repository
        self.house_price_predictor = house_price_predictor
        super().__init__()

    def train_and_save_model(self,
                             date_range: Optional[str],
                             model,
                             model_name: Optional[str]) -> None:
        data = self.repository.get_house_data(date_range)
        self.house_price_predictor.set_data(data)
        self.house_price_predictor.set_model_info(model, model_name)
        self.house_price_predictor.preprocess_data()
        self.house_price_predictor.train_model()
        self.repository.save_prediction_model(
            self.house_price_predictor.get_model()
        )

    def add_house_data(self, data: List[UpdateHouseData]):
        return self.repository.add_house_data(data)

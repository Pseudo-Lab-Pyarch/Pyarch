from abc import ABCMeta, abstractmethod
from src.domain.models import HouseDataModel


class DataRepository(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def save_house_data(self, house_data: list[HouseDataModel]):
        pass

    @abstractmethod
    def fetch_house_data(self, date: str) -> list[HouseDataModel]:
        pass

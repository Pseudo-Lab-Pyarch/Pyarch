from abc import ABCMeta, abstractmethod
from src.domain.models import HouseDataModel


class DataProcessor(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def split_features_targets(self, house_data: list[HouseDataModel]) -> tuple:
        pass

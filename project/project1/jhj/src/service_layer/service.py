from abc import ABCMeta, abstractmethod
from src.domain.data_repository import DataRepository
from src.domain.model_repository import ModelRepository
from src.domain.data_processor import DataProcessor
from src.domain.models import HouseDataModel, HouseModel


class HouseDataService(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def add_data_and_fetch(self, house_data: list[dict], date: str) -> list[HouseDataModel]:
        pass


class HouseModelService(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def train_and_save_model(self, model_path, house_data: HouseDataModel, date: str):
        pass


class HouseDataServiceImpl(HouseDataService):
    def __init__(self, data_repository: DataRepository):
        self.data_repository = data_repository
        super().__init__()

    def add_data_and_fetch(self, house_data: list[dict], date: str) -> list[HouseDataModel]:
        validated_data = [HouseDataModel(**row) for row in house_data]
        self.data_repository.save_house_data(validated_data)

        return self.data_repository.fetch_house_data(date)


class HouseModelServiceImpl(HouseModelService):
    def __init__(self, model_repository: ModelRepository, data_processor: DataProcessor):
        self.model_repository = model_repository
        self.data_processor = data_processor
        super().__init__()

    def train_and_save_model(self, model_path, house_data: list[HouseDataModel], date: str):
        features, targets = self.data_processor.split_features_targets(house_data)
        model = self.model_repository.load_model(model_path)

        house_model = HouseModel(model=model)
        house_model.train(features, targets)

        self.model_repository.save_model(house_model.model, model_path, date)

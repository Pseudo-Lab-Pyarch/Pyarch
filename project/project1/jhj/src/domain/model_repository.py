from abc import ABCMeta, abstractmethod


class ModelRepository(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def load_model(self, model_path):
        pass

    @abstractmethod
    def save_model(self, model, model_path, date):
        pass

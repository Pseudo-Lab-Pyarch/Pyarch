from src.domain.model_repository import ModelRepository
import pickle
import os


class ModelRepositoryImpl(ModelRepository):
    def __init__(self):
        super().__init__()

    def load_model(self, model_path):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model

    def save_model(self, model, model_path, date):
        model_dir = os.path.dirname(model_path)
        print(model_dir, "model_dir")
        new_model_name = f"model-{date}.pkl"
        new_model_path = os.path.join(model_dir, new_model_name)
        with open(new_model_path, 'wb') as file:
            pickle.dump(model, file)

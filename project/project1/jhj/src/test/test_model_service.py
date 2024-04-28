import unittest
from src.domain.models import HouseDataModel
from src.service_layer.service import HouseModelServiceImpl
from src.infrastructure.model_repository import ModelRepositoryImpl
from src.infrastructure.data_processor import DataProcessorImpl
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '..', 'model_database', 'model-2024-04-08.pkl')


class TestHouseModelServiceImpl(unittest.TestCase):
    def setUp(self):
        self.service = HouseModelServiceImpl(
            model_repository=ModelRepositoryImpl(),
            data_processor= DataProcessorImpl()
        )

        self.test_data = [
            HouseDataModel(overall_qual=5, gr_liv_area=1077, second_flr_sf=0, total_bsmt_sf=991, garage_cars=1, price=118000.0, date="2024-04-09"),
            HouseDataModel(overall_qual=8, gr_liv_area=1795, second_flr_sf=0, total_bsmt_sf=1777, garage_cars=2, price=230000.0, date="2024-04-09")
        ]
        self.test_date = "2024-04-09"
        self.test_model_path = model_path

    def test_train_and_save_model(self):
        self.service.train_and_save_model(self.test_model_path, self.test_data, self.test_date)


if __name__ == '__main__':
    unittest.main()

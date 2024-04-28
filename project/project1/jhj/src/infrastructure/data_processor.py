from src.domain.data_processor import DataProcessor
from src.domain.models import HouseDataModel


class DataProcessorImpl(DataProcessor):
    def __init__(self):
        super().__init__()

    def split_features_targets(self, house_data: list[HouseDataModel]) -> tuple:
        features = []
        targets = []

        for data in house_data:
            features.append([
                data.overall_qual,
                data.gr_liv_area,
                data.second_flr_sf,
                data.total_bsmt_sf,
                data.garage_cars
            ])
            targets.append(data.price)

        return features, targets

from di import HouseContainer
from utils import load_csv_as_dict


if __name__ == "__main__":
    config = {"database_url": "project.db"}
    container = HouseContainer(config=config)

    house_data_service = container.house_data_di()
    house_model_service = container.house_model_di()

    add_new_data = load_csv_as_dict("database/2024-04-10.csv")
    date = "2024-04-10"

    result_data = house_data_service.add_data_and_fetch(add_new_data, date)

    model_path = "model_database/model-2024-04-09.pkl"
    house_model_service.train_and_save_model(model_path, result_data, date)

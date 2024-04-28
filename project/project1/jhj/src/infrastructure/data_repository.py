import sqlite3
from src.domain.data_repository import DataRepository
from src.domain.models import HouseDataModel


class DataRepositoryImpl(DataRepository):
    def __init__(self, connection):
        self.connection = connection
        self.connection.row_factory = sqlite3.Row
        super().__init__()

    def save_house_data(self, house_data: list[HouseDataModel]):
        query = """
        INSERT INTO house_data (overall_qual, gr_liv_area, second_flr_sf, total_bsmt_sf, garage_cars, date, price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = self.connection.cursor()
        params = [(row.overall_qual, row.gr_liv_area, row.second_flr_sf, row.total_bsmt_sf,
                   row.garage_cars, row.date, row.price) for row in house_data]

        cursor.executemany(query, params)
        self.connection.commit()
        cursor.close()

    def fetch_house_data(self, date: str) -> list[HouseDataModel]:
        query = f"""
            SELECT 
                overall_qual, gr_liv_area, second_flr_sf, total_bsmt_sf, garage_cars, date, price
            FROM house_data
            WHERE date = '{date}'
            """
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return [HouseDataModel(**dict(row)) for row in results]

import unittest
from src.infrastructure.data_repository import DataRepositoryImpl
from src.service_layer.service import HouseDataServiceImpl
import sqlite3
from utils import load_csv_as_dict
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, '..', 'database', '2024-04-09.csv')


def setup_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS house_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            overall_qual INTEGER,
            gr_liv_area INTEGER,
            second_flr_sf INTEGER,
            total_bsmt_sf INTEGER,
            garage_cars INTEGER,
            date DATE
        );
    """)
    conn.commit()
    conn.close()


class RealDatabaseTest(unittest.TestCase):
    db_path = 'test.db'

    @classmethod
    def setUpClass(cls):
        setup_database(cls.db_path)

    def setUp(self):
        self.new_data = load_csv_as_dict(data_path)
        self.conn = sqlite3.connect(self.db_path, isolation_level='EXCLUSIVE')
        self.conn.execute('BEGIN')

    def tearDown(self):
        self.conn.rollback()
        self.conn.close()

    def test_data_insert_and_fetch(self):
        data_repository = DataRepositoryImpl(self.conn)
        service = HouseDataServiceImpl(data_repository=data_repository)

        date = self.new_data[0]["date"]
        results = service.add_data_and_fetch(self.new_data, date)
        self.assertTrue(len(results) == 112)


if __name__ == '__main__':
    unittest.main()

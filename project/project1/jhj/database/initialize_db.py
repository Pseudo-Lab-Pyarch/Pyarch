import sqlite3


def create_tables(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS house_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            overall_qual INTEGER,
            gr_liv_area INTEGER,
            second_flr_sf INTEGER,
            total_bsmt_sf INTEGER,
            garage_cars INTEGER,
            price FLOAT,
            date DATE
        );
    """)
    connection.commit()
    connection.close()


create_tables('../project.db')

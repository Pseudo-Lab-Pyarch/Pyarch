from project.project1.kjh.app.src.house_price.adapters.repository import RepositoryImpl
from project.project1.kjh.app.src.database import get_mysql_conn

conn = get_mysql_conn(
    host="localhost",
    user="root",
    password="Wjdgns1219@@",
    database="pyarchitecture"
)

a = RepositoryImpl(conn=conn)

print(a.get_house_data(None))
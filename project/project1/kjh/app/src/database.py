from typing import List
import logging
import pymysql


def get_mysql_conn(host: str, user: str, password: str, database: str):
    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=database,
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )


def execute_query(query: str, conn) -> List[dict]:
    cur = conn.cursor()
    try:
        cur.execute(query)
        result = cur.fetchall()
    except Exception as e:
        logging.exception(f"An error occurred: {e}, query: {query}")
        raise Exception('select query failed')
    finally:
        cur.close()
    return result


def mysql_commit_query(query: str, data: list, conn) -> None:
    cursor = conn.cursor()
    try:
        cursor.executemany(query, data)
        conn.commit()
    except Exception as e:
        logging.exception(e)
        cursor.execute('ROLLBACK')
        raise Exception('query failed')
    finally:
        cursor.close()

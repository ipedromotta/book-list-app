import sqlite3

class ConnectionDatabase():

    @staticmethod
    def get_connection():
        try:
            conn = sqlite3.connect('database.db', check_same_thread=False)
            return conn
        except Exception as e:
            print(e)

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
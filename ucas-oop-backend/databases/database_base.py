import sqlite3

class Database(object):
    __db_name = "markitdown.db"
    def __init__(self):
        self.conn = sqlite3.connect(self.__db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()




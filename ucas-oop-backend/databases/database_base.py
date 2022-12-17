import sqlite3

class Database(object):
    __db_name = "markitdown.db"
    conn = sqlite3.connect(__db_name)
    cursor = conn.cursor()
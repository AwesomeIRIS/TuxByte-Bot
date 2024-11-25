import mysql.connector
import os

def get_db_cursor():
    db = mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database=""
    )
    cursor = db.cursor()
    return db, cursor

def close_db_connection(db, cursor):
    cursor.close()
    db.close()

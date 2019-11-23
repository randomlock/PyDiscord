import os

import mysql.connector
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

def get_db_connection():
    config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
    }
    print('he;llo')
    print(config)
    db_connection = mysql.connector.connect(**config)
    return db_connection


def setup_database_and_table():
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    # cur.execute("CREATE DATABASE IF NOT EXISTS discord")
    # cur.execute("USE discord")
    cur.execute('''
    CREATE TABLE IF NOT EXISTS search_history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        created DATETIME,
        search_key VARCHAR(255) NOT NULL UNIQUE
    )
    '''
                )


def create_search_history(search_keyword):
    add_employee = ("REPLACE  INTO search_history"
                    "(search_key, created)"
                    "VALUES (%s, %s)")
    data = (search_keyword, datetime.utcnow())
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    # cur.execute("USE discord")
    cur.execute(add_employee, data)
    db_connection.commit()
    cur.close()
    db_connection.close()


def get_search_history(search_keyword):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    # cur.execute("USE discord")
    cur.execute('''SELECT search_key FROM search_history where search_key LIKE '%{}%' 
    ORDER BY created DESC LIMIT 5'''.format(search_keyword)
                )
    search_results = []
    for result in cur.fetchall():
        search_results.append(result[0])
    cur.close()
    return search_results

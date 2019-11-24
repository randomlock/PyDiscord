import mysql.connector
from datetime import datetime

import settings as discord_settings


def get_db_connection():
    config = {
        'user': discord_settings.DB_USER,
        'password': discord_settings.DB_PASSWORD,
        'host': discord_settings.DB_HOST,
        'database': discord_settings.DB_NAME,
    }

    db_connection = mysql.connector.connect(**config)
    return db_connection


def setup_db_table():
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    cur.execute(
        '''
            CREATE TABLE IF NOT EXISTS search_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                created DATETIME,
                search_key VARCHAR(255) NOT NULL UNIQUE
            )
        '''
    )


def create_search_history(search_keyword):
    add_employee = (
        "REPLACE  INTO search_history"
        "(search_key, created)"
        "VALUES (%s, %s)"
    )
    db_connection = get_db_connection()
    data = (search_keyword, datetime.utcnow())
    cur = db_connection.cursor()
    cur.execute(add_employee, data)
    db_connection.commit()
    cur.close()


def get_search_history(search_keyword):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    cur.execute(
        '''
        SELECT search_key FROM search_history where search_key LIKE '%{}%' 
        ORDER BY created DESC LIMIT {}
        '''.format(
            search_keyword,
            discord_settings.MAX_SEARCH_HISTORY_RESULT_COUNT,
        )
    )
    search_results = []
    for result in cur.fetchall():
        search_results.append(result[0])
    cur.close()
    return search_results

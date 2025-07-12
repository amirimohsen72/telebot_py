import sqlite3

MAIN_DB = sqlite3.connect('test_db.db',check_same_thread=False)
MAIN_CURSOR = MAIN_DB.cursor()




MAIN_CURSOR.execute(
    '''CREATE TABLE users (
    chat_id varchar(300),
    age varchar(20),
    name varchar(300),
    last_name varchar(300),
    status varchar(255)
);'''
)


MAIN_DB.commit()
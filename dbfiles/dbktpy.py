import sqlite3
import os

PATH = os.path.abspath(__file__ + '/..')

connect = sqlite3.connect(f'{PATH}/database.db', check_same_thread=False)

cursor = connect.cursor()


#func to create an sql table in database.db
def create_table():
    sql1 = '''
    CREATE TABLE users (
        nickname varchar(255)
    );
    '''

    cursor.execute()


#command to add user
def add_user(nickname):
    add_user = f'''
    INSERT INTO users
    VALUES ('{nickname}');
    '''
    cursor.execute()
    connect.commit()

#command to get users
def get_users():
    get_users = '''
    SELECT * FROM users;'''
    cursor.execute(get_users)
    result = cursor.fetchall()
    return result



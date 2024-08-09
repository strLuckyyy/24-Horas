__package__ = "com.SQLite"

import sqlite3


def connect() -> sqlite3:
    try:
        conn = sqlite3.connect('tasklist.db')
        return conn
    except:
        print('Error: Cannot connect to database.')
        return None

def disconnect(conn) -> None:
    try: conn.close()
    except: print('Error: Cannot close connection.')


def create_table(conn):
    c = conn.cursor()
    try: c.execute('''CREATE TABLE IF NOT EXISTS tasks
                     (id INTEGER PRIMARY KEY, 
                      task_name TEXT, 
                      completed BOOLEAN
                      )''')
    except:
        print('Error: Cannot create table.')
        return None
    
    conn.commit()
    print('Table created successfully.')

    disconnect(conn)

def insert_task(conn, task):
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, False))
    conn.commit()



import time as tm
import sqlite3
import io
import sys
import os

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file 
# by Nautilius, ballade4op52 -  2015, 2016
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Class responsible for facilitating the management of the SQLite database.
# It receives a connection to the database, a backup file name and a file name.
class TaskDataManager:
    # Private attributes
    __file_conn : str
    __backup_file : str
    __last_id : int

    # Constructor
    def __init__(self, file_conn : str = 'taskslist.db', backup_file : str = 'backup.sql'):
        self.__backup_file = backup_file
        self.__file_conn = file_conn
        self.__last_id = 1

        self.create_table() # Create the table if it doesn't exist.

    # Getters and Setters -----------------------------------------------------------------------------------
    @property
    def backup_file(self) -> str: return self.__backup_file
    @property
    def file_conn(self) -> str: return self.__file_conn
    @property
    def last_id(self) -> int: return self.__last_id

    @backup_file.setter
    def backup_file(self, new_backup_file : str): self.__backup_file = new_backup_file
    @file_conn.setter
    def file_conn(self, new_file_conn : str): self.__file_conn = new_file_conn


    # Private methods
    # This method will connect to the database, execute the block of code passed as a parameter, commit the changes and close the connection. 
    def __base_block(self, SQLcommand: str, values: tuple = None):
        try:
            with sqlite3.connect(resource_path(self.file_conn)) as conn: 
                c = conn.cursor()

                if values is None: c.execute(SQLcommand) # This condition is necessary to avoid errors when there are no parameters to be passed.
                else: c.execute(SQLcommand, values)
                tm.sleep(0.1)
                conn.commit()
        except sqlite3.Error as e: print('Error: Cannot execute the command.', e)


    # Public methods
    # Create a table in the database.
    def create_table(self, table_name: str = 'Tasks'):
        try:
            self.__base_block(f'''
                            CREATE TABLE IF NOT EXISTS {table_name}
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                            task_name TEXT NOT NULL, 
                            task_description TEXT,
                            completed BOOLEAN)
                            ''')
            print('Table created successfully.')                
        except sqlite3.Error as e: print(f'Error: Cannot create the table {table_name}.', e)


    # Insert a task into the database. This will be used when the user creates a new task.
    def insert_simple_task(self, task_name : str, task_description : str = ''):
        try:
            self.__base_block('INSERT INTO Tasks (task_name, task_description, completed) VALUES (?, ?, ?)', (task_name, task_description, False))
            print('Task inserted successfully.')
        except sqlite3.Error as e: print('Error: Cannot insert task.', e)


    # Delete task from the database by id.
    def delete_task(self, task_id: int):
        try:
            self.__base_block('DELETE FROM Tasks WHERE id = ?', (task_id,))
            print('Task deleted successfully.')
        except sqlite3.Error as e: print('Error: Cannot delete task.', e)


    # Update completed task status.
    def update_check_task(self, task_id: int, completed: bool):
        try:
            self.__base_block('UPDATE Tasks SET completed = ? WHERE id = ?', (completed, task_id))
            print('Task updated successfully.')
        except sqlite3.Error as e: print('Error: Cannot update task.', e)
    
    # Update task name and description.
    def update_task(self, task_id: int, task_name: str, task_description: str):
        try:
            self.__base_block('UPDATE Tasks SET task_name = ?, task_description = ? WHERE id = ?', (task_name, task_description, task_id))
            print('Task updated successfully.')
        except sqlite3.Error as e: print('Error: Cannot update task.', e)
      

    # Get all tasks from the database.
    def get_all_tasks(self) -> list:
        try:
            with sqlite3.connect(resource_path(self.file_conn)) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM Tasks;')
            return cursor.fetchall() 
        except sqlite3.Error as e: 
            print('Error: Cannot get all tasks.', e)
            return []


    # Backup/export and import data, but I haven't been able to use this.
    def export_data(self):
        try: 
            with io.open(self.__backup_file, 'w') as f: 
                for row in self.__conn.iterdump(): 
                    f.write('%s\n' % row)
            print('Data exported successfully.')
        except sqlite3.Error as e: print('Error: Cannot export data.', e)
        
    def import_data(self, table_name: str = 'Tasks'):
        try:
            self.drop_table(table_name) # Drop the table to avoid conflicts.

            conn = sqlite3.connect(resource_path(self.file_conn))
            cursor = conn.cursor()
            with io.open(self.__backup_file, 'r') as f: 
                cursor.executescript(f.read())
            conn.close()
            print('Data imported successfully.')
        except sqlite3.Error as e: 
            print('Error: Cannot import data.', e)

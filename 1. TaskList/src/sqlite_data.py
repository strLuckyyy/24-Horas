import io
import sqlite3


# Class responsible for facilitating the management of the SQLite database.
# It receives a connection to the database, a backup file name and a file name.
class TaskDataManager:
    # Attributes
    __conn : sqlite3.Connection
    __file_conn : str
    __backup_file : str

    # Constructor
    def __init__(self, file_conn : str = 'taskslist.db', backup_file : str = 'backup.sql'):
        self.__conn = sqlite3.connect(file_conn)
        self.__backup_file = backup_file
        self.__file_conn = file_conn    

    # Getters and Setters -----------------------------------------------------------------------------------
    @property
    def conn(self) -> sqlite3.Connection: return self.__conn
    @property
    def backup_file(self) -> str: return self.__backup_file
    @property
    def file_conn(self) -> str: return self.__file_conn

    # There’s no point in setting up the new connection; it could be dangerous. It’s safer to just set a new file name.
    @backup_file.setter
    def backup_file(self, new_backup_file : str): self.__backup_file = new_backup_file
    @file_conn.setter
    def file_conn(self, new_file_conn : str): self.__file_conn = new_file_conn


    # Private methods -----------------------------------------------------------------------------------------------        

    # This method will connect to the database, execute the block of code passed as a parameter, commit the changes and close the connection. 
    def __base_block(self, SQLcommand: str, values: tuple = None):
        try:
            with sqlite3.connect(self.file_conn) as conn: 
                c = conn.cursor()
                if values is None: c.execute(SQLcommand)
                else: c.execute(SQLcommand, values)
                self.__conn.commit()
        except sqlite3.Error as e: print('Error: Cannot execute the command.', e)

    # Public methods -----------------------------------------------------------------------------------------------
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

    # Drop a table from the database.
    def drop_table(self, table_name: str = 'Tasks'):
        try:
            self.__base_block(f'DROP TABLE IF EXISTS {table_name}')
            print('Table dropped successfully.')
        except sqlite3.Error as e: print(f'Error: Cannot drop table {table_name}.', e)


    # Insert a task into the database. This will be used when the user creates a new task.
    def insert_simple_task(self, task_name : str, task_description : str = ''):
        try:
            self.__base_block('INSERT INTO Tasks (task_name, task_description, completed) VALUES (?, ?, ?)', (task_name, task_description, False))
            print('Task inserted successfully.')
        except sqlite3.Error as e: print('Error: Cannot insert task.', e)

    # Insert multiple data into the database.
    def insert_task_list(self, tasks : tuple):
        try:
            with self.__connection() as conn:
                c = conn.cursor()
                c.executemany('INSERT INTO Tasks (task_name, task_description, completed) VALUES (?, ?, False)', tasks)
                conn.commit()
            print('Tasks inserted successfully.')
        except sqlite3.Error as e: print('Error: Cannot insert tasks.', e)


    # Delete task from the database by id.
    def delete_task(self, task_id: int):
        try:
            self.__base_block('DELETE FROM Tasks WHERE id = ?', (task_id,))
            print('Task deleted successfully.')
        except sqlite3.Error as e: print('Error: Cannot delete task.', e)
        
    # Delete all tasks from the database.
    def delete_all_tasks(self):
        try:
            self.__base_block('DELETE FROM Tasks WHERE id > 0')
            print('All tasks deleted successfully.')
        except sqlite3.Error as e: print('Error: Cannot delete tasks.', e)


    # I don't understand why I need to pass the self parameter here, but dosn't work without it...I hate python sometimes.
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
            with self.__connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM Tasks;')
                return cursor.fetchall()
        except sqlite3.Error as e: 
            print('Error: Cannot get all tasks.', e)
            return []


    # Backup/export and import data.
    def export_data(self):
        try: 
            with io.open(self.__backup_file, 'w') as f: 
                for row in self.__connection().iterdump(): 
                    f.write('%s\n' % row)
            print('Data exported successfully.')
        except sqlite3.Error as e: print('Error: Cannot export data.', e)
        
    def import_data(self, table_name: str = 'Tasks'):
        try:
            self.drop_table(table_name) # Drop the table to avoid conflicts.

            conn = self.__connection()
            cursor = conn.cursor()
            with io.open(self.__backup_file, 'r') as f: 
                cursor.executescript(f.read())
            conn.close()
            print('Data imported successfully.')
        except sqlite3.Error as e: 
            print('Error: Cannot import data.', e)
        

    # Show data in the console.
    def show_data_in_console(self):
        with self.__connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tasks;')
            for row in cursor.fetchall(): print(row)

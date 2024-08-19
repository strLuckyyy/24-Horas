from sqlite_data import TaskDataManager
from add_window import AddWindow
from task import Task
import flet as ft

class AppWindow(ft.Column):
    # Private attributes
    __id: int
    __sql: TaskDataManager
    __add_win: AddWindow

    __task_column: ft.Column
    __add_button: ft.Row
    __add_button_view: ft.Column

    # Constructor
    def __init__(self):
        # Initializing the attributes
        super().__init__()
        self.__sql = TaskDataManager("taskslist.db", "backup.sql")
        self.__id = self.__sql.last_id
        self.__add_win = AddWindow(self.save_task, self.cancel_task)
        
        self.__task_column = ft.Column()
        for task in self.__sql.get_all_tasks():
            self.__task_column.controls.append(Task(task[0], task[1], task[2], self.delete_task, task[3]))

        self.__add_button = self.__add_button_build()
        self.__add_button_view = self.__add_button_view_build()

        self.width = 600
        self.controls = [self.__task_column, self.__add_win, self.__add_button_view]
    
    # Private methods ------------------------------------------------------------
    # Build button to add a new task
    def __add_button_build(self) -> ft.Row:
        return ft.Row([
            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_task),
        ])

    def __add_button_view_build(self) -> ft.Column:
        return ft.Column([
            ft.Row([
                self.__add_button_build(),
            ], alignment=ft.MainAxisAlignment.END)
        ], alignment=ft.MainAxisAlignment.END)

    # Public event methods ----------------------------------------------------------
    def add_task(self, e):
        self.__add_button_view.visible = False
        self.__task_column.visible = False
        self.__add_win.visible = True
        self.update()

    def delete_task(self, task: Task):
        self.__task_column.controls.remove(task)
        self.update()

    def save_task(self, e):
        add_task_title = self.__add_win.task_title.value
        add_task_description = self.__add_win.task_description.value

        add_task_title = "Task Title" if add_task_title == "" else add_task_title
        add_task_description = "Task Description" if add_task_description == "" else add_task_description

        new_task = Task(self.__id, add_task_title, add_task_description, self.delete_task)
        self.__id += 1

        self.__task_column.controls.append(new_task)

        self.__task_column.visible = True
        self.__add_button_view.visible = True
        self.__add_win.visible = False

        self.__add_win.title_default()
        self.__add_win.description_default()

        self.__sql.insert_simple_task(add_task_title, add_task_description)
        self.update()

    def cancel_task(self, e):
        self.__task_column.visible = True
        self.__add_button_view.visible = True
        self.__add_win.visible = False

        self.update()

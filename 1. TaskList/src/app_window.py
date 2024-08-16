from sqlite_data import TaskDataManager as sql
from task import Task
import flet as ft

class AppWindow(ft.Column):
    # Private attributes
    __task_column: ft.Column

    __add_button: ft.Row
    __add_button_view: ft.Column

    __add_task_title: ft.TextField
    __add_task_description: ft.TextField
    __add_task_view: ft.Column

    # Constructor
    def __init__(self):
        # Initializing the attributes
        super().__init__()
        self.__task_column = ft.Column()
        for task in sql.get_all_tasks():
            self.__task_column.controls.append(Task(task[0], task[1], task[2], self.delete_task))        

        self.__add_button = self.__add_button_build()
        self.__add_button_view = self.__add_button_view_build()
        
        self.__add_task_title = ft.TextField(expand=1)
        self.__add_task_description = ft.TextField(expand=1)
        self.__add_task_view = self.__add_task_view_build()

        self.width = 600
        self.controls = [self.__task_column, self.__add_task_view, self.__add_button_view]
    
    # Private methods ------------------------------------------------------------
    # Build button to add a new task
    def __add_button_build(self) -> ft.Row:
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_task),
            ],
        )
    
    def __add_button_view_build(self) -> ft.Column:
        return ft.Column(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                self.__add_button_build(),
            ],
        )

    # Build the form to add a new task    
    def __add_task_view_build(self) -> ft.Column:
        return ft.Column(
            #visible=False,
            controls=[
                self.__add_task_title,
                self.__add_task_description,
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.SAVE_ALT_OUTLINED, tooltip='Save', on_click=self.save_task, data=0),
                        ft.IconButton(icon=ft.icons.CANCEL_OUTLINED, tooltip='Cancel', on_click=self.cancel_task),
                    ],
                ),
            ],
        )


    # Public event methods ----------------------------------------------------------
    def add_task(self, e):
        #self.__add_button_view.visible = False
        #self.__add_task_view.visible = True
        self.update()

    def delete_task(self, task):
        self.__task_column.controls.remove(task)
        self.update()

    def save_task(self, e):
        new_task = Task(e.data, self.__add_task_title.value, self.__add_task_description.value, self.delete_task)

        self.__task_column.controls.append(new_task)

        #self.__add_task_view.visible = False
        #self.__add_button_view.visible = True

        sql.insert_simple_task(self.__add_task_title.value, self.__add_task_description.value)

        e.data += 1
        self.update()

    def cancel_task(self, e):
        self.__add_task_title = ft.TextField(expand=1)
        self.__add_task_description = ft.TextField(expand=1)

        #self.__add_task_view.visible = False
        #self.__add_button_view.visible = True
        self.update()

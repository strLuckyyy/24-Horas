from sqlite_data import TaskDataManager
import flet as ft
import os

# This file contains the classes responsible for saving data when changes happen and for controlling the interface more easily.
class Task(ft.Column):
    # Private attributes 
    __sql: TaskDataManager
    __sql_id: int

    __task_title: str
    __task_description: str
    __display_task: ft.Column
    __display_view: ft.Row

    __edit_task_title: ft.TextField
    __edit_task_description: ft.TextField
    __edit_view: ft.Row

    __task_delete: any 
    # The attribute above will receive the task_delete(e) method from the TaskWindow class. This is necessary to delete the task from the window.

    # Constructor
    def __init__(self, task_id: int, task_title: str, task_description: str, task_delete: any):
        # Initializing the atributtes
        super().__init__()
        self.__sql = TaskDataManager()

        self.__sql_id = task_id

        self.__task_title = task_title
        self.__task_description = task_description
        self.__task_delete = task_delete

        self.__edit_task_title = ft.TextField(expand=1)
        self.__edit_task_description = ft.TextField(expand=1)
        self.__edit_view = self.__edit_view_build()

        self.__display_task = self.__display_task_build()
        self.__display_view = self.__display_view_build()

        self.controls = [self.__display_view, self.__edit_view]


    
    # Private methods ------------------------------------------------------------
    def __display_task_build(self) -> ft.Column: # Display build method. Putting the task's title and description in a column.
        return ft.Column(
            spacing=10,
            controls=[
                ft.Checkbox(label=self.__task_title, value=False, on_change=self.checked),
                ft.TextButton(self.__task_description, style=ft.ButtonStyle(color=ft.colors.WHITE)),
            ],
        )

    def __display_view_build(self) -> ft.Row:
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=150,
            controls=[
                self.__display_task,
                ft.Column(
                    controls=[
                        self.__icon_button(ft.icons.EDIT, "Edit", self.edit_task),
                        self.__icon_button(ft.icons.DELETE, "Delete", self.delete_task),
                    ],
                ),
            ],
        )
    
    def __edit_view_build(self) -> ft.Row:
        return ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=150,
            controls=[
                ft.Column(
                    controls=[
                        self.__edit_task_title,
                        self.__edit_task_description,
                    ],
                ),
                ft.Column(
                    controls=[
                        self.__icon_button(ft.icons.SAVE, "Save", self.save_task),
                        self.__icon_button(ft.icons.CANCEL, "Cancel", self.cancel_task),
                    ],
                ),
            ],
        )
    
    def __icon_button(self, _icon: str, _tooltip: str, _on_click: any) -> ft.IconButton:
        return ft.IconButton(icon=_icon, tooltip=_tooltip, icon_size=20, width=30, height=30, on_click=_on_click)

    # Public event methods ----------------------------------------------------------
    
    # In theory, these methods are working. I'll test them later.
    # These methods are supposed to update the task's status in the database.

    def checked(self, e):
        self.__sql.update_check_task(self.__sql_id, self.__display_task.controls[0].value)
        self.update()

    def edit_task(self, e):
        self.__edit_task_title.value = self.__display_task.controls[0].label
        self.__edit_task_description.value = self.__display_task.controls[1].text

        self.__display_view.visible = False
        self.__edit_view.visible = True
        self.update()

    def delete_task(self, e):
        self.__sql.delete_task(self.__sql_id)
        self.__task_delete(self)

    def save_task(self, e):
        self.__display_task.controls[0].label = self.__edit_task_title.value
        self.__display_task.controls[1].text = self.__edit_task_description.value

        self.__display_view.visible = True
        self.__edit_view.visible = False

        self.__sql.update_task(self.__sql_id, self.__edit_task_title.value, self.__edit_task_description.value)

        self.update()

    def cancel_task(self, e):
        self.__edit_task_title = ft.TextField(expand=1)
        self.__edit_task_description = ft.TextField(expand=1)

        self.__display_view.visible = True
        self.__edit_view.visible = False
        self.update()
        

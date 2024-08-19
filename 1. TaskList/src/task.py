from sqlite_data import TaskDataManager
from add_window import AddWindow
import flet as ft
import os


# This class is used to build the task block.
class Task(ft.Column):
    # Private attributes 
    __sql: TaskDataManager
    __sql_id: int
    __checked: bool

    __task_title: str
    __task_description: str
    __display_task: ft.Column
    __display_view: ft.Row

    __edit_task_title: str
    __edit_task_description: str
    __edit_view: ft.Row

    __task_delete: any 
    # The attribute above will receive the task_delete(e) method from the TaskWindow class. This is necessary for deleting the task from the window.

    # Constructor
    def __init__(self, task_id: int, task_title: str, task_description: str, task_delete: any, checked: bool = False):
        super().__init__()
        self.__sql = TaskDataManager() # Instance of the TaskDataManager class
        self.__sql_id = task_id

        self.__task_title = task_title
        self.__task_description = task_description
        self.__task_delete = task_delete
        self.__checked = bool(checked) # This is necessary to convert the value to a boolean in case it is an integer.

        self.__edit_task_title = ""
        self.__edit_task_description = ""
        self.__edit_view = self.__edit_view_build()

        self.__display_task = self.__display_task_build()
        self.__display_view = ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.AMBER_800,
            width=500,
            height=100,
            border_radius=10,
            content=self.__display_view_build()
        )

        self.controls = [self.__display_view, self.__edit_view]
    
    # Private methods 
    def __display_task_build(self) -> ft.Column: # Display build method. This method arranges the task's title and description in a column.
        return ft.Column(
            spacing=10,
            controls=[
                ft.Checkbox(
                    label=self.__task_title, 
                    value=self.__checked, 
                    on_change=self.checked, 
                    label_style=ft.TextStyle(color=ft.colors.BLACK), 
                    check_color=ft.colors.BLACK
                    ),
                ft.Text(self.__task_description, color=ft.colors.BLACK),
            ],
        )

    def __display_view_build(self) -> ft.Row: # Display view build method. This method arranges the task's display and buttons in a row.
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
    
    def __edit_view_build(self) -> ft.Row: # Edit view build method. This method arranges the task's edit form and buttons in a row.     
        def text(text: str) -> ft.TextField:
            return ft.TextField(
                hint_text=text, 
                width=200, 
                height=40, 
                text_size=12,
                )
        
        display = ft.Row([
            ft.Column([
                text("Task Title"),
                text("Task Description"),
            ]),
            ft.Column([
                ft.IconButton(icon=ft.icons.SAVE, on_click=self.save_task),
                ft.IconButton(icon=ft.icons.CANCEL, on_click=self.cancel_task)
            ])
        ], 
        alignment=ft.MainAxisAlignment.CENTER, 
        visible=False)

        return display
    
    def __icon_button(self, _icon: str, _tooltip: str, _on_click: any) -> ft.IconButton:
        return ft.IconButton(icon=_icon, tooltip=_tooltip, icon_size=22, width=30, height=30, on_click=_on_click, icon_color=ft.colors.BLACK)

    # Public event methods
    def checked(self, e): 
        self.__sql.update_check_task(self.__sql_id, self.__display_task.controls[0].value)
        self.update()

    def edit_task(self, e):
        self.__display_view.visible = False
        self.__edit_view.visible = True
        self.update()

    def delete_task(self, e):
        self.__sql.delete_task(self.__sql_id)
        self.__task_delete(self)
        self.update()

    def save_task(self, e):
        self.__display_task.controls[0].label = self.__edit_view.controls[0].controls[0].value
        self.__display_task.controls[1].value = self.__edit_view.controls[0].controls[1].value

        title = self.__display_task.controls[0].label
        description = self.__display_task.controls[1].value

        self.__display_view.visible = True
        self.__edit_view.visible = False

        self.__sql.update_task(self.__sql_id, title, description)
        self.update()

    def cancel_task(self, e):
        self.__edit_task_title = ft.TextField(expand=1)
        self.__edit_task_description = ft.TextField(expand=1)

        self.__display_view.visible = True
        self.__edit_view.visible = False
        self.update()
        

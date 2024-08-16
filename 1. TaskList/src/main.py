from sqlite_data import TaskDataManager
from app_window import AppWindow
from task import Task
import flet as ft
import os

#
# About the classes:

# - Task: class that will reference the task card [FIXME]

# - AppWindow: class that will reference the window that will contain the tasks [FIXME]

# - AddWindow: class that will reference the window that will contain the form to add a new task [TODO]

# - TaskDataManager: class that will reference the class that will manage the tasks in the database [x]

#

# NOTE:(04:40 AM - 16/08/24) I did complete 77% of the goal. So, maybe I let this project unfinished.

def main(page: ft.Page):
    page.title = "Task App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()


    # add application's root control to the page
    page.add()

if __name__ == "__main__":
    ft.app(main)


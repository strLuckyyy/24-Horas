from sqlite_data import TaskDataManager
from app_window import AppWindow
from task import Task
import flet as ft
import os

#
# About the classes:
# - Task: This class is used to build the task block.
#
# - AppWindow: This class is used to build the window that will contain the tasks. 
#
# - AddWindow: This class is used to reference the window that will contain the form to add a new task.
#
# - TaskDataManager: Class that manages the tasks in the database.
#

# Main function
def main(page: ft.Page):
    page.title = "Orange Task App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # Instance of the AppWindow class
    taskApp = AppWindow()

    # Add application's root control to the page
    page.add(taskApp)

if __name__ == "__main__":
    ft.app(main)

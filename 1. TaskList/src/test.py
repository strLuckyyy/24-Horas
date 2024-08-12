import flet as ft
from window.task_window import TaskWindow as tw

#
# this file is just for testing purposes.
#

def main(page: ft.Page):
    tw(page, 'Task Manager')

ft.app(main)
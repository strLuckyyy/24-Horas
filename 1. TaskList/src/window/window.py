__package__ = 'window'

import flet as ft

# Class responsible for creating and managing the window.
class FletWindow(ft.Page):
    # Attributes
    __width : int
    __height : int

    # Constructor
    def __init__(self, window_title: str = "Tasks", window_width: int = 800, window_height: int = 600):
        super().__init__()
        self.title = window_title
        self.__width = window_width
        self.__height = window_height

    

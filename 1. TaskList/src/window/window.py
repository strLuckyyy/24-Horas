__package__ = 'window'

import tkinter as tk

class Window(tk.Tk):
    def __init__(self, title: str = "Exemplo Tkinter", length: int = 400, height: int = 300):
        super().__init__()
        self.title(title)
        self.geometry(f"{length}x{height}")


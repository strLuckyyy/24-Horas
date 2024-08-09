from com.window.window import Window
import tkinter as tk
import os

def debug(msg: str = "Hello, World!"):
    print(msg)

if __name__ == "__main__":
    win = Window("Task List", 800, 600)

    btn = tk.Button(win, text="Clique aqui", command=debug)
    btn.pack(pady=20)

    win.mainloop()

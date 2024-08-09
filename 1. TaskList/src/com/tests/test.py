import tkinter as tk

def say_hello():
    print("Hello, World!")

root = tk.Tk()
root.title("Exemplo Tkinter")

btn = tk.Button(root, text="Clique aqui", command=say_hello)
btn.pack(pady=20)

root.mainloop()

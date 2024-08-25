import tkinter as tk

def quit(root):
    root.destroy()

root = tk.Tk()
tk.Button(root, text="Quit", command=lambda root=root:quit(root)).pack()
root.mainloop()
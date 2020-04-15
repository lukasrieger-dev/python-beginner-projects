import tkinter as tk
from tkinter import ttk

__author__ = 'Codinglukas'


def greet():
    """
    Prints the greeting to the console.
    If nothing was entered for the user name, it will take 'World' instead.
    """
    print(f"Hi, welcome to Tkinter, {user_name.get() or 'World'}!")


root = tk.Tk()
root.geometry("600x40")

# in this variable we store the input
user_name = tk.StringVar()

name_label = ttk.Label(root, text="Your Name: ")
name_label.pack(side="left", padx=(12, 12))

name_entry = ttk.Entry(root, width=20, textvariable=user_name)
name_entry.pack(side="left")
# set focus to the input field
name_entry.focus()


greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left")

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right")

root.mainloop()






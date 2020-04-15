import tkinter as tk
from tkinter import ttk


def convert_meters_to_feet():
    m_str = input_value.get() or '0'
    try:
        m = float(m_str)
        feet = 3.28084 * m
        msg = f'{feet:.2f}'
    except ValueError:
        msg = 'Invalid input'
    output_value.set(msg)


root = tk.Tk()
root.title("Unit Converter")

# in this variable we store the input
input_value = tk.StringVar()
output_value = tk.StringVar()

main = ttk.Frame(root, padding=(30, 50))
main.grid()

meters_label = ttk.Label(main, text="Meters:")
meters_input = ttk.Entry(main, width=10, textvariable=input_value)
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, text="Feet output", textvariable=output_value)
calc_button = ttk.Button(main, text="Convert", command=convert_meters_to_feet)
quit_button = ttk.Button(main, text="Quit", command=root.destroy)

meters_label.grid(column=0, row=0, sticky="W")
meters_input.grid(column=1, row=0, sticky="EW")
meters_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
quit_button.grid(column=0, row=3, columnspan=2, sticky="EW")

root.mainloop()

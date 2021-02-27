from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(feet.get())
        res = (value) / 100.0
        meters.set(f'{res:.2f}')
    except ValueError:
        pass


root = Tk()
root.title("Centimeters to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(
    column=3, row=3, sticky=W
)

ttk.Label(mainframe, text="cm").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()

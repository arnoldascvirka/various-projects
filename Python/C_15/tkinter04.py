import tkinter as tk

from sqlalchemy import column

window1 = tk.Tk()


def printer():
    entered = space1.get()
    result1["text"] = entered


written1 = tk.Label(window1, text="Enter text: ")
space1 = tk.Entry(window1)
button1 = tk.Button(window1, text="Enter", command=printer)
result1 = tk.Label(window1, text="")

written1.grid(row=0, column=0)
space1.grid(row=0, column=1)
button1.grid(row=0, column=2)
result1.grid(row=0, column=3)

window1.mainloop()

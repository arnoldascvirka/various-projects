import tkinter as tk
from turtle import width

window1 = tk.Tk()

ekr_width = window1.winfo_screenwidth()
ekr_heigth = window1.winfo_screenheight()

window1.geometry(f"{ekr_width // 2}x{ekr_heigth // 2}")

upper = tk.Frame(window1, width=300, height=200)
lower = tk.Frame(window1, width=300, height=200)

button1 = tk.Button(upper, text="1 button")
button2 = tk.Button(upper, text="2 button")
button3 = tk.Button(lower, text="3 button")
button4 = tk.Button(lower, text="4 button")

upper.pack(side=tk.TOP)
lower.pack(side=tk.BOTTOM)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.RIGHT)
button4.pack(side=tk.RIGHT)


window1.mainloop()

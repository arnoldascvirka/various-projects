import tkinter as tk

window1 = tk.Tk()


ekr_width = window1.winfo_screenwidth()
ekr_heigth = window1.winfo_screenheight()

window1.geometry(f"{ekr_width // 2}x{ekr_heigth // 2}")

line1 = tk.Label(window1, text="Hello Tkinter!")
line1.pack()

window1.mainloop()

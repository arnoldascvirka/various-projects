import tkinter as tk

window1 = tk.Tk()

ekr_width = window1.winfo_screenwidth()
ekr_heigth = window1.winfo_screenheight()
window1.geometry("200x100")


def printer(event=None):
    entered = "Labas", space1.get()
    result1["text"] = entered


written1 = tk.Label(window1, text="Enter name: ")
space1 = tk.Entry(window1)
button1 = tk.Button(window1, text="Enter", command=printer)
result1 = tk.Label(window1, text="")

window1.bind("<Return>", printer)
written1.pack()
space1.pack()
button1.pack()
result1.pack()

window1.mainloop()

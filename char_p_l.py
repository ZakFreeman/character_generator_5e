from tkinter import *
from tkinter import ttk

def otherProfs(frame, col, row, name):
    lbl_name = Label(frame, text=name)
    lbl_name.grid(column=col, row=row)
    txt_prof = Text(
        frame,
        height=3,
        width=20
        )
    txt_prof.grid(column=col, row=row+1, padx=5, pady=5)
    return txt_prof
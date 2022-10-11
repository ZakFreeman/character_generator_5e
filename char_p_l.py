from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def otherProfs(frame, col, row, name):
    lbl_name = Label(frame, text=name)
    lbl_name.grid(column=col, row=row+1)
    txt_prof = ScrolledText(
        frame,
        height=3,
        width=15,
        wrap=WORD,
        )
    txt_prof.grid(column=col, row=row+2, padx=5, pady=5)

    return txt_prof
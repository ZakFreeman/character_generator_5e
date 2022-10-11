from tkinter import *
from tkinter import ttk

def equipEntry(frame, row):
    ent_list = []
    ent_item = Entry(frame, width=35)
    ent_item.grid(column=0, row=row+2, padx=2, pady=2)
    ent_list.append(ent_item)
    ent_weight = Entry(frame, width=6)
    ent_weight.grid(column=1, row=row+2)
    ent_list.append(ent_weight)
    ent_worth = Entry(frame, width=8)
    ent_worth.grid(column=2, row=row+2)
    ent_list.append(ent_worth)
    return ent_list
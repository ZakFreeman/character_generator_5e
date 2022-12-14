from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def invEntry(frame, row):
    """Create the entry fields used to represent character equipment."""
    ent_list = []
    ent_item = Entry(frame, width=32)
    ent_item.grid(column=0, row=row+2, padx=2, pady=2)
    ent_list.append(ent_item)
    ent_weight = Entry(frame, width=6)
    ent_weight.grid(column=1, row=row+2, padx=2)
    ent_list.append(ent_weight)
    ent_worth = Entry(frame, width=8)
    ent_worth.grid(column=2, row=row+2, padx=2)
    ent_list.append(ent_worth)
    return ent_list

def otherProfs(frame, col, row, name):
    """Create the Text objects representing other Proficiencies and Languages."""
    lbl_name = Label(frame, text=name)
    lbl_name.grid(column=col, row=row+1)
    txt_prof = ScrolledText(
        frame,
        height=3,
        width=25,
        wrap=WORD,
        )
    txt_prof.grid(column=col, row=row+2, padx=5, pady=5)
    return txt_prof


def deathSave(frame, type, row):
    """Create the objects representing death saving throws."""
    lbl_saveType = Label(frame, text=type)
    lbl_saveType.grid(column=0, row=row, columnspan=3, padx=5)
    bvList = []
    for i in range(3):
        bv = BooleanVar()
        chk = ttk.Checkbutton(frame, variable=bv)
        chk.grid(column=i, row=row+1)
        bvList.append(bv)
    return bvList


def wealth(frame, coin, col):
    """Create the money information box."""
    coinList = []
    lbl_coin = Label(frame, text=coin, font='helvetica 12')
    lbl_coin.grid(column=col, row=0)
    coinList.append(lbl_coin)
    ent_coin = Entry(frame, width=8)
    ent_coin.grid(column=col, row=1, padx=5, pady=5)
    coinList.append(ent_coin)
    return coinList
from tkinter import *
from tkinter import ttk

padding = {'padx': 5, 'pady': 5}

def statEntry(stat, col, row, window, frame):
    """Creates the frames and Entry objects for the various stats of a character.
    Returns the Entry Field object or Checkbutton object"""
    frm_stat = ttk.Frame(
        frame,
        borderwidth=5,
        relief=GROOVE,
      )
    frm_stat.grid(column=col, row=row, **padding, sticky='NWES')
    lbl_stat = Label(frm_stat, text=stat)
    lbl_stat.grid(column=col, row=row, **padding)
    if stat == 'INSPIRATION':
        chkVar = BooleanVar()
        chk_stat = ttk.Checkbutton(frm_stat, variable=chkVar, text='Advantage')
        chk_stat.grid(column=col, row=row+1)
        return chkVar
    vcmd = (window.register(statValidate), '%P')
    ent_stat = Entry(
        frm_stat,
        width=4,
        validate='key',
        validatecommand=vcmd
    )
    ent_stat.grid(column=col, row=row+1, **padding, sticky='N')
    return ent_stat

def statValidate(P):
    """Validate inputs for the stat objects. Takes Digits only."""
    if len(P) == 0 or (len(P) > 0 and P.isdigit()):
        return True
    else:
        return False

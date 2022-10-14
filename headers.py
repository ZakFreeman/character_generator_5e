from tkinter import *
from tkinter import ttk

padding = {'padx':5, 'pady':5}

def abilHeader(frame):
    """Create the top portion of the ability frame."""
    lbl_abilHeader = Label(frame, text='Ability', font='helvetica 12')
    lbl_abilHeader.grid(column=0, row=0, padx=2)
    lbl_abilScoreHeader = Label(frame, text='Score', font='helvetica 12')
    lbl_abilScoreHeader.grid(column=1, row=0, padx=2)
    lbl_abilModHeader = Label(frame, text='Bonus', font='helvetica 12')
    lbl_abilModHeader.grid(column=2, row=0, padx=2)
    lbl_saveHeader = Label(frame, text='Save', font='helvetica 12')
    lbl_saveHeader.grid(column=4, row=0, padx=2, sticky='E')


def skillHeader(frame):
    """Create the top portion of the skills frame."""
    lbl_pHeader = Label(frame, text='Prof', font='helvetica 12')
    lbl_pHeader.grid(column=0, row=0, padx=5)
    lbl_mHeader = Label(frame, text='Mod', font='helvetica 12')
    lbl_mHeader.grid(column=1, row=0, padx=5)
    lbl_sHeader = Label(frame, text="Skill", font='helvetica 12')
    lbl_sHeader.grid(column=2, row=0, padx=5, sticky='W')
    lbl_bHeader = Label(frame, text='Bonus', font='helvetica 12')
    lbl_bHeader.grid(column=3, row=0, padx=5, sticky='E')

def profHeader(frame):
    """Create the top portion of the Proficiencies and Languages frame."""
    lbl_pHead = Label(frame, text='Proficiencies & Languages', font='helvetica 12')
    lbl_pHead.grid(column=0, row=0)

def invHeader(frame):
    """Create the top portion of the Inventory frame."""
    lbl_iHead = Label(frame, text='Inventory', font='helvetica 12')
    lbl_iHead.grid(column=0, row=0, sticky='N', columnspan=3)
    lbl_item = Label(frame, text='Item')
    lbl_item.grid(column=0, row=1)
    lbl_weight = Label(frame, text='Weight')
    lbl_weight.grid(column=1, row=1)
    lbl_worth = Label(frame, text='Worth')
    lbl_worth.grid(column=2, row=1)

def dSaveHeader(frame):
    """Create the top portion of the Death Saves frame."""
    lbl_dsaves = Label(frame, text='Death Saves', font='helvetica 12')
    lbl_dsaves.grid(column=0, row=0, padx=5, columnspan=3, sticky='W')

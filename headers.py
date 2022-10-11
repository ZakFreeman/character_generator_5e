from tkinter import *
from tkinter import ttk

padding = {'padx':5, 'pady':5}

def abilHeader(frame):
    hFrame = ttk.Frame(frame, borderwidth=5, relief=GROOVE)
    hFrame.grid(column=0, row=1, padx=5, pady=(5,0), sticky='WE')
    lbl_abilHeader = Label(hFrame, text='Ability')
    lbl_abilHeader.grid(column=0, row=0, padx=2)
    lbl_abilScoreHeader = Label(hFrame, text='Score')
    lbl_abilScoreHeader.grid(column=1, row=0, padx=2)
    lbl_abilModHeader = Label(hFrame, text='Mod')
    lbl_abilModHeader.grid(column=2, row=0, padx=2)
    lbl_saveHeader = Label(hFrame, text='Save')
    lbl_saveHeader.grid(column=3, row=0, padx=2)


def skillHeader(frame):
    hFrame = ttk.Frame(frame, borderwidth=5, relief=GROOVE)
    hFrame.grid(column=1, row=1, padx=5, pady=(5,0), sticky='WE')
    lbl_pHeader = Label(hFrame, text='Prof')
    lbl_pHeader.grid(column=0, row=0, padx=5)
    lbl_mHeader = Label(hFrame, text='Mod')
    lbl_mHeader.grid(column=1, row=0, padx=5)
    lbl_sHeader = Label(hFrame, text="Skill")
    lbl_sHeader.grid(column=2, row=0, padx=5)
    lbl_bHeader = Label(hFrame, text='Bonus')
    lbl_bHeader.grid(column=3, row=0, padx=5, sticky='E')

def profHeader(frame):
    lbl_pHead = Label(frame, text='Proficiencies & Languages')
    lbl_pHead.grid(column=0, row=0)
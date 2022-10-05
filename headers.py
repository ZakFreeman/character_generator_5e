from tkinter import *
from tkinter import ttk
def abilHeader(frame):
    lbl_abilHeader = Label(frame, text='Ability')
    lbl_abilHeader.grid(column=0, row=0, padx=2)
    lbl_abilScoreHeader = Label(frame, text='Score')
    lbl_abilScoreHeader.grid(column=1, row=0, padx=2)
    lbl_abilModHeader = Label(frame, text='Mod')
    lbl_abilModHeader.grid(column=2, row=0, padx=2)


def skillHeader(frame):
    lbl_pHeader = Label(frame, text='Prof')
    lbl_pHeader.grid(column=0, row=0, padx=5)
    lbl_mHeader = Label(frame, text='Mod')
    lbl_mHeader.grid(column=1, row=0, padx=5, sticky='W')
    lbl_sHeader = Label(frame, text="Skill")
    lbl_sHeader.grid(column=2, row=0, padx=5, sticky='W')
    lbl_bHeader = Label(frame, text='Bonus')
    lbl_bHeader.grid(column=3, row=0, padx=5, sticky='E')

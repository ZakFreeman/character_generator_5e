from tkinter import *
from tkinter import ttk

padding = {'padx':5, 'pady':5}

def abilHeader(frame):
    lbl_abilHeader = Label(frame, text='Ability')
    lbl_abilHeader.grid(column=0, row=0, padx=2)
    lbl_abilScoreHeader = Label(frame, text='Score')
    lbl_abilScoreHeader.grid(column=1, row=0, padx=2)
    lbl_abilModHeader = Label(frame, text='Bonus')
    lbl_abilModHeader.grid(column=2, row=0, padx=2)
    lbl_saveHeader = Label(frame, text='Save')
    lbl_saveHeader.grid(column=4, row=0, padx=2, sticky='E')


def skillHeader(frame):
    lbl_pHeader = Label(frame, text='Prof')
    lbl_pHeader.grid(column=0, row=0, padx=5)
    lbl_mHeader = Label(frame, text='Mod')
    lbl_mHeader.grid(column=1, row=0, padx=5)
    lbl_sHeader = Label(frame, text="Skill")
    lbl_sHeader.grid(column=2, row=0, padx=5)
    lbl_bHeader = Label(frame, text='Bonus')
    lbl_bHeader.grid(column=3, row=0, padx=5, sticky='E')

def profHeader(frame):
    lbl_pHead = Label(frame, text='Proficiencies & Languages')
    lbl_pHead.grid(column=0, row=0)

def equipHeader(frame):
    lbl_iHead = Label(frame, text='Inventory')
    lbl_iHead.grid(column=0, row=0, sticky='N', columnspan=3)
    lbl_item = Label(frame, text='Item')
    lbl_item.grid(column=0, row=1)
    lbl_weight = Label(frame, text='Weight')
    lbl_weight.grid(column=1, row=1)
    lbl_worth = Label(frame, text='Worth')
    lbl_worth.grid(column=2, row=1)

def dSaveHeader(frame):
    lbl_dsaves = Label(frame, text='Death Saves')
    lbl_dsaves.grid(column=0, row=0, padx=5, columnspan=3, sticky='W')
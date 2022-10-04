from calendar import setfirstweekday
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Gui Practice")

padding = {'padx': 5, 'pady': 5}

mainframe = ttk.Frame(window, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky="nsew")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frm_basicInfo = ttk.Frame(
    mainframe,
    borderwidth=5,
    relief=GROOVE
)
frm_basicInfo.grid(column=0, row=0)  # Might need a columnspan=3|6

def basicInfoEntry(lbl_name, column, row):
    """Make a basic Label: entry structure. """
    lbl_className = ttk.Label(frm_basicInfo, text=str(lbl_name))
    lbl_className.grid(column=column, row=row, **padding, sticky="W")

    classNameVar = StringVar()
    ent_className = ttk.Entry(frm_basicInfo, textvariable=classNameVar)
    ent_className.grid(column=column+1, row=row, **padding, sticky="W")

basicInfoEntry("Name:", 0, 0)
basicInfoEntry("Class:", 0, 1)
basicInfoEntry("Race:", 2, 0)
basicInfoEntry("Level:", 2, 1)
basicInfoEntry("Alignment:", 4, 0)
basicInfoEntry("Background:", 4, 1)
frm_abilities = ttk.Frame(
    mainframe,
    borderwidth=5, 
    relief=GROOVE
    )
frm_abilities.grid(column=0, row=1, pady=5, sticky="W")  # Might need columnspan=2

for i in range(6):
    abilityEntry = Entry(frm_abilities, width=3)
    abilityEntry.grid(row=i, **padding)
window.mainloop()

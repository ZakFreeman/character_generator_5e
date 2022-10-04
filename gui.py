from __future__ import absolute_import
from tkinter import *
from tkinter import ttk


ABILITY_NAMES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']


def basicInfoEntry(lbl_name, column, row):
    """Make a basic Label: entry structure. Pass the name of the label, then
    position of column and row for the grid."""
    lbl_labelName = ttk.Label(frm_basicInfo, text=lbl_name)
    lbl_labelName.grid(column=column, row=row, **padding, sticky="W")
    # The StringVar() class can be used to track changes in entry fields.
    ent_string_var = StringVar()
    ent_entryName = ttk.Entry(frm_basicInfo, textvariable=str(ent_string_var))
    ent_entryName.grid(column=column+1, row=row, **padding, sticky="W")
    
    return ent_string_var


def abilityEntry(abilityName, row):
    """Generate a StringVar to hold an abilities text entry."""
    ent_ability_var = StringVar()
    lbl_ability = Label(frm_abilities, text=f'{abilityName}:')
    lbl_ability.grid(row=row)
    ent_ability = Entry(frm_abilities, width=3, textvariable=ent_ability_var)
    ent_ability.grid(row=row, column=1, **padding)

    return ent_ability_var

def strCallback(*args):
    """These all do the same thing, couldn't figure out a way to pass an index in a 
    list. Hardcoded this for the time being."""
    print(charStr_var.get())

def dexCallback(*args):
    print(charDex_var.get())

def conCallback(*args):
    print(charCon_var.get())

def intCallback(*args):
    print(charInt_var.get())

def wisCallback(*args):
    print(charWis_var.get())

def chaCallback(*args):
    print(charCha_var.get())

'''
def generateAblityModifier(baseScore):
    """Called to generate the modifier for a given ability score, baseScore."""
    abilityModifier = -5
    abilityScoreTable = 0
    while abilityScoreTable < 30:
            if baseScore == abilityScoreTable or baseScore == (abilityScoreTable + 1):
                break
            abilityScoreTable += 2
            abilityModifier += 1
    return abilityModifier
'''

window = Tk()
window.title("Character Sheet")

# Basic 5x5 padding to pass.
padding = {'padx': 5, 'pady': 5}

mainframe = ttk.Frame(window, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky="nsew")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Create a frame for basic character information.
frm_basicInfo = ttk.Frame(
    mainframe,
    borderwidth=5,
    relief=GROOVE
)
frm_basicInfo.grid(column=0, row=0)  # Might need a columnspan=3|6?

# Create all of the basic information for a new character, place at top of screen.
charName_var = basicInfoEntry("Name:", 0, 0)
charClass_var = basicInfoEntry("Class:", 0, 1)
charRace_var = basicInfoEntry("Race:", 2, 0)
charLevel_var = basicInfoEntry("Level:", 2, 1)
charAlign_var = basicInfoEntry("Alignment:", 4, 0)
charBg_var = basicInfoEntry("Background:", 4, 1)

# Make the frame for ability scores, modifiers, and saving throws.
frm_abilities = ttk.Frame(
    mainframe,
    borderwidth=5, 
    relief=GROOVE
    )
frm_abilities.grid(column=0, row=1, pady=5, sticky="W")  # Might need columnspan=2?

# Generate entry fields and labels for a given ability. Messy, got stuck.
# Couldn't loop because of .trace() on the StringVar's being returned from 
# abilityEntry().
charStr_var = abilityEntry(ABILITY_NAMES[0], 0)
charStr_var.trace('w', strCallback)
charDex_var = abilityEntry(ABILITY_NAMES[1], 1)
charDex_var.trace('w', dexCallback)
charCon_var = abilityEntry(ABILITY_NAMES[2], 2)
charCon_var.trace('w', conCallback)
charInt_var = abilityEntry(ABILITY_NAMES[3], 3)
charInt_var.trace('w', intCallback)
charWis_var = abilityEntry(ABILITY_NAMES[4], 4)
charWis_var.trace('w', wisCallback)
charCha_var = abilityEntry(ABILITY_NAMES[5], 5)
charCha_var.trace('w', chaCallback)


def handle_button():
    print()

button = ttk.Button(text="Print values", command=handle_button)
button.grid(column=1, row=1, **padding)

window.mainloop()

from __future__ import absolute_import
from tkinter import *
from tkinter import ttk


ABILITY_NAMES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']


def generateAblityModifier(baseScore):
    """Called to generate the modifier for a given ability score, baseScore. Takes 
    a StringVar, so need to convert that to an int, then process it."""
    mod_var = StringVar()
    # Return 0 if an entry field is blank.
    if baseScore == '':
        mod_var.set('0')
        return mod_var
    # Math for calculating the ability modifier, from 0->30
    baseScore = int(baseScore)
    abilityModifier = -5
    abilityScoreTable = 0
    while abilityScoreTable < 30:
        if baseScore == abilityScoreTable or baseScore == (abilityScoreTable + 1):
            break
        abilityScoreTable += 2
        abilityModifier += 1
    # Make the modifier a str again, to assign it to a Label.
    mod_var.set(str(abilityModifier))
    return mod_var


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


def abilCallback(*args):
    """Called when .trace() is used in one of the ability score fields."""
    for i in range(len(abilList)):
        abilCallbackHandler(abilList[i], i)


def abilCallbackHandler(abilStrVar, row):
    """Handles argument input for the .trace() callback for ability score fields.
    Dynamically creates the labels showing ability score modifiers."""
    strVar = generateAblityModifier(abilStrVar.get())
    lbl_mod = Label(frm_abilities, textvariable=strVar)
    lbl_mod.grid(column=2, row=row)


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
basicInfoDict = {}
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

# Create a list holding the StringVar objects with the ability scores inside them.
abilList = []
for row, abil in enumerate(ABILITY_NAMES):
    abilList.append(abilityEntry(abil, row))

# Generate the modifiers for the ability scores using .trace() 
for i in range(len(abilList)):
    abilList[i].trace('w', abilCallback)


def handle_button():
    print(abilList[0].get())

button = ttk.Button(text="Print values", command=handle_button)
button.grid(column=1, row=1, **padding)

window.mainloop()

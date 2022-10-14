import json
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def saveButton(savedDicts):
    """Calls functions to handle the dictionaries passed from the save button call.
    The dictionaries are all different, and need to be handled a few different
    ways."""
    saveNamesList = []  # Used to pass names for file generation.
    for name in savedDicts:
        saveNamesList.append(name)
    labelEntrySave(savedDicts[saveNamesList[0]], saveNamesList[0])  # Basic
    labelMulEntrySave(savedDicts[saveNamesList[1]], saveNamesList[1])  # Saves
    abilitySave(savedDicts[saveNamesList[2]], saveNamesList[2])  # Abilities
    labelEntrySave(savedDicts[saveNamesList[3]], saveNamesList[3])  # Skills
    statSave(savedDicts[saveNamesList[4]], saveNamesList[4])  # Stats
    statSave(savedDicts[saveNamesList[5]], saveNamesList[5])  # Proficiencies
    labelMulEntrySave(savedDicts[saveNamesList[6]], saveNamesList[6])  # Inventory
    labelEntrySave(savedDicts[saveNamesList[7]], saveNamesList[7])  # Money


def abilitySave(dict, name):
    """Hardcoded ability score function to handle the checkboxes."""
    with open(f'saveData/{name}.txt', 'w') as f:
        abils = {}  # Remake dict as {Label : [Entry, BooleanVar]}
        for ability in dict:
            vList = []
            vList.append(dict[ability][1].get())
            vList.append(dict[ability][3].get())
            abils[ability] = vList
        jabils = json.dumps(abils)
        f.write(jabils)
    

def labelEntrySave(dict, name):
    """Handles save data generation for dictionaries that contain a label, 
    then Entry."""
    with open(f'saveData/{name}.txt', 'w') as f:
        basicInfo = {}  # Remake dict as {Label : Entry.get()}
        for label in dict:
            if isinstance(dict[label][0], BooleanVar):  # Handles skills
                basicInfo[label] = dict[label][0].get()
            else:
                basicInfo[label] = dict[label][1].get()
        jbasic = json.dumps(basicInfo)
        f.write(jbasic)
    return jbasic


def labelMulEntrySave(dict, name):
    """Handles save data dictionaries with a list for the value."""
    with open(f'saveData/{name}.txt', 'w') as f:
        mulEntry = {}  # Remake dict as {Label : [List of values]}
        for label in dict:  # Keys
            vList = []
            for chk in dict[label]:  # Multiple values
                vList.append(chk.get())
            mulEntry[label] = vList
        jMul = json.dumps(mulEntry)
        f.write(jMul)
    return jMul


def statSave(dict, name):
    """Handles save data for stats, and for the proficiencies text boxes."""
    with open(f'saveData/{name}.txt', 'w') as f:
        statInfo = {}  # Remake dict as {Label : Entry.get() or Checkbutton.get()}
        for stat in dict:
            if isinstance(dict[stat], ScrolledText):  # Handles the proficiencies.
                statInfo[stat] = dict[stat].get('1.0', END)
            else:  # Handles Stats.
                statInfo[stat] = dict[stat].get()
        jstats = json.dumps(statInfo)
        f.write(jstats)
    return jstats
import json
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def saveButton(savedDicts):
    saveNamesList = []  # Used to pass names for file generation.
    for name in savedDicts:
        saveNamesList.append(name)
    labelEntrySave(savedDicts[saveNamesList[0]], saveNamesList[0])  # Basic
    labelMulEntrySave(savedDicts[saveNamesList[1]], saveNamesList[1])  # Saves
    labelEntrySave(savedDicts[saveNamesList[2]], saveNamesList[2])  # Abilities
    statSave(savedDicts[saveNamesList[3]], saveNamesList[3])  # Stats
    statSave(savedDicts[saveNamesList[4]], saveNamesList[4])  # Proficiencies
    labelMulEntrySave(savedDicts[saveNamesList[5]], saveNamesList[5])  # Equipment
    labelEntrySave(savedDicts[saveNamesList[6]], saveNamesList[6])  # Money
    return


def labelEntrySave(dict, name):
    """Handles save data generation for dictionaries that contain a label, 
    then Entry."""
    with open(f'saveData/{name}.txt', 'w') as f:
        basicInfo = {}  # Remake dict as {Label : Entry.get()}
        for label in dict:
            basicInfo[label] = dict[label][1].get()
        jbasic = json.dumps(basicInfo)
        f.write(jbasic)
    return jbasic


def labelMulEntrySave(dict, name):
    """Handles save data dictionaries with a list for the value."""
    with open(f'saveData/{name}.txt', 'w') as f:
        mulEntry = {}  # Remake dict as {Label : [List of values]}
        for label in dict:  # 'Successes', 'Failures'.
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
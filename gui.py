from tkinter import *
from tkinter import ttk
import headers
import os

# If changed, edit skillModLbls
ABILITY_NAMES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
# If changed, edit statEntry implementation in script.
STATS = ['ARMOR CLASS', 'HIT POINTS', 'INITIATIVE',
 'INSPIRATION', 'PROFICIENCY', 'SPEED']

#################################################################################
# TODO Clean this up, don't think I want StringVar, maybe return Entry object.
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
    """Return an Entry object to hold an ability's text entry."""
    # Input Validation
    vcmd = (window.register(abilValidate), '%P')
    lbl_ability = Label(frm_abilities, text=f'{abilityName}:')
    lbl_ability.grid(row=row, sticky='W')
    ent_ability = Entry(
        frm_abilities,
        width=3,
        validate='key',
        validatecommand=vcmd
    )
    ent_ability.grid(row=row, column=1, **padding)

    return ent_ability


def generateAblityModifier(baseScore):
    """Called to generate the modifier for a given ability score, baseScore. Convert
    string input to int, process, return string."""
    # Return _ if an entry field is blank.
    if baseScore == '':
        modStr = '_'
        return modStr
    # Math for calculating the ability modifier, from 0->30
    baseScore = int(baseScore)
    abilityModifier = -5
    abilityScoreTable = 0
    while abilityScoreTable < 30:
        if baseScore == abilityScoreTable or baseScore == (abilityScoreTable + 1):
            break
        abilityScoreTable += 2
        abilityModifier += 1
    abilityModifier = str(abilityModifier)
    return abilityModifier


def abilModLbls(abil, row):
    """For each item in the ability list, generate a label."""
    lbl_ability_mod = Label(frm_abilities, text=abilModDict[abil])
    lbl_ability_mod.grid(column=2, row=row)


def abilValidate(P):
    """Input validation for the ability score input fields. Only accepts 
    numbers, and only 2 characters in the field."""
    if len(P) == 0 or (len(P) ==1 and P.isdigit()) or (len(P) ==2 and P.isdigit()):
        return True
    else:
        window.bell()
        return False


def skillLbl(skillName, row):
    '''Creates a label for the skills passed from skills.txt. Returns an IntVar
    to keep the checkboxes from coming in as black squares.'''
    skill, mod = skillName.split(',')
    # Checkbox for proficiencies.
    window.chkVar = IntVar()
    skillChkbox = ttk.Checkbutton(
        frm_skills,
        variable=window.chkVar,
        command=addProf(mod.strip())
    )
    skillChkbox.grid(column=0, row=row, **padding)
    # Modifier affecting the skill.
    lbl_mod = ttk.Label(frm_skills, text=mod.strip())
    lbl_mod.grid(column=1,row=row, **padding)
    # Skill name.
    lbl_skill = ttk.Label(frm_skills, text=skill.strip())
    lbl_skill.grid(column=2,row=row, **padding, sticky='W')
    return window.chkVar

###########################################################################
# TODO Implement this guy. Currently Running once for each skill on startup.
def addProf(abilMod):
    pass


def skillModLbls(skill, row):
    """Create the label showing the skill bonus."""
    abilName = skill[-4:].strip()
    if abilName == "STR":
        lbl_skill_mod = Label(frm_skills, text=abilModDict[abilName])
        lbl_skill_mod.grid(column=3, row=row)
    elif abilName == 'DEX':
        lbl_skill_mod = Label(frm_skills, text=abilModDict[abilName])
        lbl_skill_mod.grid(column=3, row=row)
    elif abilName == 'CON':
        lbl_skill_mod = Label(frm_skills, text=abilModDict[abilName])
        lbl_skill_mod.grid(column=3, row=row)
    elif abilName == 'INT':
        lbl_skill_mod = Label(frm_skills, text=abilModDict[abilName])
        lbl_skill_mod.grid(column=3, row=row)
    elif abilName == 'WIS':
        lbl_skill_mod = Label(frm_skills, text=abilModDict[abilName])
        lbl_skill_mod.grid(column=3, row=row)
    elif abilName == 'CHA':
        lbl_skill_mod = Label(frm_skills, text=abilModDict[abilName])
        lbl_skill_mod.grid(column=3, row=row)
    

def modGen(event):
    """Generate ability score modifiers, gets called with any keypress."""
    # Create the modifier dictionary, then the modifier labels.
    for i in range(len(abilList)):
        abilModDict[ABILITY_NAMES[i]] = generateAblityModifier(abilList[i].get())
        abilModLbls(ABILITY_NAMES[i], i+1)
    # Create skill modifier labels.
    for row, skill in enumerate(skillList):
        skillModLbls(skill, row+1)
    return abilModDict

def statEntry(stat, col, row):
    frm_stat = ttk.Frame(frm_stats, borderwidth=5, relief=GROOVE)
    frm_stat.grid(column=col, row=row, sticky="NWES", **padding)
    lbl_stat = Label(frm_stat, text=stat)
    lbl_stat.grid(column=col, row=row, **padding)
    if stat == 'INSPIRATION':
        window.chkVar = IntVar()
        window.chkVar.set(0)
        chk_stat = ttk.Checkbutton(frm_stat, variable=window.chkVar, text='Advantage')
        chk_stat.grid(column=col, row=row+1)
        return chk_stat
    ent_stat = Entry(frm_stat, width=4)
    ent_stat.grid(column=col, row=row+1, **padding)
    return ent_stat

# Create the Tk class object called Character sheet.        
window = Tk()
window.title("Character Sheet")
# Will Regenerate ability modifiers if any key is pressed, allowing for changes.
abilModDict= window.bind('<Key>', modGen)
padding = {'padx': 5, 'pady': 5}

mainframe = ttk.Frame(window, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky="nsew")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Create a frame for basic character info.
frm_basicInfo = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
# Formatting compromise: columnspan of 10
frm_basicInfo.grid(column=0, row=0, columnspan=10, sticky="WE", **padding)

# Create a frame for ability scores, modifiers.
frm_abilities = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_abilities.grid(column=0, row=1, sticky="NWE", **padding)

# Create a frame for skills, and proficiency checkboxes.
frm_skills = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_skills.grid(column=1, row=1, sticky="W", **padding)

# Create a frame for the button.
frm_button = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_button.grid(column=2, row=2, sticky="SE", **padding)

# Create a frame holding some stats.
# AC, Speed, Initiative, Proficiency, HP, Inspiration
frm_stats = ttk.Frame(mainframe)
frm_stats.grid(column=2, row=1, sticky="NWE")

# Create all of the basic information for a new character, place at top of screen.
charName_var = basicInfoEntry("Name:", 0, 0)
charClass_var = basicInfoEntry("Class:", 0, 1)
charRace_var = basicInfoEntry("Race:", 2, 0)
charLevel_var = basicInfoEntry("Level:", 2, 1)
charAlign_var = basicInfoEntry("Alignment:", 4, 0)
charBg_var = basicInfoEntry("Background:", 4, 1)

# Create headers for the ability frame.
headers.abilHeader(frm_abilities)

# Create a list holding Entry objects of ability scores.
abilModDict = {}
abilList = []
for row, abil in enumerate(ABILITY_NAMES):
    abilList.append(abilityEntry(abil, row+1))
# Populate the modifier dictionary like e.g. 'STR': 2. Updates on keypress.
for i in range(len(abilList)):
    abilModDict[ABILITY_NAMES[i]] = abilList[i].get()
# Generate the labels that display the modifiers for ability scores.
for row, abil in enumerate(ABILITY_NAMES):
    abilModLbls(abil, row+1)

# Create headers for the skills frame
headers.skillHeader(frm_skills)
# Get the path of the charSkills file.
absFilePath = os.path.dirname(os.path.abspath(__file__))
skillFile = os.path.join(absFilePath, 'charSkills.txt')
# This will hold IntVar objects that need to be set to 0.
chkboxList = []
# Create skills labels with file data.
#################################################################################
# TODO Fill this dictionary to update the modifiers displayed for skills.
skillModList = {}  # Holds Skillname:mod
with open(skillFile, 'r') as sf:
    skillList = sf.readlines()
    skillList.sort()
    for row, skill in enumerate(skillList):
        chkboxList.append(skillLbl(skill.strip(), row+1))
        chkboxList[row].set(0)  # Setting IntVars to 0
        
# Create the block holding various stat elements.
sCol = 0
sRow = 0
statDict = {}
for i, stat in enumerate(STATS):
    if i == 3:
        sRow = 2
        sCol = 0
    sCol += 1
    statDict[stat] = (statEntry(stat, sCol, sRow))

def handle_button():
    print(statDict['ARMOR CLASS'].get())
button = ttk.Button(frm_button, text="Print values", command=handle_button)
button.pack()
window.mainloop()

from concurrent.futures.process import _system_limits_checked
from tkinter import *
from tkinter import ttk
import headers
import os

# If changed, edit skillModLbls
ABILITY_NAMES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
# If changed, edit statEntry implementation in script.
STATS = ['ARMOR CLASS', 'HIT POINTS', 'INITIATIVE',
 'INSPIRATION', 'PROFICIENCY', 'SPEED']

def basicInfoEntry(lbl_name, column, row):
    """Make a basic Label: entry structure. Pass the name of the label, then
    position of column and row for the grid."""
    basicInfoList = []
    lbl_basic = ttk.Label(frm_basicInfo, text=lbl_name)
    lbl_basic.grid(column=column, row=row, **padding, sticky="W")
    basicInfoList.append(lbl_basic)
    # The StringVar() class can be used to track changes in entry fields.
    ent_basic = ttk.Entry(frm_basicInfo)
    ent_basic.grid(column=column+1, row=row, **padding, sticky="W")
    basicInfoList.append(ent_basic)
    return basicInfoList


def abilityEntry(abilityName, row):
    """Return a list of tkinter objects. 0->Ability Label, 1->Entry Object,
     2->Modifier Label."""
    abilList = []
    # Input Validation
    vcmd = (window.register(abilValidate), '%P')
    # Label Holding ability name
    lbl_ability = Label(frm_abilities, text=f'{abilityName}:')
    lbl_ability.grid(row=row, sticky='W')
    abilList.append(lbl_ability)
    # Entry object for the score to go in.
    ent_ability = Entry(
        frm_abilities,
        width=3,
        validate='key',
        validatecommand=vcmd
    )
    ent_ability.grid(column=1, row=row, **padding)
    abilList.append(ent_ability)
    # Label for ability modifier.
    lbl_mod = Label(frm_abilities, text=genAbilMod(ent_ability.get()))
    lbl_mod.grid(column=2, row=row)
    abilList.append(lbl_mod)
    return abilList

def genAbilMod(baseScore):
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
    skillsList = []
    skill, mod = skillName.split(',')
    # Checkbox for proficiencies.
    window.chkVar = IntVar()
    window.chkVar.set(0)  # Keeps Checkbuttons from starting filled.
    skillChkbox = ttk.Checkbutton(
        frm_skills,
        variable=window.chkVar,
    )
    skillChkbox.grid(column=0, row=row, **padding, sticky='NEWS')
    skillsList.append(skillChkbox)
    # Modifier affecting the skill.
    lbl_mod = ttk.Label(frm_skills, text=mod.strip())
    lbl_mod.grid(column=1,row=row, **padding)
    skillsList.append(lbl_mod)
    # Skill name.
    lbl_skill = ttk.Label(frm_skills, text=skill.strip())
    lbl_skill.grid(column=2,row=row, **padding, sticky='W')
    skillsList.append(lbl_skill)
    # Skill Bonus
    lbl_bonus = ttk.Label(frm_skills, text=skillbonus(lbl_mod.cget('text')))
    lbl_bonus.grid(column=3, row=row, **padding, sticky='E')
    skillsList.append(lbl_bonus)
    skillsList.append(window.chkVar)  # Returns only to hold value. Not accessed.
    return skillsList

def skillbonus(mod):
    return abilDict[mod][2].cget('text')


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
    vcmd = (window.register(statValidate), '%P')
    ent_stat = Entry(
        frm_stat,
        width=4,
        validate='key',
        validatecommand=vcmd
    )
    ent_stat.grid(column=col, row=row+1, **padding)
    return ent_stat


def statValidate(P):
    """Validate inputs for the stat objects. Takes Digits only."""
    if len(P) == 0 or (len(P) > 0 and P.isdigit()):
        return True
    else:
        window.bell()
        return False

def genAbilBonus(event):
    """Generate the bonus for an ability score whenever focus leaves an Entry 
    object."""
    for abil in abilDict.keys():
        if abilDict[abil][1].get() == '':
            abilDict[abil][2].configure(text='_')
        if not abilDict[abil][1].get() == '':  # If the field isn't blank:
            abilDict[abil][2].configure(text=genAbilMod(abilDict[abil][1].get()))

def genSkillBonus(event):
    for skill in skillDict.keys():
        
        skillDict[skill][3].configure(text=genAbilMod(abilDict[skillDict[skill][1].cget('text')][1].get()))



# Create the Tk class object called Character sheet.        
window = Tk()
window.title("Character Sheet")
# Will Regenerate ability modifiers when focus moves out of any Entry.
window.bind_class('Entry','<FocusOut>', genAbilBonus)
window.bind_class('Entry','<FocusOut>', genSkillBonus, add='+')
# Makes any widget clicked become focus.
window.bind_all('<Button-1>', lambda event: event.widget.focus_set())
#abilModDict= window.bind('<Key>', modGen)
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
frm_abilities.grid(column=0, row=2, sticky="NWE", padx=5)
# Create headers for the ability frame.
headers.abilHeader(mainframe)

# Create a frame for skills, and proficiency checkboxes.
frm_skills = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_skills.grid(column=1, row=2, sticky="W", padx=5)
# Create headers for the skills frame.
headers.skillHeader(mainframe)

# Create a frame for the button.
frm_button = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_button.grid(column=2, row=3, sticky="SE", **padding)

# Create a frame holding some stats.
# AC, Speed, Initiative, Proficiency, HP, Inspiration
frm_stats = ttk.Frame(mainframe)
frm_stats.grid(column=2, row=1, sticky="NWE", rowspan=2)

# Create all of the basic information for a new character, place at top of screen.
# Each item is a list with index 0 Label, index 1 Entry objects.
charNameList = basicInfoEntry("Name:", 0, 0)
charClassList = basicInfoEntry("Class:", 0, 1)
charRaceList = basicInfoEntry("Race:", 2, 0)
charLevelList = basicInfoEntry("Level:", 2, 1)
charAlignList = basicInfoEntry("Alignment:", 4, 0)
charBgList = basicInfoEntry("Background:", 4, 1)

# Will hold all of the info in the abilities frame. 
# Dict key ability name, value is list index 0 Label, index 1 Entry
abilDict = {}
for row, abil in enumerate(ABILITY_NAMES):
    abilDict[abil] = abilityEntry(abil, row)

# Get the path of the charSkills file.
absFilePath = os.path.dirname(os.path.abspath(__file__))
skillFile = os.path.join(absFilePath, 'charSkills.txt')
# Key = row, values are a list with indexes:
# 0->Checkbutton Object, 1-> Mod Label, 2-> Skill Name Label, 3-> Skill Bonus Label
skillDict = {}
with open(skillFile, 'r') as sf:
    skillList = sf.readlines()
    skillList.sort()
    # Create the skill checkboxes and labels.
    for row, skill in enumerate(skillList):
        skillDict[row] = skillLbl(skill.strip(), row)

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
    print()
button = ttk.Button(frm_button, text="Print values", command=handle_button)
button.pack()
window.mainloop()
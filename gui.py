from tkinter import *
from tkinter import ttk
import headers
import character

ABILITY_NAMES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']


def generateAblityModifier(baseScore):
    """Called to generate the modifier for a given ability score, baseScore. Takes 
    a StringVar, so need to convert that to an int, then process it."""
    mod_var = StringVar()
    # Return _ if an entry field is blank.
    if baseScore == '':
        mod_var.set('_')
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
    """Generate a StringVar to hold an ability's text entry."""
    ent_ability_var = StringVar()
    # Input Validation
    vcmd = (window.register(abilValidate), '%P')
    lbl_ability = Label(frm_abilities, text=f'{abilityName}:')
    lbl_ability.grid(row=row, sticky='W')
    ent_ability = Entry(
        frm_abilities,
        width=3,
        textvariable=ent_ability_var,
        validate='key',
        validatecommand=vcmd
    )
    ent_ability.grid(row=row, column=1, **padding)
    return ent_ability_var


def skillLbl(skillName, row):
    '''Creates a label for the skills passed from skills.txt. Place'''
    mod, skill = skillName.split(',')
    # Checkbox for proficiencies.
    skillChkbox = ttk.Checkbutton(frm_skills)
    skillChkbox.grid(column=0, row=row, **padding)
    # Modifier affecting the skill.
    lbl_mod = ttk.Label(frm_skills, text=mod)
    lbl_mod.grid(column=1,row=row, **padding)
    # Skill name.
    lbl_skill = ttk.Label(frm_skills, text=skill)
    lbl_skill.grid(column=2,row=row, **padding, sticky='W')
    # Skill bonus.
    #lbl_sBonus = ttk.Label(frm_skills, text=)

#####################################################################
# TODO
def skillModGen(mDict):
    for row, skill in enumerate(skillList):
        mod = skill[:3]
        print(mDict)
        """
        if mDict[mod]:
            lbl_mod = Label(frm_skills, text=mDict[mod][0])
            lbl_mod.grid(column=3, row=row+1)
        if mDict[mod]:
            lbl_mod = Label(frm_skills, text=mDict[mod][1])
            lbl_mod.grid(column=3, row=row+1)
        """
def abilCallback(*args):
    """Called when .trace() is used in one of the ability score fields."""
    modList = []
    modDict = {}
    for i in range(len(abilList)):
        modList.append(abilCallbackHandler(abilList[i], i+1).get())
    
    for ability in ABILITY_NAMES:
        modDict[ability] = modList

    skillModGen(modDict)

def abilCallbackHandler(abilStrVar, row):
    """Handles argument input for the .trace() callback for ability score fields.
    Dynamically creates the labels showing ability score modifiers."""
    strVar = generateAblityModifier(abilStrVar.get())
    lbl_mod = Label(frm_abilities, textvariable=strVar)
    lbl_mod.grid(column=2, row=row)
    return strVar

def abilValidate(P):
    """Input validation for the ability score input fields. Only accepts 
    numbers, and only 2 characters in the field."""
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isdigit():
        return True
    elif len(P) == 2 and P.isdigit():
        return True
    else:
        window.bell()
        return False


# Create the Tk class object called Character sheet.        
window = Tk()
window.title("Character Sheet")

# Basic 5x5 padding to pass.
padding = {'padx': 5, 'pady': 5}

mainframe = ttk.Frame(window, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky="nsew")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Create a frame for basic character info.
frm_basicInfo = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_basicInfo.grid(column=0, row=0, columnspan=10)  # Formatting compromise: columnspan

# Create a frame for ability scores, modifiers.
frm_abilities = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_abilities.grid(column=0, row=1, pady=5, sticky="NWE")

# Create a frame for skills, and proficiency buttons.
frm_skills = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_skills.grid(column=1, row=1, **padding, sticky="W")

# Create a frame for the button.
frm_button = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_button.grid(column=2, row=2, sticky="SE")

frm_stats = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_stats.grid(column=2, row=1, **padding)
# Create all of the basic information for a new character, place at top of screen.
charName_var = basicInfoEntry("Name:", 0, 0)
charClass_var = basicInfoEntry("Class:", 0, 1)
charRace_var = basicInfoEntry("Race:", 2, 0)
charLevel_var = basicInfoEntry("Level:", 2, 1)
charAlign_var = basicInfoEntry("Alignment:", 4, 0)
charBg_var = basicInfoEntry("Background:", 4, 1)

# Create headers for the skills frame
headers.skillHeader(frm_skills)

# Create skills labels with file data.
with open('skills.txt', 'r') as sf:
    skillList = sf.readlines()
    for row, skill in enumerate(skillList):
        skillLbl(skill.strip(), row+1)


# Create headers for the ability frame.
headers.abilHeader(frm_abilities)

# Create a list holding StringVar objects with the ability scores inside them.
abilList = []
for row, abil in enumerate(ABILITY_NAMES):
    abilList.append(abilityEntry(abil, row+1))

# Generate the modifiers for the ability scores using .trace() 
for i in range(len(abilList)):
    abilList[i].trace('w', abilCallback)



def handle_button():
    print(abilList[0].get())

button = ttk.Button(frm_button, text="Print values", command=handle_button)
button.pack()
window.mainloop()

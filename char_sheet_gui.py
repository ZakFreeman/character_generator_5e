from tkinter import *
from tkinter import ttk
import headers
import os
import stats
import char_entry_fields as cef
import buttons
import json

# If changed, edit skillModLbls
ABILITY_NAMES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
STATS = ['ARMOR CLASS', 'HIT POINTS', 'MAX HP', 'INITIATIVE', 'PROFICIENCY',
 'INSPIRATION', 'SPEED', 'TEMP HP', 'HIT DICE']
MONEY = ['CP', 'SP', 'EP', 'GP', 'PP']

def basicInfoEntry(lbl_name, column, row):
    """Make a basic Label: entry structure. Pass the name of the label, then
    position of column and row for the grid."""
    basicinfoList = []
    lbl_basic = Label(frm_basicInfo, text=lbl_name, font='helvetica 12')
    lbl_basic.grid(column=column, row=row, **padding)
    basicinfoList.append(lbl_basic)
    ent_basic = Entry(frm_basicInfo)
    ent_basic.grid(column=column+1, row=row, **padding)
    basicinfoList.append(ent_basic)
    return basicinfoList


def abilityEntry(abilityName, row):
    """Return a list of tkinter objects. 0->Ability Label, 1->Entry Object,
     2->Modifier Label."""
    abilList = []
    # Input Validation
    vcmd = (window.register(abilValidate), '%P')
    # Label Holding ability name
    lbl_ability = Label(frm_abilities, text=f'{abilityName}:')
    lbl_ability.grid(row=row)
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
    lbl_mod.grid(column=2, row=row, **padding)
    abilList.append(lbl_mod)
    # Checkbox for saving throw proficiency
    chk_var = BooleanVar()
    chk_save = ttk.Checkbutton(frm_abilities, variable=chk_var, command=addSaveProf)
    chk_save.grid(column=3, row=row, padx=(5,0))
    abilList.append(chk_var)
    # Label for saving throw value
    lbl_save = Label(frm_abilities, text=genAbilMod(ent_ability.get()))
    lbl_save.grid(column=4, row=row)
    abilList.append(lbl_save)
    return abilList


def genAbilMod(baseScore):
    """Called to generate the modifier for a given ability score, baseScore. Convert
    string input to int, process, return string."""
    # Return _ if an entry field is blank.
    if baseScore == '':
        modStr = '__'
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
    """Creates a label for each skill passed from skills.txt. Also creates checkboxes."""
    skillsList = []
    skill, mod = skillName.split(',')
    # Checkbox for proficiencies.
    chkVar = BooleanVar()
    skillChkbox = ttk.Checkbutton(
        frm_skills,
        command=addProf,
        variable=chkVar,
    )
    skillChkbox.grid(column=0, row=row, **padding)
    skillsList.append(chkVar)
    # Modifier affecting the skill.
    lbl_mod = Label(frm_skills, text=mod.strip())
    lbl_mod.grid(column=1,row=row, **padding)
    skillsList.append(lbl_mod)
    # Skill name.
    lbl_skill = Label(frm_skills, text=skill.strip())
    lbl_skill.grid(column=2,row=row, **padding, sticky='W')
    skillsList.append(lbl_skill)
    # Skill Bonus
    lbl_bonus = Label(frm_skills, text=skillbonus(lbl_mod.cget('text')))
    lbl_bonus.grid(column=3, row=row, **padding)
    skillsList.append(lbl_bonus)
    return skillsList


def skillbonus(mod):
    """Fetches the bonus from the label being displayed by the ability scores."""
    return abilDict[mod][2].cget('text')


def addProf():
    """Loops through the skill list to add proficiencies to any new checkboxes."""
    for i in skillDict.keys():
        if statDict['PROFICIENCY'].get() == '' or skillDict[i][3].cget('text') == '__':
            pass
        elif skillDict[i][0].get():  # Enter this block if the checkbox is on
            # Generate the modifier based off the input from ability score Entry object.
            newMod = skillbonus(
                skillDict[i][1].cget('text')) + int(statDict['PROFICIENCY'].get())
            skillDict[i][3].configure(text=newMod)
        else:
            skillDict[i][3].configure(text=skillbonus(skillDict[i][1].cget('text')))
            

def addSaveProf():
    """Loops through ability list to add saving throw proficiencies to checkboxes."""
    for i, abil in enumerate(abilDict.keys()):
        if statDict['PROFICIENCY'].get() == '' or abilDict[abil][2].cget('text') == '__':
            pass
        elif abilDict[abil][3].get():
            profMod = int(statDict['PROFICIENCY'].get())
            # Generate the modifier based off the input from ability score Entry object.
            newMod = skillbonus(abil) + profMod
            abilDict[abil][4].configure(text=newMod)
        else:
            abilDict[abil][4].configure(text=skillbonus(abil))


def addProfCallback(event):
    """Cheeky workaround to allow addProf to function as a Checkbox and an event.
    Probably bad practice, but works well."""
    addProf()

def addSaveCallback(event):
    """Cheeky workaround to allow addSaveProf to function as a Checkbox and an event.
    Probably bad practice, but works well."""
    addSaveProf()

def genAbilBonus(event):
    """Generate the bonus for an ability score whenever focus leaves an Entry 
    object."""
    for abil in abilDict.keys():
        if abilDict[abil][1].get() == '':
            abilDict[abil][2].configure(text='__')  # Ability bonus
            abilDict[abil][4].configure(text='__')  # Save bonus
        if not abilDict[abil][1].get() == '':  # If the field isn't blank:
            abilDict[abil][2].configure(text=genAbilMod(abilDict[abil][1].get()))
            abilDict[abil][4].configure(text=genAbilMod(abilDict[abil][1].get()))


def genSkillBonus(event):
    """Generate the bonus displayed in the skills frame. Gets the score from the 
    abilDict."""
    for row in skillDict.keys():
        # Changes the skill bonus label text to reflect the ability score bonus.
        skillDict[row][3].configure(
            text=genAbilMod(abilDict[skillDict[row][1].cget('text')][1].get()))


def loadButton(savedDicts):
    """Loads info saved in the text files into the loadDict dictionary. 
    Finally paid for using global variables instead of a class."""
    loadList = []
    for name in savedDicts:
        loadList.append(name)
    for file in savedDicts:
        with open(f'saveData/{file}.txt', 'r') as f:
            text = f.read()
            jdict = json.loads(text)
            loadDict[file] = jdict
    basicLoad(loadDict[loadList[0]])  # Basic info
    dsaveLoad(loadDict[loadList[1]])  # Death Saves
    abilLoad(loadDict[loadList[2]])  # Abilities
    skillLoad(loadDict[loadList[3]])  # Skills
    statLoad(loadDict[loadList[4]])  # Stats
    profLoad(loadDict[loadList[5]])  # Proficiencies
    invLoad(loadDict[loadList[6]])  # Inventory
    monLoad(loadDict[loadList[7]])  # Money
    abilDict[ABILITY_NAMES[1]][1].focus()  # These lines are used to 
    abilDict[ABILITY_NAMES[0]][1].focus()  # call the FocusOut event callbacks.


def basicLoad(dict):
    """Loads the basic info into entry fields."""
    for label in dict:
        basicinfoDict[label][1].delete(0, 'end')
        basicinfoDict[label][1].insert(0, dict[label])


def dsaveLoad(dict):
    """Loads the deathsave checkboxes."""
    for savetype in dict:  # For each success or failure:
        for i, chk in enumerate(dict[savetype]):  # Move through list of boxes.
            if chk:  # Bool returns True/False
                dsaveDict[savetype][i].set(True)
            else:
                dsaveDict[savetype][i].set(False)


def abilLoad(dict):  # SAVE CHECKBOXES TODO
    """Loads info from the json dicts into the entry fields for abilities."""
    for mod in dict:
        abilDict[mod][1].delete(0, 'end')
        abilDict[mod][1].insert(0, dict[mod][0])
        if dict[mod][1]:
            abilDict[mod][3].set(True)
        else:
           abilDict[mod][3].set(False)


def skillLoad(dict):
    """Loads the skill checkboxes."""
    for row in dict:
        if dict[row]:
            skillDict[int(row)][0].set(True)
        else:
            skillDict[int(row)][0].set(False)


def statLoad(dict):
    """Loads the stat boxes Entry Fields and checkboxes."""
    for stat in dict:
        if isinstance(statDict[stat], BooleanVar):  # The checkbox value.
            statDict[stat].set(dict[stat])
        else:
            statDict[stat].delete(0, END)
            statDict[stat].insert(0, dict[stat])


def profLoad(dict):
    """Loads the proficiencies text boxes. Also loads an extra newline
    char whenever loaded, but unsure how to solve that."""
    for prof in dict:
        plDict[prof].delete('1.0', END)
        plDict[prof].insert(END, dict[prof])


def invLoad(dict):
    """Loads the inventory items."""
    for row in dict:
        for i, detail in enumerate(dict[row]):
            invDict[int(row)][i].delete(0, END)
            invDict[int(row)][i].insert(0, detail)



def monLoad(dict):
    """Loads the money."""
    for money in dict:
        monDict[money][1].delete(0, END)
        monDict[money][1].insert(0, dict[money])


# Create the Tk class object titled Character sheet.        
window = Tk()
window.title("Character Sheet")
# Will Regenerate ability modifiers when focus moves out of any Entry.
window.bind_class('Entry', '<FocusOut>', genAbilBonus)
window.bind_class('Entry', '<FocusOut>', genSkillBonus, add='+')
window.bind_class('Entry', '<FocusOut>', addProfCallback, add='+')
window.bind_class('Entry', '<FocusOut>', addSaveCallback, add='+')
# Makes any widget clicked become focus.
window.bind_all('<Button-1>', lambda event: event.widget.focus_set())
# Formatting
padding = {'padx': 5, 'pady': 5}
mainframe = ttk.Frame(window, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky="nsew")

# Create a frame for basic character info.
frm_basicInfo = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_basicInfo.grid(column=0, row=0, columnspan=4, sticky="W", **padding)

# Create a frame holding death saving throws.
frm_dSaves = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_dSaves.grid(column=0, row=3, **padding, sticky='NSEW')
headers.dSaveHeader(frm_dSaves)

# Create a frame for ability scores, modifiers.
frm_abilities = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_abilities.grid(column=0, row=1, sticky="NWES", **padding, columnspan=2)
# Create headers for the ability frame.
headers.abilHeader(frm_abilities)

# Create a frame for skills, and proficiency checkboxes.
frm_skills = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_skills.grid(column=2, row=1, sticky="NWS", **padding, rowspan=2)
# Create headers for the skills frame.
headers.skillHeader(frm_skills)

# Create a frame holding some stats.
frm_stats = ttk.Frame(mainframe)
frm_stats.grid(column=3, row=1, sticky="NWE")

# Create a frame holding the 'Proficiencies & Languages' Block.
frm_p_l = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
headers.profHeader(frm_p_l)
frm_p_l.grid(column=0, row=2, **padding, sticky='NWES', columnspan=2)

# Create a frame holding the Inventory block.
frm_inv = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
headers.invHeader(frm_inv)
frm_inv.grid(column=3, row=2, **padding, sticky='NW', rowspan=2)

# Create a frame holding money values.
frm_money = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_money.grid(column=1, row=3, **padding, sticky='NWE', columnspan=2)

# Create a frame for the button.
frm_button = ttk.Frame(mainframe, borderwidth=5, relief=GROOVE)
frm_button.grid(column=3, row=10, sticky="SE", **padding)

# A dict holding all of the dictionaries created to hold values.
saveDict = {}
loadDict = {}   # A dict of dicts holding loaded data.
# Create all of the basic information for a new character, place at top of screen.
# Each item is a list with index 0 Label, index 1 Entry objects.
basicinfoDict = {}
basicinfoDict['Name'] = basicInfoEntry("Name:", 0, 0)
basicinfoDict['Class'] = basicInfoEntry("Class:", 0, 1)
basicinfoDict['Race'] = basicInfoEntry("Race:", 2, 0)
basicinfoDict['Level'] = basicInfoEntry("Level:", 2, 1)
basicinfoDict['Alignment'] = basicInfoEntry("Alignment:", 4, 0)
basicinfoDict['Background'] = basicInfoEntry("Background:", 4, 1)
saveDict['basicinfo'] = basicinfoDict

# Create the Death Saving Throws box
dsaveDict = {}
dsaveDict['Successes'] = cef.deathSave(frm_dSaves, 'Successes', 1)
dsaveDict['Failures'] = cef.deathSave(frm_dSaves, 'Failures', 3)
saveDict['deathsaves'] = dsaveDict

# Will hold all of the info in the abilities frame. Dict keys == ability, values:
# 0->Ability Label, 1->Entry, 2->Bonus Label, 3->BooleanVar, 4-> Save bonus Label.
abilDict = {}
for row, abil in enumerate(ABILITY_NAMES):
    abilDict[abil] = abilityEntry(abil, row+1)
saveDict['abilities'] = abilDict

# Get the path of the charSkills file.
absFilePath = os.path.dirname(os.path.abspath(__file__))
skillFile = os.path.join(absFilePath, 'charSkills.txt')
# Key == row, values are a list with indexes:
# 0->BooleanVar, 1-> Mod Label, 2-> Skill Name Label, 3-> Skill Bonus Label
skillDict = {}
with open(skillFile, 'r') as sf:
    skillList = sf.readlines()
    skillList.sort()
    # Create the skill checkboxes and labels.
    for row, skill in enumerate(skillList):
        skillDict[row] = skillLbl(skill.strip(), row+1)
saveDict['skills'] = skillDict
# Create the block holding various stat elements.
statDict = {}
statDict[STATS[0]] = stats.statEntry(STATS[0], 0, 0, window, frm_stats)
statDict[STATS[1]] = stats.statEntry(STATS[1], 1, 0, window, frm_stats)
statDict[STATS[2]] = stats.statEntry(STATS[2], 1, 1, window, frm_stats)
statDict[STATS[3]] = stats.statEntry(STATS[3], 2, 0, window, frm_stats)
statDict[STATS[4]] = stats.statEntry(STATS[4], 0, 1, window, frm_stats)
statDict[STATS[5]] = stats.statEntry(STATS[5], 2, 1, window, frm_stats)
statDict[STATS[6]] = stats.statEntry(STATS[6], 0, 2, window, frm_stats)
statDict[STATS[7]] = stats.statEntry(STATS[7], 1, 2, window, frm_stats)
statDict[STATS[8]] = stats.statEntry(STATS[8], 2, 2, window, frm_stats)
saveDict['stats'] = statDict

# Create the Proficiencies and Language Text Box
plDict = {}
plDict['Armor'] = cef.otherProfs(frm_p_l, 0, 0, 'Armor')
plDict['Weapons'] = cef.otherProfs(frm_p_l, 0, 2, 'Weapons')
plDict['Tools'] = cef.otherProfs(frm_p_l, 0, 4, 'Tools')
plDict['Languages'] = cef.otherProfs(frm_p_l, 0, 6, 'Languages')
saveDict['profs'] = plDict

# Create the Inventory box.
invDict = {}
for i in range(20):
    invDict[i] = cef.invEntry(frm_inv, i)
saveDict['inventory'] = invDict

# Create the money tracker.
monDict = {}
for col, coin in enumerate(MONEY):
    monDict[coin] = cef.wealth(frm_money, coin, col)
saveDict['money'] = monDict

save_button = ttk.Button(
    frm_button,
    text="Save",
    command=lambda : buttons.saveButton(saveDict)
    )
save_button.pack(side='right')

load_button = ttk.Button(
    frm_button,
    text="Load",
    command=lambda : loadButton(saveDict)
    )
load_button.pack(side='left')

window.mainloop()
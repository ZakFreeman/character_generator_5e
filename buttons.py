import json

def saveButton(savedDicts):
    basicDict = savedDicts['basicinfo']
    with open('saveData/basicinfo.txt', 'w') as f:
        basic = {}
        for label in basicDict:
            basic[label] = basicDict[label][1].get()
        jbasic = json.dumps(basic)
        f.write(jbasic)
    
    dsaveDict = savedDicts['deathsaves']  # TODO
    with open('saveData/deathsaves.txt', 'w') as f:
        dsave = {}
        for save in dsaveDict:  # 'Successes', 'Failures'.
            for chk in dsaveDict[save]:  # 3 Checkboxes each.
                dsave[save] = chk.get()
        f.write(json.dumps(dsave))

    abilDict = savedDicts['abilities']
    
    return
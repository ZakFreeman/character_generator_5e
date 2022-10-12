def saveButton(savedDicts):
    basicDict = savedDicts['basicinfo']
    with open('saveData/basicinfo.txt', 'w') as f:
        for label in basicDict:
            f.write(basicDict[label][1].get() + '\n')
    
    dsaveDict = savedDicts['deathsaves']
    with open('saveData/deathsaves.txt', 'w') as f:
        for save in dsaveDict:
            for chk in dsaveDict[save]:
                if chk.get():
                    f.write('1\n')
                else:
                    f.write('0\n')
    return
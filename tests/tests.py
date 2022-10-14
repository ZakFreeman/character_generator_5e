import json

with open('saveData/abilities.txt', 'r') as f:
    j = f.read()
    jd = json.loads(j)  # Makes a dict from the txt file in a json str.
    print(jd)
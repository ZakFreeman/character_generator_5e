# Python 3.1
# A character generator for D&D 5E, randomized or from user input (TBI).
import character
A_STR, A_DEX, A_CON, A_INT, A_WIS, A_CHA = character.ABILITY_NAMES

def main():

    char = character.Character('Domorn')
    
    # Write values generated from Character into a text file.
    with open(f'{char.charName} Character Sheet.txt', 'w') as f:
        f.write(f'Character Name: {char.charName}\n')
        for k in list(char.abilities.keys()):
            f.write(f'{k}: {char.abilities[k][0]}, {char.abilities[k][1]}\n')

if __name__ == '__main__':
    main()
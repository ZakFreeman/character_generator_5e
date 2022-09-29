# Python 3.1
# A character generator for D&D 5E, either randomized or from user input (TBI)
import character
STREN, DEXTE, CONST, INTEL, WISDO, CHARI = character.ABILITY_NAMES

def main():

    char = character.Character('Domorn')
    print(f'{char.abilities}\n')

    char.editAbilityScore(STREN, 4)
    print(char.abilities)

if __name__ == '__main__':
    main()
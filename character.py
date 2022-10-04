#!/usr/bin/env

import dice

ABILITY_NAMES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

class Character:
    def __init__(self, name):
        self.charName = name
        self.abilities = generateAbilityScores()  # Creates a dictionary for scores


    def getAbilityModifier(self, abilityName):
        """Returns only the ability modifier associated with an ability score."""
        return self.abilities[abilityName][1]


    def editAbilityScore(self, abilityName, adjustment):
        """Increase or decrease an ability score, regenerate modifier."""
        if (self.abilities[abilityName][0] + adjustment)  <= 0:
            return print('Cannot adjust to 0 or lower.')
        self.abilities[abilityName][0] += adjustment
        self.abilities[abilityName][1] = generateAblityModifier(
            self.abilities[abilityName][0])
        return print(
            f'Ability Scores adjusted: {abilityName} {self.abilities[abilityName]} ')
        

def generateAbilityScores():
    """Returns a dictionary after randomly generating ability scores.
     Values stored as lists, with score followed by modifier."""
    baseScoreDict = {}
    # Gets random ability scores, assigns to first key in dict.
    for abilityType in ABILITY_NAMES:
        baseScoreList = []
        for i in range(4):  # Roll 4 d6, drop lowest.
            baseScoreList.append(dice.roll(6))
        baseScoreList.remove(min(baseScoreList))
        baseScoreSum = sum(baseScoreList)

        baseScoreDict[abilityType] = [baseScoreSum, generateAblityModifier(baseScoreSum)]
    return baseScoreDict


def generateAblityModifier(baseScore):
    """Called to generate the modifier for a given ability score, baseScore."""
    abilityModifier = -5
    abilityScoreTable = 0
    while abilityScoreTable < 30:
        if baseScore == abilityScoreTable or baseScore == (abilityScoreTable + 1):
            break
        abilityScoreTable += 2
        abilityModifier += 1
    return abilityModifier
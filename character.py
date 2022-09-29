#!/usr/bin/env

import random

ABILITY_NAMES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

class Character:
    def __init__(self, name):
        self.charName = name
        self.abilities = generateAbilityScores()  # Creates a dictionary for scores


    def getAbilityModifiers(self, abilityName):
        """Returns only the ability modifier associated with an ability score."""
        return self.abilities[abilityName][1]


    def editAbilityScore(self, abilityName, adjustment):
        """Increase or decrease an ability score, regenerate modifier."""
        self.abilities[abilityName][0] += adjustment
        self.abilities[abilityName][1] = generateAblityModifier(
            self.abilities[abilityName][0])
        return print(
            f'Ability Scores adjusted. {abilityName} {self.abilities[abilityName]} ')
        

def generateAbilityScores():
    """Returns a dictionary after randomly generating ability scores.
     Values stored as lists, with score followed by modifier."""
    baseScoreDict = {}
    # Gets random ability scores, assigns to first key in dict.
    for abilityType in ABILITY_NAMES:
        baseScoreList = []
        for i in range(4):
            baseScoreList.append(random.randint(1, 6))
        baseScoreList.remove(min(baseScoreList))
        baseScoreSum = sum(baseScoreList)

        baseScoreDict[abilityType] = [baseScoreSum, generateAblityModifier(baseScoreSum)]
    return baseScoreDict

def generateAblityModifier(baseScore):
    """Called to generate the modifier for a given ability score, baseScore."""
    # TODO Make negative number works as an arg being passed, if it takes the base score
    # down below zero.
    abilityModifier = -5
    abilityScoreTable = 0
    while abilityScoreTable < 30:
            if baseScore == abilityScoreTable or baseScore == (abilityScoreTable + 1):
                break
            abilityScoreTable += 2
            abilityModifier += 1
    return abilityModifier
#!/usr/bin/env

import random 

def roll(sides):
    """Roll a die with a passed number of sides."""
    return random.randint(1, sides)
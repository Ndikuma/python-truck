from random import randint
from math import floor


def modifier(value):
    return floor((value - 10) / 2)


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        rolls = [randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)
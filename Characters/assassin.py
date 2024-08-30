"""
Filename: assassin.py
Description: Defines Assassin class
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

from .character import Character
from action import Action
from color import Color

class Assassin(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self._HP = 20
        self._HP_MAX = 20
        self._MP = 20
        self._MP_MAX = 20
        self._ATK = 4
        self._DEF = -1
        self._color = Color.ORANGE
        
        # Init Assassin actions
        self._actions.append(Action(
            "Attack",
            "Slash with poisoned dagger. Deals 2d6 damage.",
            self.knife
        ))
        self._actions.append(Action(
            "Critical Strike",
            "Teleport through the shadows, landing a lethal blow on an opponent. Deals 6d6 damage, costs 20 MP.",
            self.critical_strike
        ))
        self._actions.sort(key=lambda action: action.name)

    # TODO: Assassin.knife()
    def knife():
        pass
    
    # TODO: Assassin.critical_hit()
    def critical_strike():
        pass
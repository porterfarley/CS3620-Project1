"""
Filename: mage.py
Description: Defines Mage class
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

from .character import Character
from action import Action
from events import *
from color import Color

class Mage(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self._HP = 15
        self._HP_MAX = 15
        self._MP = 40
        self._MP_MAX = 40
        self._ATK = -1
        self._DEF = 2
        self._color = Color.BLUE
        
        # Init Mage Actions
        self._actions.pop()
        self._actions.append(Action(
            "Attack",
            "Swing with mage's staff. Deals 1d6 damage.",
            self.attack
        ))
        self._actions.append(Action(
            "Blizzard",
            "Cast a barrage of icy shards. Deals 2d6 damage, costs 5 MP.",
            self.blizzard
        ))
        self._actions.append(Action(
            "Fireball", 
            "Hurl a raging ball of flame that hits all opponents. Deals 4d6 damage, costs 20 MP.", 
            self.fireball
        ))
        self._actions.sort(key=lambda action: action.name)
        
    # TODO: Mage.fireball()
    def fireball(self, enemies: list[Character]):
        pass
    
    
    
    
    # TODO: Mage.staff()
    def attack(self, enemies: list[Character]):
        
        DICE = 6
        NUM_DICE = 1
        ACTION_NAME = "Attack"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
    
    
    
        
    
    # TODO: Mage.blizzard()
    def blizzard(self):
        pass
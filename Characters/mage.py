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
        self._actions.append(Action(
            "Attack",
            "Swing with mage's staff. Deals 1d6 damage.",
            self.staff
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
        
        target = get_user_opponent(enemies)
        print(f"  > I Cast Fireball at {target.get_name()}")
    
    
    
    
    # TODO: Mage.staff()
    def staff(self, enemies: list[Character]):
        
        DICE = 6
        NUM_DICE = 1
        ACTION_NAME = "Attack"
        
        target = get_user_opponent(enemies)    
        attack(self, target, enemies, DICE, NUM_DICE, ACTION_NAME)
    
    
    
        
    
    # TODO: Mage.blizzard()
    def blizzard(self):
        pass
"""
Filename: bbg.py
Description: Defines bbg class
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 09/09/2024
"""

from .character import Character
from action import Action
from combat import *
from color import Color

from .character import Character
from action import Action
from combat import *
from color import Color

class bbg(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self._HP = 999
        self._HP_MAX = 999
        self._MP = 999
        self._MP_MAX = 999
        self._ATK = 20
        self._DEF = 20
        self._color = Color.RED
        
        # Init bbg Actions
        self._actions.clear()
        self._actions.append(Action(
            "Smash",
            "Smashes down with a giant fist of darkness.",
            self.attack
        ))
        
    def __str__(self) -> str:
        # Name the ClassType: xx/xx HP || xx/xx MP
        txt = f'{Color.BOLD}{self._color}{self._name}{Color.END}'
        txt += f': {self._HP}/{self._HP_MAX} HP || {self._MP}/{self._MP_MAX} MP'
        return txt 
        
    def attack(self, enemies: list[Character]) -> None:
        DICE = 6
        NUM_DICE = 30
        ACTION_NAME = "Attack"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
        
    def get_cpu_action(self) -> Action:
        return self._actions[0]
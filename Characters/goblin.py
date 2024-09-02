"""
Filename: goblin.py
Description: Defines Goblin class
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/29/2024
"""

from .character import Character
from action import Action
from events import *
from color import Color

class Goblin(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self._HP = 7
        self._HP_MAX = 7
        self._MP = 0
        self._MP_MAX = 0
        self._ATK = 1
        self._DEF = -2
        self._color = Color.RED
        
        # Init Goblin Actions
        self._actions.clear()
        self._actions.append(Action(
            "Attack",
            "Slash with a rusty knife.",
            self.attack
        ))
        
    def __str__(self) -> str:
        # Name the ClassType: xx/xx HP || xx/xx MP
        txt = f'{Color.BOLD}{self._color}{self._name}{Color.END}'
        txt += f': {self._HP}/{self._HP_MAX} HP || {self._MP}/{self._MP_MAX} MP'
        return txt 
        
    def attack(self, enemies: list[Character]) -> None:
        DICE = 6
        NUM_DICE = 1
        ACTION_NAME = "Attack"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
        
    def get_cpu_action(self) -> Action:
        return self._actions[0]
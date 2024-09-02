"""
Filename: knight.py
Description: Defines Knight class
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

from .character import Character
from action import Action
from color import Color

class Knight(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self._HP = 30
        self._HP_MAX = 30
        self._MP = 10
        self._MP_MAX = 10
        self._ATK = 2
        self._DEF = 4
        self._color = Color.GREEN
        
        # Init Knight actions
        self._actions.append(Action(
            "Attack",
            "Slam downward with the ancestral greatsword. Deals 3d6 damage.",
            self.greatsword
        ))
        self._actions.sort(key=lambda action: action.name)
        
    # - - - - - COMBAT - - - - - 
        
        
        
    # - - - - - ACTIONS - - - - -
        
    # TODO: Knight.greatsword()
    def greatsword():
        pass
    
    # TODO: Knight.shield_bash()
    def shield_bash():
        pass
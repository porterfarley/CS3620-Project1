"""
Filename: character.py
Description: Defines Super Class Character
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

import random
from action import *
from color import Color

class Character():
    
    # - - - - - OPERATORS - - - - -
    
    def __init__(self, name: str) -> None:
        self._name = name
        self._user_controlled = False
        self._HP = 20
        self._HP_MAX = 20
        self._MP = 20
        self._MP_MAX = 20
        self._ATK = 0
        self._DEF = 0
        self._actions = []
        self._color = Color.CYAN
        
        # Init Actions
        self._actions.append(Action("Prayer", "Offer a prayer for divine aid. Regains 2d6 HP, costs 10 MP.", self.prayer))
        
    def __str__(self) -> str:
        # Name the ClassType: xx/xx HP || xx/xx MP
        txt = f'{Color.BOLD}{self._color}{self._name}'
        
        if(type(self).__name__ != "Character"):
            txt += f' the {type(self).__name__}'
            
        txt += f'{Color.END}'
        txt += f': {self._HP}/{self._HP_MAX} HP || {self._MP}/{self._MP_MAX} MP'
        return txt 
    
    # - - - - - HEALTH & ACTIONS - - - - -
    
    def change_health(self, diff: int) -> bool:
        """Controls players health by adding diff to current health.
           Also controls player death.

        Args:
            diff (int): Value to add to health. Use negative diff to subtract from health.

        Returns:
            bool: True if character died. False if character still alive.
        """
        self._HP += diff
        
        if(self._HP > self._HP_MAX):
            self._HP = self._HP_MAX
            
        if(self._HP <= 0):
            self.die()
            return True
        else:
            return False
            
    def roll_to_hit(self) -> int:
        return random.randint(1, 20)
    
    def roll_to_defend(self) -> int:
        return random.randint(1, 20)
        
    # TODO: better death text
    def die(self) -> None:
        if(not self._user_controlled):
            print(f"  > {self.get_name(True)} has been slain.")
        else:
            print(f"  > Your vision begins to turn red and your breath becomes shallow.")
            print(f"  > Fear envelopes you. The deed has been done.")
            print(f"  > {self.get_name(True)} has been slain.")
            input("\nPress enter to continue.")
            exit(0)     
    
    # - - - - - ACTIONS - - - - -
     
    def prayer(self):
        if(self.MP - 10 < 0):
            return False
        else:
            # Spend MP and roll for healing
            self.MP -= 10
            healing = random.randint(1, 6) + random.randint(1, 6)
            self.change_health(healing)
                
            return True
        
    
    # - - - - - GETTERS - - - - -
    
    def get_name(self, color: bool) -> str:
        txt = f'{Color.BOLD}{self._color}{self._name}{Color.END}' if color else self._name
        return txt
    
    def get_user_controlled(self) -> bool:
        return self._user_controlled
    
    def get_HP(self):
        return self._HP
    
    def get_HP_MAX(self):
        return self._HP_MAX
    
    def get_MP(self):
        return self._MP
    
    def get_MP_MAX(self):
        return self._MP_MAX
    
    def get_ATK(self):
        return self._ATK
    
    def get_DEF(self):
        return self._DEF
    
    def get_actions(self):
        return self._actions
    
    # - - - - - SETTERS - - - - -
    
    def set_user_controlled(self, user_controlled: bool) -> None:
        self._user_controlled = bool
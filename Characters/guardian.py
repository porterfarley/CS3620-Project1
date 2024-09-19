"""
Filename: Guardian.py
Description: Defines Guardian class
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 09/18/2024
"""

from .character import Character
from action import Action
from combat import *
from color import Color

class Guardian(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self._HP = 30
        self._HP_MAX = 30
        self._MP = 30
        self._MP_MAX = 30
        self._ATK = 2
        self._DEF = 0
        self._color = Color.RED
        
        # Init Guardian Actions
        self._actions.clear()
        self._actions.append(Action(
            "Smash",
            "Smashes down with a giant fist of darkness.",
            self.attack
        ))
        self._actions.append(Action(
            "Shadow Blizzard",
            "A dark form of the Blizzard spell.",
            self.shadow_blizzard
        ))
        self._actions.append(Action(
            "Shadow Spike",
            "A dark spike emerges from the ground, attempting to impale the target.",
            self.shadow_spike
        ))
        
    def __str__(self) -> str:
        # Name the ClassType: xx/xx HP || xx/xx MP
        txt = f'{Color.BOLD}{self._color}{self._name}{Color.END}'
        txt += f': {self._HP}/{self._HP_MAX} HP || {self._MP}/{self._MP_MAX} MP'
        return txt 
        
    def attack(self, enemies: list[Character]) -> None:
        DICE = 4
        NUM_DICE = 3
        ACTION_NAME = "Smash"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
        
    def shadow_blizzard(self, enemies: list[Character]) -> None:
        """Uses events.attack() to attempt 2d6 dmg at 5 MP Cost.

        Args:
            enemies (list[Character]): List of all enemies
        """
        
        from combat import attack
        
        MP_COST = -10
        DICE = 6
        NUM_DICE = 2
        ACTION_NAME = "Shadow Blizzard"
        
        # Action Print
        print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
        
        # Break statement for not having enough MP to cast
        if(not self.change_MP(MP_COST)):
            time.sleep(0.5)
            print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
            time.sleep(0.5)
            print(f"  > NOTICE: Too little MP To cast {ACTION_NAME}.")
            time.sleep(0.5)
            print(f"  > Little more than snowflakes fly from thier fingertips. Their enemies are unfazed.")
        else:
            
            # Identify if user controlled to get opponent
            if self._user_controlled:
                opponent = self.get_user_opponent(enemies)
            else:
                opponent = self.get_cpu_opponent(enemies)
                
            attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
        
    def shadow_spike(self, enemies: list[Character]) -> None:
        from combat import attack
        
        DICE = 6
        NUM_DICE = 2
        ACTION_NAME = "Shadow Spike"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
    
    def get_cpu_action(self) -> Action:
        import random
        
        choice = random.random()
        if choice >= 0.80 and self._MP > 10:
            return self.get_action_by_name("Shadow Blizzard")
        elif choice < 0.8 and choice >= 0.50:
            return self.get_action_by_name("Shadow Spike")
        else:
            return self.get_action_by_name("Smash")
        
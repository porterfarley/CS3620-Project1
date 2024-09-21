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
        self._actions.pop()
        self._actions.append(Action(
            "Attack",
            "Slash with poisoned dagger. Deals 2d8 damage.",
            self.attack
        ))
        self._actions.append(Action(
            "Critical Strike",
            "Teleport through the shadows, landing a lethal blow on an opponent. Roll w/ +2 to hit, deals 6d6 + ATK damage, costs 20 MP.",
            self.sneak_attack
        ))
        self._actions.sort(key=lambda action: action.name)

    # - - - - - ACTIONS - - - - -
    def attack(self, enemies: list[Character]) -> None:
        
        from combat import attack
        
        DICE = 8
        NUM_DICE = 2
        ACTION_NAME = "Attack"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
    
    def get_cpu_action(self) -> Action:
        import random
        
        curr_HP = self.get_HP()
        curr_MP = self.get_MP()
        
        should_heal = random.random()
        
        if(curr_HP <= self.get_HP_MAX()/3 and curr_MP > 25 and should_heal >= 0.4):
            return self.get_action_by_name("Prayer")
        else:
            choice = random.random()
            
            if choice > 0.5 and curr_MP >= 20:
                return self.get_action_by_name("Critical Strike")
            else:
                return self.get_action_by_name("Attack")
    
    def sneak_attack(self, enemies: list[Character]) -> None:
        
        from combat import attack
        import time
        
        MP_COST = -20
        DICE = 6
        NUM_DICE = 6
        ACTION_NAME = "Sneak Attack"
            
        # +2 to ATK for action
        curr_ATK = self.get_ATK()
        self._ATK += 2
        
        # Break statement for not having enough MP to cast
        if(not self.change_MP(MP_COST)):
            time.sleep(0.5)
            print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
            time.sleep(0.5)
            print(f"  > NOTICE: Too little MP To cast {ACTION_NAME}.")
            time.sleep(0.5)
            print(f"  > Shadows swirl at their feet, but fail to engulf them. No attack is made.")
        else:
            # Identify if user controlled to get opponent
            if self._user_controlled:
                opponent = self.get_user_opponent(enemies)
            else:
                opponent = self.get_cpu_opponent(enemies)
            
            # Attack
            attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
        
        # Remove ATK Bonus
        self._ATK = curr_ATK
"""
Filename: LordOfDeath.py
Description: Defines LordOfDeath class
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 09/18/2024
"""

from .character import Character
from action import Action
from combat import *
from color import Color

class LordOfDeath(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self._HP = 75
        self._HP_MAX = 75
        self._MP = 60
        self._MP_MAX = 60
        self._ATK = 3
        self._DEF = -1
        self._color = Color.PURPLE
        
        # Init LordOfDeath Actions
        self._actions.clear()
        self._actions.append(Action(
            "Smash",
            "Smashes down with a giant fist of bones.",
            self.attack
        ))
        self._actions.append(Action(
            "Bone Barrage",
            "Shoots bone shards at high speeds at target. Does 3 separate attacks for 1d6 each.",
            self.bone_barrage
        ))
        self._actions.append(Action(
            "Life Drain",
            "Dark energy lunges from your fingertips and sucks the life out of the target. If attack hits, halves target's HP.",
            self.life_drain
        ))
        self._actions.append(Action(
            "Magic Drain",
            "Dark energy lunges from your fingertips and sucks the magic out of the target. If attack hits, halves target's MP.",
            self.magic_drain
        ))
        self._actions.sort(key=lambda action: action.name)
        
    # - - - - - COMBAT - - - - - 
    def get_cpu_action(self) -> Action:
        import random
        
        choice = random.random()
        
        if choice >= 0.82 and self._MP >= 30:
            return self.get_action_by_name("Life Drain")
        elif choice >= 0.65 and self._MP >= 30:
            return self.get_action_by_name("Magic Drain")
        elif choice < 0.65 and choice >= 0.30:
            return self.get_action_by_name("Bone Barrage")
        else:
            return self.get_action_by_name("Smash")
        
    # - - - - - ACTIONS - - - - - 
    def attack(self, enemies: list[Character]) -> None:
        from combat import attack
        
        DICE = 6
        NUM_DICE = 2
        ACTION_NAME = "Attack"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
        
    def bone_barrage(self, enemies: list[Character]) -> None:
        from combat import attack
        
        DICE = 6
        NUM_DICE = 1
        ACTION_NAME = "Bone Barrage"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        for i in range(3):
            attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
            
    def life_drain(self, enemies: list[Character]) -> None:
        from combat import attack
        
        ACTION_NAME = "Life Drain"
        MP_COST = -30
        
        if(self.change_MP(MP_COST)):
            if self._user_controlled:
                opponent = self.get_user_opponent(enemies)
            else:
                opponent = self.get_cpu_opponent(enemies)
                
            DICE = opponent.get_HP() / 2
            NUM_DICE = 1
        
            attack(self, opponent, enemies, DICE, NUM_DICE, "Life Drain")
        else:
            time.sleep(0.25)
            print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
            time.sleep(0.25)
            print(f"  > NOTICE: Too little MP to cast {ACTION_NAME}")
            time.sleep(0.25)
            print(f"  > The dark energy forming in your hands is unstable, and dissapates. No attack is made.")
            
    def magic_drain(self, enemies: list[Character]) -> None:
        
        ACTION_NAME = "Magic Drain"
        MP_COST = -30
        
        if(self.change_MP(MP_COST)):
            if self._user_controlled:
                opponent = self.get_user_opponent(enemies)
            else:
                opponent = self.get_cpu_opponent(enemies)
            
            print(f"  > {self.get_name(True)} uses {ACTION_NAME} on {opponent.get_name(True)}")
                
            to_hit = self.roll_to_hit()
            print(f"  > {self.get_name(True)} rolls {to_hit} + {self.get_ATK()} to hit.")
            to_hit += self.get_ATK()
            
            to_defend = opponent.roll_to_defend()
            print(f"  > {opponent.get_name(True)} rolls {to_defend} + {opponent.get_DEF()} to defend.")
            to_defend += self.get_DEF()
            
            if to_hit >= to_defend:
                diff = (opponent.get_MP()/2)
                opponent.set_MP(0-diff)
                print(f"  > {self.get_name(True)} successfully drains {diff} MP from {opponent.get_name(True)}")
                
            else:
                print(f"  > {opponent.get_name(True)} successfully defends against {self.get_name(True)}'s {ACTION_NAME}")
                
        else:
            time.sleep(0.25)
            print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
            time.sleep(0.25)
            print(f"  > NOTICE: Too little MP to cast {ACTION_NAME}")
            time.sleep(0.25)
            print(f"  > The dark energy forming in your hands is unstable, and dissapates. No attack is made.")
            
    def get_name(self, color: bool) -> str:
        txt = f'{Color.BOLD}{self._color}{self._name}, Lord of Death{Color.END}' if color else self._name
        return txt
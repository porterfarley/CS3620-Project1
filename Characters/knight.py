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
import random
import time

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
        self._actions.pop()
        self._actions.append(Action(
            "Attack",
            "Slam downward with the ancestral greatsword. Deals 2d8 damage.",
            self.attack
        ))
        self._actions.sort(key=lambda action: action.name)
        
    # - - - - - COMBAT - - - - - 
    
    # Overrides the Character's on_defend() to handle shield bash
    def on_defend(self, attacker: Character) -> None:
        self.shield_bash(attacker)
        
    # - - - - - ACTIONS - - - - -
    def attack(self, enemies: list[Character]) -> None:
        
        from events import attack
        
        DICE = 8
        NUM_DICE = 2
        ACTION_NAME = "Attack"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
    
    # TODO: Knight.shield_bash()
    def shield_bash(self, attacker: Character) -> None:
        """Defensive maneuver on successful block. Automatically hits. Does
        1d6 damage, and cannot kill.

        Args:
            attacker (Character): The character that had initially tried to attack. Or in other words
               the target of the Shield Bash.
        """
        
        DICE = 6
        NUM_DICE = 1
        ACTION_NAME = "Shield Bash"
        
        # Print initial action
        time.sleep(0.5)
        print(f"  > {self.get_name(True)} uses {ACTION_NAME} on {attacker.get_name(True)}.")
        
        # Get Damage Dice
        dmg = 0
        for i in range(NUM_DICE):
            dmg += random.randint(1, DICE)
            
        # If attack would kill, leave at 1 HP Instead
        attacker_HP = attacker.get_HP()
        if attacker_HP - dmg <= 0:
            attacker.change_HP(1-attacker_HP)
        else:
            attacker.change_HP(-dmg)
            
        # Print results
        time.sleep(0.5)
        print(f"  > {self.get_name(True)} deals {dmg} damage to {attacker.get_name(True)}.")
        time.sleep(0.5)
        print(f"  > {attacker.get_name(True)} New HP: {attacker.get_HP()}/{attacker.get_HP_MAX()} HP")
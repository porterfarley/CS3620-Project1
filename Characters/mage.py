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
            "Hurl a raging ball of flame that automatically hits all opponents. Deals 4d6 damage, costs 20 MP.", 
            self.fireball
        ))
        self._actions.sort(key=lambda action: action.name)
        
    def fireball(self, enemies: list[Character]) -> None:
        """Wizard special attack that automatically hits every enemy, doing
        2d12 damage, costs 20 MP.

        Args:
            enemies (list[Character]): Collection of all enemies to cast the spell at.
        """
        import random
        
        MP_COST = 20
        DICE = 12
        NUM_DICE = 2
        ACTION_NAME = "Fireball"
        
        # Action Print
        print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
        
        # Break statement for not being able to cast the spell
        if(not self.change_MP(-MP_COST)):
            time.sleep(0.5)
            print("  > NOTICE: Too little MP to cast Fireball.")
            time.sleep(0.5)
            print("  > Their strained magic fails to generate much more than sparks. Their enemies are unfazed.")
            return None
        
        # Get damage roll
        dmg = self._ATK
        for i in range(NUM_DICE):
            dmg += random.randint(1, DICE)
            
        # Show what happens
        time.sleep(0.5)
        print(f"  > {self.get_name(True)} feels the magic surge from every inch of their body to their hands.")
        time.sleep(0.5)
        print(f"  > Their staff glows a furious crimson as a sphere of flame soars from the top, enveloping all enemies.")
        time.sleep(0.5)
        print(f"  > {self.get_name(True)} deals {str(dmg)} to all enemies.")
        
        # Do the dmg to each enemy
        slain_enemies = []
        for i in range(len(enemies)):
            if enemies[i].change_HP(-dmg):
                slain_enemies.append(enemies[i])

        # Remove all slain enemies
        for enemy in slain_enemies:
            enemies.remove(enemy)
    
    
    def attack(self, enemies: list[Character]):
        
        DICE = 6
        NUM_DICE = 1
        ACTION_NAME = "Attack"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
    
    
    
        
    
    def blizzard(self, enemies: list[Character]) -> None:
        """Uses events.attack() to attempt 2d6 dmg at 5 MP Cost.

        Args:
            enemies (list[Character]): List of all enemies
        """
        
        MP_COST = 5
        DICE = 6
        NUM_DICE = 2
        ACTION_NAME = "Blizzard"
        
        # Action Print
        print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
        
        # Break statement for not having enough MP to cast
        if(not self.change_MP(-MP_COST)):
            time.sleep(0.5)
            print(f"  > {self.get_name(True)} casts Blizzard.")
            time.sleep(0.5)
            print(f"  > NOTICE: Too little MP To cast Blizzard.")
            time.sleep(0.5)
            print(f"  > Little more than snowflakes fly from thier fingertips. Their enemies are unfazed.")
        else:
            
            # Identify if user controlled to get opponent
            if self._user_controlled:
                opponent = self.get_user_opponent(enemies)
            else:
                opponent = self.get_cpu_opponent(enemies)
                
            attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
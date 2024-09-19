"""
Filename: HonoredOne.py
Description: Defines HonoredOne class
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 09/18/2024
"""

from .character import Character
from action import Action
from combat import *
from color import Color

class HonoredOne(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self._HP = 50
        self._HP_MAX = 50
        self._MP = 60
        self._MP_MAX = 60
        self._ATK = 3
        self._DEF = 3
        self._color = Color.CYAN
        
        # Init HonoredOne Actions
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
        self._actions.append(Action(
            "Enhanced Blizzard",
            "Cast a barrage of icy shards. Deals 3d6 damage, costs 5 MP.",
            self.blizzard
        ))
        self._actions.append(Action(
            "Fireball", 
            "Hurl a raging ball of flame that automatically hits all opponents. Deals 4d6 damage, costs 20 MP.", 
            self.fireball
        ))
        self._actions.sort(key=lambda action: action.name)
    
    def __str__(self) -> str:
        txt = f"{Color.BOLD}{self._color}{self._name} The Honored One{Color.END}"
        txt += f": {self._HP}/{self._HP_MAX} HP || {self._MP}/{self._MP_MAX} MP"
        return txt
    
    
    # - - - - - COMBAT - - - - - 
    
    # Overrides the Character's on_defend() to handle shield bash
    def on_defend(self, attacker: Character) -> None:
        self.shield_bash(attacker)
    
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
            time.sleep(0.25)
            print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
            time.sleep(0.25)
            print(f"  > NOTICE: Too little MP To cast {ACTION_NAME}.")
            time.sleep(0.25)
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
        time.sleep(0.25)
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
        time.sleep(0.25)
        print(f"  > {self.get_name(True)} deals {dmg} damage to {attacker.get_name(True)}.")
        time.sleep(0.25)
        print(f"  > {attacker.get_name(True)} New HP: {attacker.get_HP()}/{attacker.get_HP_MAX()} HP")
        
        
    def fireball(self, enemies: list[Character]) -> None:
        """Wizard special attack that automatically hits every enemy, doing
        2d12 damage, costs 20 MP.

        Args:
            enemies (list[Character]): Collection of all enemies to cast the spell at.
        """
        import random
        
        MP_COST = -20
        DICE = 6
        NUM_DICE = 3
        ACTION_NAME = "Fireball"
        
        # Action Print
        print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
        
        # Break statement for not being able to cast the spell
        if(not self.change_MP(MP_COST)):
            time.sleep(0.25)
            print("  > NOTICE: Too little MP to cast Fireball.")
            time.sleep(0.25)
            print("  > Their strained magic fails to generate much more than sparks. Their enemies are unfazed.")
            return None
        
        # Get damage roll (3d6 + 3)
        dmg = 3
        for i in range(NUM_DICE):
            dmg += random.randint(1, DICE)
            
        # Show what happens
        time.sleep(0.25)
        print(f"  > {self.get_name(True)} feels the magic surge from every inch of their body to their hands.")
        time.sleep(0.25)
        print(f"  > Their staff glows a furious crimson as a sphere of flame soars from the top, enveloping all enemies.")
        time.sleep(0.25)
        print(f"  > {self.get_name(True)} deals {str(dmg)} to all enemies.")
        
        # Do the dmg to each enemy
        slain_enemies = []
        for i in range(len(enemies)):
            if enemies[i].change_HP(-dmg):
                slain_enemies.append(enemies[i])

        # Remove all slain enemies
        for enemy in slain_enemies:
            enemies.remove(enemy)
            
    def blizzard(self, enemies: list[Character]) -> None:
        """Uses events.attack() to attempt 2d6 dmg at 5 MP Cost.

        Args:
            enemies (list[Character]): List of all enemies
        """
        
        from combat import attack
        
        MP_COST = -5
        DICE = 6
        NUM_DICE = 3
        ACTION_NAME = "Enhanced Blizzard"
        
        # Action Print
        print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
        
        # Break statement for not having enough MP to cast
        if(not self.change_MP(MP_COST)):
            time.sleep(0.25)
            print(f"  > {self.get_name(True)} casts {ACTION_NAME}.")
            time.sleep(0.25)
            print(f"  > NOTICE: Too little MP To cast {ACTION_NAME}.")
            time.sleep(0.25)
            print(f"  > Little more than snowflakes fly from thier fingertips. Their enemies are unfazed.")
        else:
            
            # Identify if user controlled to get opponent
            if self._user_controlled:
                opponent = self.get_user_opponent(enemies)
            else:
                opponent = self.get_cpu_opponent(enemies)
                
            attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
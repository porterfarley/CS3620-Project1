"""
Filename: character.py
Description: Defines Super Class Character
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

import random
import time
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
        self._actions.append(Action(
            "Prayer", 
            "Offer a prayer for divine aid. Regains 2d6 HP, costs 10 MP.", 
            self.prayer
        ))
        self._actions.append(Action(
            "Attack",
            "Swing with a generic weapon.",
            self.attack
        ))
        
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
            
    def get_user_action(self) -> Action:
        """Gets user input and selects the Character's Action

        Args:
            user (Character): User's character

        Returns:
            Action: The Action the player selected
        """
        
        from events import exit_program
        
        # Gets all actions
        actions = self.get_actions()
        
        # Loops until valid input taken
        while True:
            for action in actions:
                print(f'  > {str(action)}')
            
            choice = input("  > Your Action: ")
            # print(f'  > User wrote: {choice}')
            
            # Break statement to end game at any time
            if(choice.upper() == "EXIT_PROGRAM"):
                exit_program()
            
            actions = self.get_actions()
            for action in actions:
                if(choice.upper() == action.name.upper()):
                    time.sleep(1)
                    return action
            
            time.sleep(1)
            print("  > Not a valid choice. Please try again.")
            
    def get_user_opponent(self, enemies: list["Character"]) -> "Character":
        """Gets user input and selects enemy out of the list.

        Args:
            enemies (list[Character]): List of all possible targets.

        Returns:
            Character: Enemy being selected.
        """
        
        from events import exit_program
        
        while True:
            print("  > Select your target:")
            for i in range(len(enemies)):
                print(f"     - {str(i+1)}) {str(enemies[i])}")
            choice = input("  > Target: ")
            
            # Break statement to end game at any time
            if choice.upper() == "EXIT_PROGRAM":
                exit_program()
            
            # Handle user entering a number
            if choice.isdigit():
                choice = int(choice) - 1
                
                if choice < len(enemies) and choice >= 0:
                    return enemies[choice]
                else:
                    print("  > Not a valid choice. Please try again.")
                    continue
            else:
                for i in range(len(enemies)):
                    if (enemies[i].get_name(False).upper() == choice.upper()):
                        return enemies[i]
                print("  > Not a valid choice. Please try again.")
                continue
    
    def get_cpu_action(self) -> Action:
        if self._HP <= self._HP_MAX/3 and self._MP >= 10:
            return self.get_action_by_name("Prayer")
        else:
            return self.get_action_by_name("Attack")
        
    def get_cpu_opponent(self, enemies: list["Character"]) -> "Character":
        return enemies[random.randint(0, len(enemies)-1)]
    
    # - - - - - ACTIONS - - - - -
     
    def prayer(self):
        
        time.sleep(0.5)
        print(f"  > {self.get_name(True)} casts Prayer.")
        time.sleep(0.5)
        
        if(self._MP < 10):
            print(f"  > {self.get_name(True)} doesn't have enough MP, and the prayer has no effect.")
        else:
            # Spend _MP and roll for healing
            self._MP -= 10
            healing = random.randint(1, 6) + random.randint(1, 6)
            self.change_health(healing)
            print(f"  > A trickle of sunlight sprinkles from the sky onto {self.get_name(True)}")
            time.sleep(0.5)
            print(f"  > {self.get_name(True)} heals for {healing} HP.")
            time.sleep(0.5)
        
    def attack(self, enemies: list["Character"]):
        
        from events import attack
        
        DICE = 6
        NUM_DICE = 1
        ACTION_NAME = "Attack"
        
        if self._user_controlled:
            opponent = self.get_user_opponent(enemies)
        else:
            opponent = self.get_cpu_opponent(enemies)
            
        attack(self, opponent, enemies, DICE, NUM_DICE, ACTION_NAME)
    
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
    
    def get_action_by_name(self, name: str) -> Action:
        for act in self.get_actions():
            if act.name == name: return act
        return None
    
    # - - - - - SETTERS - - - - -
    
    def set_user_controlled(self, user_controlled: bool) -> None:
        self._user_controlled = bool
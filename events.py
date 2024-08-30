"""
Filename: events.py
Description: Defines events within the game
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

import time
from Characters.character import *

INVALID_CHOICE_TEXT = "  > Not a valid choice. Please try again."

def exit_program():
    print("Sucks to suck")
    exit(0)

def get_user_action(user: Character) -> Action:
    """Gets user input and selects the Character's Action

    Args:
        user (Character): User's character

    Returns:
        Action: The Action the player selected
    """
    
    # Gets all actions
    actions = user.get_actions()
    
    # Loops until valid input taken
    while True:
        for action in actions:
            print(f'  > {str(action)}')
        
        choice = input("Your Action: ")
        # print(f'  > User wrote: {choice}')
        
        # Break statement to end game at any time
        if(choice.upper() == "EXIT_PROGRAM"):
            exit_program()
        
        actions = user.get_actions()
        for action in actions:
            # print(f'     - Action Checked: {action.name[0].upper()}|{action.name.upper()}')
            if(choice.upper() == action.name.upper()):
                time.sleep(1)
                return action
        
        time.sleep(1)
        print(INVALID_CHOICE_TEXT)
    
def get_user_opponent(enemies: list[Character]) -> Character:
    """Gets user input and selects enemy out of the list.

    Args:
        enemies (list[Character]): List of all possible targets.

    Returns:
        Character: Enemy being selected.
    """
    
    while True:
        print("Select your target")
        for i in range(len(enemies)):
            print(f"  > {str(i+1)}) {str(enemies[i])}")
        choice = input("Target: ")
        
        # Break statement to end game at any time
        if choice.upper() == "EXIT_PROGRAM":
            exit_program()
        
        # Handle user entering a number
        if choice.isdigit():
            choice = int(choice) - 1
            
            if choice < len(enemies) and choice >= 0:
                return enemies[choice]
            else:
                print(INVALID_CHOICE_TEXT)
                continue
        else:
            for i in range(len(enemies)):
                if (enemies[i].get_name(False).upper() == choice.upper()):
                    return enemies[i]
            print(INVALID_CHOICE_TEXT)
            continue
        
def attack(attacker: Character, defender: Character, enemies: list[Character], dice: int, num_dice: int, action_name: str):
    
    # Print action
    time.sleep(0.5)
    print(f"  > {attacker.get_name(True)} uses {action_name} on {defender.get_name(True)}")

    # Print attacker's roll
    to_hit = attacker.roll_to_hit()
    time.sleep(0.5)
    print(f"  > {attacker.get_name(True)} rolls {str(to_hit)} + {str(attacker.get_ATK())} to hit.")
    
    # Print defender's roll
    to_defend = defender.roll_to_defend()
    time.sleep(0.5)
    print(f"  > {defender.get_name(True)} rolls {str(to_defend)} + {str(defender.get_DEF())} to defend.")
    
    # Add bonuses
    to_hit += attacker.get_ATK()
    to_defend += defender.get_DEF()
    
    # Handle hit attack
    if(to_hit >= to_defend):
        # Crit mechanics
        if to_hit - attacker.get_ATK() == 20:
            # Get dmg num 
            dmg = attacker.get_ATK() * 2
            for i in range(num_dice*2):
                dmg += random.randint(1, dice+1)
            
            # Print attack details
            time.sleep(0.5)
            print(f"  > {attacker.get_name(True)} scores a critical hit on {defender.get_name(True)}, dealing {dmg}.")
        
        # Normal hit mechanics
        else:
            # Get dmg num
            dmg = attacker.get_ATK()
            for i in range(num_dice):
                dmg += random.randint(1, dice+1)
            
            # Print attack details
            time.sleep(0.5)
            print(f"  > {attacker.get_name(True)} deals {dmg} to {defender.get_name(True)}.")
        
        # Apply damage. If defender killed, remove from enemies.
        time.sleep(0.5)
        if(defender.change_health(-dmg)):
            enemies.remove(defender)
        
    else:
        time.sleep(0.5)
        print(f"  > {defender.get_name(True)} successfully defends against {attacker.get_name(True)}'s {action_name}.")

        
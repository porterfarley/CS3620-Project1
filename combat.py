"""
Filename: combat.py
Description: Defines combat events within the game
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

import time
from Characters import *
import random

def exit_program():
    print("Sucks to suck")
    exit(0)
        
def attack(attacker: Character, defender: Character, enemies: list[Character], dice: int, num_dice: int, action_name: str) -> None:
    """Handles the attack event.
        1) Handles all the printing of actions used
        2) Handles all dice rolling, including doubling attack damage for 20's rolled
        3) Calls defender.change_health() if attack successful. Removes defender from enemies if killed.

    Args:
        attacker (Character): Attacking Character. Can be user_controlled or !user_controlled
        defender (Character): Defending Character. Can be user_controlled or !user_controlled
        enemies (list[Character]): Collection of enemies. Modified if defender is killed.
        dice (int): Highest number on the damage dice. i.e. 6 would be a d6, giving values from 1-6 inclusive.
        num_dice (int): How many of the above dice to roll.
        action_name (str): Name of the action being done for printing purposes.
    """
    
    # Print action
    time.sleep(0.25)
    print(f"  > {attacker.get_name(True)} uses {action_name} on {defender.get_name(True)}")

    # Print attacker's roll
    to_hit = attacker.roll_to_hit()
    time.sleep(0.25)
    print(f"  > {attacker.get_name(True)} rolls {str(to_hit)} + {str(attacker.get_ATK())} to hit.")
    
    # Print defender's roll
    to_defend = defender.roll_to_defend()
    time.sleep(0.25)
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
                dmg += random.randint(1, dice)
            
            # Print attack details
            time.sleep(0.25)
            print(f"  > {attacker.get_name(True)} scores a critical hit on {defender.get_name(True)}, dealing {dmg} damage.")
        
        # Normal hit mechanics
        else:
            # Get dmg num
            dmg = attacker.get_ATK()
            for i in range(num_dice):
                dmg += random.randint(1, dice)
            
            # Print attack details
            time.sleep(0.25)
            print(f"  > {attacker.get_name(True)} deals {dmg} damage to {defender.get_name(True)}.")
        
        # Apply damage. If defender killed, remove from enemies.
        if(defender.change_HP(-dmg)):
            enemies.remove(defender)
        else:
            time.sleep(0.25)
            print(f"  > {defender.get_name(True)} New HP: {defender.get_HP()}/{defender.get_HP_MAX()} HP")
        
    else:
        time.sleep(0.25)
        print(f"  > {defender.get_name(True)} successfully defends against {attacker.get_name(True)}'s {action_name}.")
        defender.on_defend(attacker)


def combat(allies: list[Character], enemies: list[Character], combat_text: str, user_order: int) -> bool:
    """Handles combat turns

    Args:
        allies (list[Character]): user and all allies
        enemies (list[Character]): all enemies
        combat_text (str): Text to print as combat is starting
        user_order (int): Handles the user's spot in turns. -1 = last, 1 = first, else = random.
        
    Returns:
        bool: True if character died. False if character still alive.
    """
    
    from inspect import signature
    from events import next
    
    # Find and save user Character
    for i in range(len(allies)):
        if allies[i].get_user_controlled:
            user = allies[i]
            break
        
    # Get random initative order
    all_characters = allies + enemies
    random.shuffle(all_characters)
    
    # Add user to the back of initiative
    if user_order == -1:
        all_characters.remove(user)
        all_characters.append(user)
    # Add user to the front of initiative
    elif user_order == 1:
        all_characters.remove(user)
        all_characters.insert(0, user)
    
    # Print initial combat text
    time.sleep(0.25)
    print(combat_text)
    next()
    
    # Print the Initiative Order
    time.sleep(0.25)
    print("\nInitative Order")
    for i in range(len(all_characters)):
        time.sleep(0.25)
        print(f"  > {i+1}) {str(all_characters[i])}")
    print()
    
    i = 0
    while len(enemies) > 0 and len(allies) > 0:
        # Gets character who's up
        up_next = all_characters[i]
        
        # Pass character if character dead
        if up_next.get_HP() <= 0:
            
            if i + 1 == len(all_characters):
                i = 0
            else:
                i += 1
            continue
        
        # Print character's name
        time.sleep(0.25)
        print(str(up_next))
        
        # Get users action and target
        if up_next.get_user_controlled():
            action = up_next.get_user_action()
            num_params = len(signature(action.on_call).parameters)
            if(num_params == 1):
                action.on_call(enemies)
            else:
                action.on_call()
                
        # Get CPU Action and Target        
        else:
            # Get CPU Action
            action = up_next.get_cpu_action()
            
            # Determine if ally or enemy by searching through allies
            targets = allies
            for x in allies:
                if x == up_next: targets = enemies

            # Call action.
            num_params = len(signature(action.on_call).parameters)
            if(num_params == 1):
                action.on_call(targets)
            else:
                action.on_call()
        
        # End statement for i
        if i + 1 == len(all_characters):
            i = 0
        else:
            i += 1
        
        # Make user click enter to continue. Allows for exit_program
        if input("  > Press enter to continue: ").upper() == "EXIT_PROGRAM":
            exit_program()
        print()
        
        # Check user alive and confirm want to restart
        if user.get_HP() <= 0 and user_died():
            user.rest()
            return True
    
    return False
    
def user_died() -> bool:
    from events import prompt
    
    print()
    choices = ["Continue From Last Chapter", "Exit Game"]
    choice = prompt("You have been defeated. What would you like to do?", choices)
    
    if choice == 0:
        return True
    else:
        exit_program()

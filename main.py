"""
Filename: main.py
Description: Variety of printed functionality
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

from inspect import signature
from Characters import *
from events import *

def main():
    
    print()
    
    # dude1 = Character("dude1")
    # print(str(dude1))
    # for action in dude1.get_actions():
    #     print("  > " + str(action))
        
    # print()
    
    enemies = [
        Goblin("Goblin 1"),
        Goblin("Goblin 2"),
    ]
    
    mindgoblin = Goblin("Mind Goblin")
    enemies.append(mindgoblin)
    
    dragon = Character("Young Blue Dragon")
    dragon.change_health(-4)
    enemies.append(dragon)
    
    for i in range(len(enemies)):
        enemies[i].change_health(-6)
    
    mage1 = Mage("Gandalf")
    mage1.set_user_controlled(True)
    
    allies = [mage1]
    combat_text = "\nThe battle begins!"
    combat(allies, enemies, combat_text, 1)
    
    # # Gandalf's Action
    # print(str(mage1))
    # action = mage1.get_user_action()
    # num_params = len(signature(action.on_call).parameters)
    # if(num_params == 1):
    #     action.on_call(enemies)
    # else:
    #     action.on_call()
    
    # # Show Status'
    # print()
    # print(str(mage1))
    # for i in range(len(enemies)):
    #     print(str(enemies[i]))
    # print()
    
    # # Young Blue Dragon's Action
    # action = dragon.get_cpu_action()
    # num_params = len(signature(action.on_call).parameters)
    # if(num_params == 1):
    #     action.on_call(allies)
    # else:
    #     action.on_call()
        
    # # Show Status'
    # print()
    # print(str(mage1))
    # for i in range(len(enemies)):
    #     print(str(enemies[i]))
    # print()
    
    # # Young Blue Dragon's Action
    # action = dragon.get_cpu_action()
    # num_params = len(signature(action.on_call).parameters)
    # if(num_params == 1):
    #     action.on_call(allies)
    # else:
    #     action.on_call()
        
    
    # # Mind Goblin's Action
    # action = mindgoblin.get_cpu_action()
    # num_params = len(signature(action.on_call).parameters)
    # if(num_params == 1):
    #     action.on_call(allies)
    # else:
    #     action.on_call()
    
    # print()
    
    # knight1 = Knight("Aragorn")
    # print(str(knight1))
    # for action in knight1.get_actions():
    #     print("  > " + str(action))
        
    # print()
    
    # assassin1 = Assassin("Loki")
    # print(str(assassin1))
    # for action in assassin1.get_actions():
    #     print("  > " + str(action))
        
    # print()
    
    
if __name__ == "__main__":
    main()
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
        Goblin("Mind Goblin"),
        Goblin("Young Blue Dragon")
    ]
    
    for i in range(len(enemies)):
        enemies[i].change_health(-6)
    
    mage1 = Mage("Gandalf")
    mage1.set_user_controlled(True)
    
    allies = [mage1]
    combat_text = "\nThe battle begins!"
    combat(allies, enemies, combat_text, 0)
    
    # while True:
    #     print(str(mage1))
    #     action = get_user_action(mage1)
    #     numParams = len(signature(action.on_call).parameters)
    #     if(numParams == 1):
    #         action.on_call(enemies)
    #     else:
    #         action.on_call()
        
    #     print()
    #     print(str(mage1))
    #     for i in range(len(enemies)):
    #         print(str(enemies[i]))
    #     print()
        
    #     if(len(enemies) == 0):
    #         break
        
    # mage1.change_health(-1000)
    
        
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
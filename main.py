"""
Filename: main.py
Description: Variety of printed functionality
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

from inspect import signature
from Characters import *
from combat import *
from color import Color

def main():
    
    # gandalf = Mage("Gandalf")
    # gandalf.set_user_controlled(True)
    
    # saruman = Mage("Saruman")
    # saruman.set_color(Color.RED)
    
    # allies = [gandalf]
    # enemies = [saruman]
    # combat_text = "The battle begins!"
    # combat(allies, enemies, combat_text, 1)
    
    # print("\nCombat Finished")
    
    sung_jin_woo = Assassin("Sung Jin-Woo")
    sung_jin_woo.set_user_controlled(True)
    allies = [sung_jin_woo]
    
    redmage1 = Mage("Red Mage 1")
    redmage1.set_color(Color.RED)
    
    goblin1 = Goblin("Goblin 1")
    goblin2 = Goblin("Goblin 2")
    goblin3 = Goblin("Goblin 3")
    
    enemies = [redmage1, goblin1, goblin2, goblin3]
    
    combat_text = "Assassin Battle Test 1"
    combat(allies, enemies, combat_text, 1)
    
    
    
if __name__ == "__main__":
    main()
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
    
    aragorn = Knight("Aragorn")
    aragorn.set_user_controlled(True)
    allies = [aragorn]
    
    redknight1 = Mage("Red Knight 1")
    redknight1.set_color(Color.RED)
    enemies = [redknight1]
    
    combat_text = "Knight Battle Test 1"
    combat(allies, enemies, combat_text, 1)
    
    
    
if __name__ == "__main__":
    main()
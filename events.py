"""
Filename: events.py
Description: Defines events within the game
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 09/01/2024
"""

from color import Color
from Characters import *
from typing import Union
import time

def intro() -> None:
   
    # Print Title
    print("Hello, and welcome to")
    time.sleep(0.5)
    print()
    print("...")
    time.sleep(0.5)
    print()
    file = open("art.txt", "r").read().splitlines()
    title_spot = False
    for line in file:        
        if line == "START_TITLE_SCREEN":
            title_spot = True
            continue
        elif line == "END_TITLE_SCREEN":
            break
    
        if title_spot:
            print(line)
            
    # Print Start Dialogue
    time.sleep(0.5)
    print()
    print("...")
    time.sleep(0.5)
    print()
    txt([f"To begin the game, press enter to continue:"])
    
    # Print Dialogue Enter tip
    txt(f"{Color.DARKGREY}(TIP: Whenever you see the {Color.END}{Color.YELLOW}▼ {Color.END}{Color.DARKGREY}icon, press enter to continue.){Color.END}")

def character_creation() -> Character:
    opener1 = ["What a strange feeling,",
            "",
            "...",
            "",
            "To feel something again.",
            "",
            "...",
            "",
            "You haven't felt anything in a long time.",
            "",
            "...",
            "",
            "The darkness feels cold against your...",
            "",
            "...",
            "",
            "Skin. Where is your skin?",
            "",
            "...",
            "",
            "For that matter, where is your body?"]
    txt(opener1)
    
    opener2 = ["You go to look down, though neither head nor eyes move,",
               "and where you would normally find yourself,",
               "only swirling black vapor occupies the space.",
               "",
               "You were sure there used to be a body there before."]
    txt(opener2)
    
    opener3 = ["Below where you're standing,",
               "or where you would be standing if you had a body,",
               "is what appears to be a large stained glass window.",
               "The only source of light within the darkness,",
               "it is curious looking indeed.",
               "",
               "The center, where you find yourself, lies equally between",
               "three circular panes, beautifully crafted.",
               "",
               ""]
    txt(opener3)
    

# - - - - - - - U T I L I T I E S - - - - - - - 

def next() -> None:
    if input(f"{Color.YELLOW}▼ {Color.END}").upper() == "EXIT_PROGRAM":
        from combat import exit_program
        exit_program()
    else:
        print()
        return None
    
def txt(text: Union[str, list[str]]) -> None:
    if isinstance(text, str):
        time.sleep(0.5)
        print(text)
    elif isinstance(text, list):
        for line in text:
            time.sleep(0.5)
            print(line)
    next()
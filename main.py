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
from events import *

def main():
    
    story_0_intro()
    player = story_0_character_creation()
    next_story = story_0(player)
    while(callable(next_story)):
        next_story = next_story(player)
    
if __name__ == "__main__":
    main()
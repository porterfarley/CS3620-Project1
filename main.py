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

    #intro()
    #player = character_creation()
    # player = Knight("Porter")
    # next_story = story_0(player)
    
    # while(callable(next_story)):
    #     next_story = next_story(player)
        
    player = Knight("Satoru")
    story_1_start(player)
        
    print("All Done")
    
if __name__ == "__main__":
    main()
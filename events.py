"""
Filename: events.py
Description: Defines events within the game
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 09/01/2024
"""

from color import Color
from Characters import *
from combat import combat
from typing import Union
import time

def intro() -> None:
    
    from combat import exit_program
    
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
    print(f"To begin the game, press enter to continue:")
    
    while True:
        # Handles ADMIN_MODE and EXIT_PROGRAM
        intro_text = input(f"{Color.YELLOW}▼ {Color.END}")
        if intro_text.upper() == "EXIT_PROGRAM":
            from combat import exit_program
            exit_program
        elif intro_text.upper() == "ADMIN_MODE":
            if input("  > Password: ") == "100324":
                # Get Character to put in the game
                name = input("  > Name: ")
                class_type = prompt("What class would you like to use?", ["Knight", "Mage", "Assassin"])
                if class_type == 0:
                    player = Knight(name)
                elif class_type == 1: 
                    player = Mage(name)
                else:
                    player = Assassin(name)
                    
                # Get mission
                while True:
                    story = "story_" + input("  > Story Module: ")
                    
                    try:
                        story_module = globals()[story]
                        story_module(player)
                        break
                    except:
                        if story.upper() == "STORY_EXIT_PROGRAM":
                            exit_program()
                        else:
                            print("  > Not valid module. Try again.")
            else:
                print("  > Incorrect password. Moving forward in game.")
                break
        
        # General Break Statement
        break
    
    # Print Dialogue Enter tip
    txt(f"{Color.DARKGREY}(TIP: Whenever you see the {Color.END}{Color.YELLOW}▼ {Color.END}{Color.DARKGREY}icon, press enter to continue.){Color.END}")
    return character_creation

def character_creation() -> Character:
    
    from prettytable import PrettyTable
    
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
               "three circular panes of magnificent craftmanship.",
               "Each pane holds a weapon of some kind, and you can't help",
               "but feel something inside reaching out to them."
               "",]
    txt(opener3)
    
    opener4 = ["The first circle you notice contains an image of an oak staff.",
               "Around it, you find the glass is actually swirling, the visages",
               "of fire and ice dance playfully around the staff's tip.",
               "",
               "The second pane is filled with a sturdy steel shield in front of",
               "A forest of tall pine trees. It glistens from where you look. You", 
               "feel confidence and sturdiness swell within you looking at it.",
               "",
               "Finally, the third looks to be covered in some kind of liquid.",
               "Closer inspection reveals a tawny poison, dripping from a coated",
               "dagger emerging from the shadows.",
               ""]
    txt(opener4)
    
    opener5 = ["As you go to reach out for any pane, where you know your arm",
               "used to be is now only flickers of a vaguely human form.",
               "",
               "Each pane seems to hum as you make any approach towards it at all,",
               "almost as if they call for you, praying your hand."]
    txt(opener5)
    
    txt(f"{Color.DARKGREY}(TIP: When making game decisions, you can type either the number or the text option,\n then press enter to select your choice.){Color.END}")
    
    choices = ["The Staff", "The Shield", "The Dagger"]
    
    while True:
        choice = prompt("Which pane will you reach for?", choices)
        
        # Staff
        if choice == 0:
            time.sleep(0.5)
            print("The elements excite as you move closer and the fire grows brighter.")
            time.sleep(0.5)
            print("The magic feels familiar, and you feel a faint image show in your mind.")
            
            time.sleep(0.5)
            print()
            print_art("MAGE")
            print()
            
            table = PrettyTable()
            table.max_width = 100
            table.field_names = ["Class", "HP", "MP", "ATK", "DEF", "Special"]
            table.add_row([f"{Color.BLUE}Mage{Color.END}", "15", "40", "-1", "2", f"{Color.UNDERLINE}Fireball{Color.END}: Hurl a raging ball of flame that automatically hits all opponents. Deals 4d6 damage, costs 20 MP."])
            
            time.sleep(0.5)
            print(table)
            print()
            
            select_class = prompt("By choosing the Path of the Mage, you select these attributes.",
                                ["Select the Path of the Mage", "Maybe Not Yet"])
            
            if select_class == 0:
                time.sleep(0.5)
                txt(["The staff flies from the glass itself into your hand, crackling with power.",
                    "The fire create a beautiful pillar of light around you,",
                    "as flowing blue robes appear over your shoulders and around your head."])
                
                player = Mage("Player")
                break
            else:
                continue
        
        elif choice == 1:
            time.sleep(0.5)
            print("The pine trees blow in a real wind as you approach.")
            time.sleep(0.5)
            print("Resolution swells within you and you see an image appear in your mind.")
            
            time.sleep(0.5)
            print()
            print_art("KNIGHT")
            print()
            
            table = PrettyTable()
            table.max_width = 100
            table.field_names = ["Class", "HP", "MP", "ATK", "DEF", "Special"]
            table.add_row([f"{Color.GREEN}Knight{Color.END}", "30", "10", "+2", "+4", f"{Color.UNDERLINE}Shield Bash{Color.END}: After successfully blocking an attack, bash with your shield for 1d6 unblockable damage, though it cannot kill."])
            
            time.sleep(0.5)
            print(table)
            print()
            
            select_class = prompt("By choosing the Path of the Knight, you select these attributes.",
                                ["Select the Path of the Knight", "Maybe Not Yet"])
            
            if select_class == 0:
                time.sleep(0.5)
                txt(["You are able to draw the shield right from the glass itself,",
                    "and to sling it around your arm. The forest seems to salute",
                    "you as armor begins to form around your joints and a large helmet",
                    "covers your face."])
                
                player = Knight("Player")
                break
            else:
                continue
    
        elif choice == 2:
            time.sleep(0.5)
            print("The shadows nip at the edge of the poison pool as you approach.")
            time.sleep(0.5)
            print("An eerie pride fills your chest and you see an image appear in your mind.")
            
            time.sleep(0.5)
            print()
            print_art("Assassin")
            print()
            
            table = PrettyTable()
            table.max_width = 100
            table.field_names = ["Class", "HP", "MP", "ATK", "DEF", "Special"]
            table.add_row([f"{Color.ORANGE}Assassin{Color.END}", "20", "20", "+4", "-1", f"{Color.UNDERLINE}Critical Strike{Color.END}: Teleport through the shadows, landing a lethal blow on an opponent. Roll w/ +2 to hit, deals 6d6 + ATK damage, costs 20 MP."])
            
            time.sleep(0.5)
            print(table)
            print()
            
            select_class = prompt("By choosing the Path of the Assassin, you select these attributes.",
                                ["Select the Path of the Assassin", "Maybe Not Yet"])
            
            if select_class == 0:
                txt(["An eerie whistle sounds and the dagger flies straight to your oustretched hand.",
                    "Dark leather begins to hide your form, covering even your face.",
                    "The shadows from the pool rush to join your growing shadow, ready to do your bidding."])
                
                player = Assassin("Player")
                break
            else:
                continue
    
    text = ["Your decision made, a brief flash of greed strikes, and you wonder",
            "if you can grab the other weapons as well.",
            "",
            "Before you have the chance to move, the darkness arounds you seems to",
            "buzz. Two yellow, pupiless eyes appear immediately in front of you.",
            "",
            "The voice behind the eyes is neither spoken, nor heard, merely",
            "understood within your own mind."]
    txt(text)
    
    shadow = bbg("???")
    
    text = ["...",
            "...",
            "O ye fallen one, consider yourself worthy of The Honored One's Powers?",
            "...",
            "...",
            "That is yet to be seen."]
    character_txt(shadow, text)
    
    time.sleep(0.5)
    print(f"{Color.BOLD}{Color.UNDERLINE}{shadow.get_name(True)}: What is thy name, warrior?")
    time.sleep(0.5)
    name = input(f"  > {Color.DARKGREY} Your answer:{Color.END} ")
    print()
    
    player.set_name(name)
    time.sleep(0.5)
    text = [f"Well then {player.get_name(True)}, prepare to prove thyself.",
            "take up thy weapon and fall not to the shadows, that ye may",
            "rise in a better light."]
    character_txt(shadow, text)
    
    player.set_user_controlled(True)
    
    enemies = [enemy("Shadow 1"),
               enemy("Shadow 2"),
               enemy("Shadow 3")]
    allies = [player]
    
    txt([f"{Color.DARKGREY}(TIP: You are about to enter combat. Combat only ends if you are defeated,",
         "of if all enemies are defeated. Turns are determined randomly and represented by initiative order.",
         f"On your turn, type the number or the action name of the action you'd like to take.){Color.END}"])
    
    combat(allies, enemies, "Shadows suddenly begin to stir all around you. Eyes appear, and slender\nfaceless humanoid figures run from the shadows, directly at you.", 1)
    
    txt("The last shadow dissapates as you finish it off. Then, the air begins to vibrate once more.")
    
    character_txt(shadow, "Do not delight in thyself, warrior. You are far from the honor you yet seek.")
    
    enemies = [shadow]
    player.set_user_controlled(False)
    allies = [player]
    combat(allies, enemies, "Around the eyes materializes a dark figure with spikes rising from his head.\nOne great step rocks the great glass pane, and it swings at you with an outstretched fist.", -1)
    
    player.rest()
    player.set_user_controlled(True)
    return player
    
def story_0(player: Character) -> callable:
    
    txt(["Your eyes shoot open. You were sure you were done for from that...",
         "that monster? Where is it? Where is everything from where you were?"])
    
    necro = Mage("???")
    necro.set_color(Color.PURPLE)
    character_txt(necro, "Oh! You're finally awake I see, that took much longer than normal. On your feet now.")
    
    txt(["The person in front of you wears a deep purple Mage's robe, with wrappings",
         "that cover head to toe. Two pin pricks of yellow light poke through",
         "the darkness where their face should be. The robes cover what appears to be",
         "a quite old and slender frame. Their voice has an eerie eveness that makes it",
         "almost impossible to tell a thing about them."])
    
    character_txt(necro, ["I'm sure you're disoriented, but I don't have time to tell you everything.",
                          "The goblins are already on us. Make your questions quick."])
    
    choices = ["Where am I?", "Who are you?", "What happened to me?", "Continue"]
    x = prompt("What do you say?", choices)
    
    while (x != len(choices)-1):
        if x == 0:
            character_txt(necro, ["The Goblins' front porch. They were planning to march on the capital,",
                                  "we would have lost thousands if we hadn't gotten here first. We're about 2 kilometers",
                                  "out from their castle walls. And running out of warriors, I might add, which is why",
                                  "we called you up."])
        elif x == 1:
            necro.set_name("Tvashtri")
            character_txt(necro, [f"You can call me {necro.get_name(True)}. I'm his royal highness' wizard. I'm also the",
                                  "reason you're breathing once more. Well, maybe not breathing, but you get the picture."])
        elif x == 2:
            character_txt(necro, ["Can't say. You, and the rest, are warriors for the kingdom, protecting our people",
                                  "and the kingdoms' interests. I called you up to keep fighting."])
            character_txt(necro, ["You won't remember anything from the past, but it's a blessing you don't. Your",
                                  "memories, your body, all sacrifices for the people."])
            
        x = prompt("What do you say?", choices)
    
    if type(player).__name__ == "Knight":
        return story_1_0
    elif type(player).__name__ == "Mage":
        return story_2_0
    elif type(player).__name__ == "Assassin":
        return story_3_0
    else:
        raise NotImplementedError

# TODO: story_1_0  
def story_1_0(player: Character) -> callable:
    print("Got to story_1_0")

# TODO: story_2_0  
def story_2_0(player: Character) -> callable:
    print("Got to story_2_0")

# TODO: story_3_0  
def story_3_0(player: Character) -> callable:
    print("Got to story_3_0")

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
    
def character_txt(speaker: Character, text: Union[str, list[str]]) -> None:
    if isinstance(text, str):
        time.sleep(0.5)
        print(f"{Color.BOLD}{Color.UNDERLINE}{speaker.get_name(True)}: " + text)
    elif isinstance(text, list):
        for i in range(len(text)):
            time.sleep(0.5)
            if i == 0:
                print(f"{Color.BOLD}{Color.UNDERLINE}{speaker.get_name(True)}: " + text[i])
            else:
                print((" " * len(speaker.get_name(False))) + "  " + text[i])
    next()
    
def prompt(prompt: str, choices: list[str]) -> int:
    while True:
        time.sleep(0.5)
        print(prompt)
        
        for i in range(len(choices)):
            time.sleep(0.5)
            print(f"  > " + str(i+1) + ") " + choices[i])
            
        user_choice = input(f"  > {Color.DARKGREY}Your Choice:{Color.END} ")
        
        if user_choice.upper() == "EXIT_PROGRAM":
            from combat import exit_program
            exit_program()
        
        if user_choice.isdigit():
            user_choice = int(user_choice)-1
            if user_choice < len(choices) and user_choice >= 0:
                print()
                return user_choice
            else:
                time.sleep(0.5)
                print("  > Not a valid choice. Please try again.")
                print()
                continue
        else:
            for i in range(len(choices)):
                if user_choice.upper() == choices[i].upper():
                    print()
                    return i
            time.sleep(0.5)
            print("  > Not a valid choice. Please try again.")
            print()
            continue
        
def character_prompt(speaker: Character, prompt: str, choices: list[str]) -> int:
    while True:
        time.sleep(0.5)
        print(f"{Color.BOLD}{Color.UNDERLINE}{speaker.get_name(True)}: {prompt}")
        
        for i in range(len(choices)):
            time.sleep(0.5)
            print(f"  > " + str(i+1) + ") " + choices[i])
            
        user_choice = input(f"  > {Color.DARKGREY}Your Choice:{Color.END} ")
        
        if user_choice.upper() == "EXIT_PROGRAM":
            from combat import exit_program
            exit_program()
        
        if user_choice.isdigit():
            user_choice = int(user_choice)-1
            if user_choice < len(choices) and user_choice >= 0:
                print()
                return user_choice
            else:
                time.sleep(0.5)
                print("  > Not a valid choice. Please try again.")
                print()
                continue
        else:
            for i in range(len(choices)):
                if user_choice.upper() == choices[i].upper():
                    print()
                    return i
            time.sleep(0.5)
            print("  > Not a valid choice. Please try again.")
            print()
            continue
        
def print_art(title: str) -> None:
    title = title.upper()
    file = open("art.txt", "r").read().splitlines()
    found_art = False
    for line in file:        
        if line == ("START_" + title):
            found_art = True
            continue
        elif line == ("END_" + title):
            break
    
        if found_art:
            print(line)
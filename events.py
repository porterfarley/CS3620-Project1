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

def story_0_intro() -> None:
    
    from combat import exit_program
    
    # Print Title
    print("Hello, and welcome to")
    time.sleep(0.25)
    print()
    print("...")
    time.sleep(0.25)
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
    time.sleep(0.25)
    print()
    print("...")
    time.sleep(0.25)
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
                class_type = prompt("What class would you like to use?", ["Knight", "Mage", "Assassin", "Honored One", "Lord of Death", "BBG"])
                if class_type == 0:
                    player = Knight(name)
                elif class_type == 1: 
                    player = Mage(name)
                elif class_type == 2:
                    player = Assassin(name)
                elif class_type == 3:
                    player = HonoredOne(name)
                elif class_type == 4:
                    player = LordOfDeath(name)
                elif class_type == 5:
                    player = bbg(name)
                else:
                    player = Knight(name)
                    
                # Get mission
                while True:
                    story = "story_" + input("  > Story Module: ")
                    print()
                    try:
                        player.set_user_controlled(True)
                        story_module = globals()[story]
                        
                    except Exception as e:
                        if story.upper() == "STORY_EXIT_PROGRAM":
                            exit_program()
                        else:
                            print("  > Not valid module. Try again.")
                            
                    try:
                        story_module = story_module(player)
                        
                        while(callable(story_module)):
                            story_module = story_module(player)
                    except Exception as e:
                        print("\nEncountered error.")
                        print("  > " + str(e))
                        print()
            else:
                print("  > Incorrect password. Moving forward in game.")
                break
        
        # General Break Statement
        break
    
    # Print Dialogue Enter tip
    txt(f"{Color.DARKGREY}(TIP: Whenever you see the {Color.END}{Color.YELLOW}▼ {Color.END}{Color.DARKGREY}icon, press enter to continue.){Color.END}")
    return story_0_character_creation

def story_0_character_creation() -> Character:
    
    from prettytable import PrettyTable
    
    opener1 = ["What a strange feeling,",
            "...",
            "To feel something again.",
            "...",
            "You haven't felt anything in a long time.",
            "...",
            "The darkness feels cold against your...",
            "...",
            "Skin. Where is your skin?",
            "...",
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
               "a forest of tall pine trees. It glistens from where you look. You", 
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
            time.sleep(0.25)
            print("The elements excite as you move closer and the fire grows brighter.")
            time.sleep(0.25)
            print("The magic feels familiar, and you feel a faint image show in your mind.")
            
            time.sleep(0.25)
            print()
            print_art("MAGE")
            print()
            
            table = PrettyTable()
            table.max_width = 100
            table.field_names = ["Class", "HP", "MP", "ATK", "DEF", "Special"]
            table.add_row([f"{Color.BLUE}Mage{Color.END}", "15", "40", "-1", "2", f"{Color.UNDERLINE}Fireball{Color.END}: Hurl a raging ball of flame that automatically hits all opponents. Deals 4d6 damage, costs 20 MP."])
            
            time.sleep(0.25)
            print(table)
            print()
            
            select_class = prompt("By choosing the Path of the Mage, you select these attributes.",
                                ["Select the Path of the Mage", "Maybe Not Yet"])
            
            if select_class == 0:
                time.sleep(0.25)
                txt(["The staff flies from the glass itself into your hand, crackling with power.",
                    "The fire create a beautiful pillar of light around you,",
                    "as flowing blue robes appear over your shoulders and around your head."])
                
                player = Mage("Player")
                break
            else:
                continue
        
        elif choice == 1:
            time.sleep(0.25)
            print("The pine trees blow in a real wind as you approach.")
            time.sleep(0.25)
            print("Resolution swells within you and you see an image appear in your mind.")
            
            time.sleep(0.25)
            print()
            print_art("KNIGHT")
            print()
            
            table = PrettyTable()
            table.max_width = 100
            table.field_names = ["Class", "HP", "MP", "ATK", "DEF", "Special"]
            table.add_row([f"{Color.GREEN}Knight{Color.END}", "30", "10", "+2", "+4", f"{Color.UNDERLINE}Shield Bash{Color.END}: After successfully blocking an attack, bash with your shield for 1d6 unblockable damage, though it cannot kill."])
            
            time.sleep(0.25)
            print(table)
            print()
            
            select_class = prompt("By choosing the Path of the Knight, you select these attributes.",
                                ["Select the Path of the Knight", "Maybe Not Yet"])
            
            if select_class == 0:
                time.sleep(0.25)
                txt(["You are able to draw the shield right from the glass itself,",
                    "and to sling it around your arm. The forest seems to salute",
                    "you as armor begins to form around your joints and a large helmet",
                    "covers your face."])
                
                player = Knight("Player")
                break
            else:
                continue
    
        elif choice == 2:
            time.sleep(0.25)
            print("The shadows nip at the edge of the poison pool as you approach.")
            time.sleep(0.25)
            print("An eerie pride fills your chest and you see an image appear in your mind.")
            
            time.sleep(0.25)
            print()
            print_art("Assassin")
            print()
            
            table = PrettyTable()
            table.max_width = 100
            table.field_names = ["Class", "HP", "MP", "ATK", "DEF", "Special"]
            table.add_row([f"{Color.ORANGE}Assassin{Color.END}", "20", "20", "+4", "-1", f"{Color.UNDERLINE}Critical Strike{Color.END}: Teleport through the shadows, landing a lethal blow on an opponent. Roll w/ +2 to hit, deals 6d6 + ATK damage, costs 20 MP."])
            
            time.sleep(0.25)
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
            f"O ye fallen one, consider yourself worthy of thyself back?",
            "...",
            "...",
            "That is yet to be seen."]
    character_txt(shadow, text)
    
    time.sleep(0.25)
    print(f"{Color.BOLD}{Color.UNDERLINE}{shadow.get_name(True)}: What is thy name, warrior?")
    time.sleep(0.25)
    name = input(f"  > {Color.DARKGREY} Your answer:{Color.END} ")
    print()
    
    player.set_name(name)
    time.sleep(0.25)
    text = [f"Well then {player.get_name(True)}, prepare to prove thyself.",
            "take up thy weapon and fall not to the shadows."]
    character_txt(shadow, text)
    
    player.set_user_controlled(True)
    
    enemies = [enemy("Shadow 1"),
               enemy("Shadow 2"),
               enemy("Shadow 3")]
    allies = [player]
    
    txt([f"{Color.DARKGREY}(TIP: You are about to enter combat. Combat only ends if you are defeated,",
         "of if all enemies are defeated. Turns are determined randomly and represented by initiative order.",
         f"On your turn, type the number or the action name of the action you'd like to take.){Color.END}"])
    
    battle_text = "Shadows suddenly begin to stir all around you. Eyes appear, and slender\nfaceless humanoid figures run from the shadows, directly at you."
    if combat(allies, enemies, battle_text, 1): return story_0_character_creation
    
    txt("The last shadow dissapates as you finish it off. Then, the air begins to vibrate once more.")
    
    character_txt(shadow, "Do not delight in thyself, warrior. You are far from the honor you yet seek.")
    
    enemies = [shadow]
    player.set_user_controlled(False)
    allies = [player]
    battle_text = "Around the eyes materializes a dark figure with spikes rising from its head.\nOne great step rocks the great glass pane, and it swings at you with a giant, outstretched fist."
    combat(allies, enemies, battle_text, -1)
    
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
        character_txt(player, choices[x])
        
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
        return story_1_start
    elif type(player).__name__ == "Mage":
        return story_2_0
    elif type(player).__name__ == "Assassin":
        return story_3_0
    else:
        raise NotImplementedError

def story_0_captured(player: Character) -> callable:
    
    txt(["You slowly start coming to in a dark, stone room. The walls are",
         "hewn out of dark stone, but look to be very old. Moss sprouts",
         "through every open crack between the slabs. A small, barred window",
         "offers the only light."])
    
    txt(["As you get up, the sound alerts someone on the other side of the",
         "large oak door leading into your cell. A young voice squeeks",
         "from the other side."])
    
    tristan = enemy("Tristan")
    kheah = enemy("Kheah")
    
    character_txt(tristan, ["Oy! You awake in there?"])
    
    choices = ["Hello? Who's there?", "Let me out of here or I'll kill you.", "*Say Nothing*"]
    choice = prompt("What do you say?", choices)
    
    character_txt(player, choices[choice])
    if choice == 0:
        character_txt(tristan, ["Uh, nobody!", "I mean, everybody!", "I mean, a great warrior, that's for sure!", 
                               "I'd be scared if I was you!", "But I'll let you off easy this time, since you're",
                               f"awake, I'll go get {kheah.get_name(True)}!"])
    elif choice == 1:
        character_txt(tristan, ["*jumps*", "*shakily* You couldn't if you tried, I'm a tough warrior mate.",
                               f"But, I'm...retired! Right, I'm retired. So uh...",
                               f"I'll go get {kheah.get_name(True)}, she'll sort you out!"])
    elif choice == 2:
        character_txt(tristan, ["Well.... uh.....",
                               "Are you sure you're not there?",
                               "Oh man, they'll get mad at me if it's a false alarm...",
                               "But I'm NOT going in there...",
                               "Fine, maybe I'll go get her to be sure."])
        character_txt(tristan, ["*knocks on door*",
                               "Hello in there!",
                               "You should probably wake up, I'm going to go get",
                               f"{kheah.get_name(True)}, she's going to interrogate you now!"])
    else:
        raise NotImplementedError
    
    txt(["Little footsteps run hurriedly down the cobblestone hallway.",
        "The boy can't be over 10 years old, and the fear of you was",
        "clear in his voice."])
    
    txt(["You look down at your hands, and thick iron chains keep you",
         "in place and from moving your arms much higher than your waist.",
         "Your weapons are nowhere to be seen. To be a prisoner of war is",
         "a different experience, but you feel a sense of calm. You wonder",
         "if maybe this new form just can't feel anxiety, or if there's a",
         "simple sense that everything is going to turn out fine."])
    
    txt(["After what feels like an hour, you finally hear steps down the",
         "hallway again."])
    
    character_txt(kheah, ["Alright, we're coming to get you out now. You had better not forget",
                          "how bad I got you last time, so don't try anything funny.",
                          "",
                          "I'm going to open the door, I'm going to undo the chains, and then",
                          "we're going to take a walk down to the council chambers. Nice and",
                          "easy."])
    
    txt(["The same woman from before enters the room. She is wrapped in",
         "a pine green robe, her silver eyes glare down at you with deep",
         "mistrust. She draws your attention to her same knife, glistening",
         "with some kind of oil, as if to add more insurance. Then, she",
         "reaches down to the spot you are chained to the floor."])
    
    choice = prompt("Do you do anything?", ["*Comply*", "*Kick her and run for it*"])
    
    if choice == 1:
        from combat import user_died
        
        txt(["The moment the chains come unbolted from the ground,",
             "you spin with all the mobility you have to kick the",
             "woman in the head."])
        txt(["Your foot connects... with her outstretched hand.",
             "She had expected your move the whole time. With a flick",
             "of her arm, you find yourself sprawled out on the ground,",
             "a knife sticking out between your eyes."])
        txt(["Your vision starts to cloud, everything begins to go dark."])
        
        character_txt(kheah, ["You got what you deserved. Good riddance I say.",
                              "*Spits on you*"])
        player.die()
        if user_died(): return story_0_captured
        
    txt(["She leads you by the chains down several flights of stone stairs.",
         "The halls look aged, but more confusing is the complete silence",
         "that attends your hike.",
         "",
         "From time to time you catch the young boy staring at you, as if",
         "both terrified and in awe."])
    
    character_txt(kheah, ["We'll be there soon.",
                          "",
                          "You better know, you're only alive because of her.",
                          "My sister has this theory about you monsters.",
                          "Says you can be reasoned with. You better hope for",
                          "your own sake that's true."])
    
    return story_0_eyma_talk
    
def story_0_eyma_talk(player: Character) -> callable:
    txt(["After one more flight of stairs, you exit through a set of doors",
         "into a huge balcony area. Covered in grass and encircled by large",
         "stone thrones, carved into the natural outcroppings.",
         "On the far side sits a woman, no more than 25, adorned in a royal",
         "blue robe. Her eyes are covered by a white blindfold, yet she still",
         "looks up at you upon your arrival."])
    
    eyma = Mage("Eyma")
    eyma.set_color(Color.RED)
    kheah = Assassin("Kheah")
    tristan = Knight("Tristan")
    character_txt(eyma, ["Ah, you are here. Thank you for coming."])
    
    txt(["You notice something changing about the girl. She begins to glow",
         "softly, a warm golden light that feels inviting. You have not felt",
         "magic like this before. Her eyes, underneath the blindfold, begin",
         "to radiate the same goldent hue, as she stares at you. It feels",
         "almost sacred to be in her presence."])
    
    print_art("EYMA")
    
    eyma.set_color(Color.BLUE)
    kheah.set_color(Color.ORANGE)
    tristan.set_color(Color.GREEN)
    
    character_txt(eyma, [f"My name is {eyma.get_name(True)}, inheritor of my father's throne and newest wielder",
                         f"of the Spark. It has shown me many wonderful things in a world of such sorrow,",
                         f"even visions of hope and possibility. Thank you for coming here."])
    
    character_txt(eyma, [f"You are the one called {player.get_name(True)}, yes? I have seen you",
                         "through the Spark. You need not worry, we will not harm you. I",
                         "believe there are some important things for us to discuss. You",
                         "have undoubtedly lost your memories, a side affect of your \"calling\".",
                         "However, I believe I can help you find them again."])
    
    choices = ["Who are you?", "Why are you at war with us?", "You can help me get my memories back?",
               "Why should I trust you?", "Continue"]
    choice = prompt("What do you say?", choices)
    while choice != len(choices)-1:
        
        character_txt(player, choices[choice])
        
        if choice == 0:
            character_txt(eyma, [f"I am {eyma.get_name(True)}, queen of the people of Yyondril. I believe you",
                                 "have been told that we are called the goblins, yes? It is",
                                 "amusing to hear the schemes the imperials use on their soldiers."])
            character_txt(eyma, ["I wield the Spark, an ancient gift of the Yyondril. It",
                                "is what helped me see you as you truly are, and what guides",
                                "the path forward for my people. It is rare for a female to",
                                "hold it, and provides us our only advantage against the",
                                "imperials."])
        elif choice == 1:
            character_txt(eyma, ["I'm afraid you have much to learn about the current condition of",
                                 "our world.",
                                 "",
                                 "My people are called the Yyondril, natives to these very lands.",
                                 "We have been blessed from the beginning to inherit the Spark, an",
                                 "ancient spiritual gift that allows us to see glimpses into the",
                                 "many possible futures. The Spark comes from the great magic of",
                                 "life itself, and as such has many other powers associated with it",
                                 "as well."])
            character_txt(eyma, ["About 700 years ago, our people lived peacefully secluded in these",
                                 "lands, thriving and being nourished by the light of the Spark.",
                                 "A day came when we began to hear rumors of a foreign, conquering",
                                 "legion, lead by a wizard who could contort the very powers of death",
                                 "itself. Their soldiers were said to be made of darkness, and fought",
                                 "with the strength of the very storms.",
                                 "",
                                 "The rumors stopped when the surviving nations did. About 300 years",
                                 "ago, the imperial assault began on our people. The struggle has been",
                                 "horrific. Scared of the Spark's power, they have sought out and killed",
                                 "almost all of our men, as they are the most likely to receive it.",
                                 f"{tristan.get_name(True)} here is one of the few survivors."])
            character_txt(eyma, ["So, to answer your question, I'm afraid it is not us who is at war with",
                                 "the imperials, but the imperials who are at war with us. We simply wish",
                                 "to preserve our people."])
        elif choice == 2:
            character_txt(eyma, ["Yes, I believe I can. Your life was made forfeit by imperial magic, and",
                                 "I believe you have a right to it again. I believe that my powers are the",
                                 "only ones that may offer you that chance."])
        elif choice == 3:
            character_txt(eyma, ["Hmm... it is justified to ask this. I'm afraid you were brought here in",
                                 "... less than ideal circumstances. You must understand our caution. Your",
                                 "kind have killed many of our people.",
                                 "...",
                                 "Ah, I believe I have a question for you in return then: who else would",
                                 "you trust?",
                                 "",
                                 "Surely being \"called up\", handed a weapon, and pointed in a general",
                                 "direction was not the most trustworthy of beginnings either."])
            character_txt(eyma, ["I'd ask you to hear us out, and make the choice that seems most",
                                 "logical to you. But I'm also afraid that you know more than we can",
                                 "afford to let slip at this time in our fight against the imperials.",
                                 "I will not threaten your life, but I will return you to the cell",
                                 "you were in before until such a time you agree to comply."])
            txt(["The woman's voice holds no malice and doesn't seem to be",
                 "threatening. Instead, her words seem very matter of fact."])
        elif choice == 4:
            break
        else:
            raise NotImplementedError
        
        choice = prompt("What do you say?", choices)
        
    character_txt(player, ["So what does this have to do with me?"])
    
    character_txt(eyma, ["An excellent question indeed, where do you fit into all of this?"])
    
    choices = ["Yes, I did.", "*Say Nothing*"]
    character_prompt(eyma, f"{player.get_name(True)} before you were called up, did you dream of anything?", choices)
    
    character_txt(eyma, ["The Spark shows more than the temporal things; I have seen your",
                   "vision too. Even more, I have seen visions of your past."])
    
    txt([f"{eyma.get_name(True)} begins to glow even more and you can now see the irises of her",
         "eyes through the blindfold. Her voice becomes more authoratative and",
         "a somber feeling fills the air."])
    
    character_txt(eyma, ["Over 1000 years ago, the lands were united together by faith and magic.",
                         "Though separated over great distances, each people shared a portion of",
                         "their gifts with a wise and powerful ruler. The ruler used the shared",
                         "powers to protect every land in the kingdom. They never imposed taxes",
                         "or shared burdens, but helped to create prosperity and shared strength."])
    
    character_txt(eyma, ["Wielding all kinds of magic and weaponry skills, the ruler ensured the",
                         "safety of all of their people. When their time came, they would pass on",
                         "the powers to their successor.",
                         "",
                         "This warrior was revered and beloved by all the people, and soon earned",
                         f"the title of {Color.CYAN}The Honored One{Color.END}."])
    
    tvashtri = enemy("Tvashtri")
    
    character_txt(eyma, [f"About 800 years ago, without warning, {Color.CYAN}The Honored one{Color.END} disappeared.",
                         f"No one knows where the last {Color.CYAN}Honored One{Color.END} went. And unfortunately,",
                         "the Spark can't see that either.",
                         "",
                         f"What I can see, is that 100 years after this, a dark necromancer named {tvashtri.get_name(True)}",
                         "began a march with legions of undead soldiers, wiping out the lands originally under",
                         f"{Color.CYAN}The Honored One{Color.END}'s protection. Surely, this could not have been a mere coincidence."])
    
    character_txt(eyma, [f"And this is where you come in {player.get_name(True)}. You are one of these undead",
                         f"soldiers. I believe that {tvashtri.get_name(True)}'s soldiers are stolen souls from the",
                         f"time of the last {Color.CYAN}Honored One{Color.END}, recycled upon their deaths over and over again.",
                         ""
                         "I apologize if this sounds callous. I can only imagine how I would feel",
                         "if I just found this out for the first time as well. But I believe that",
                         "you, and your fellow compatriots, have been under his command and",
                         "made the ultimate sacrifice an innumerable amount of times in the last",
                         "800 years."])
    
    character_txt(eyma, [f"{player.get_name(True)}, we are losing this war. Before long, my entire",
                         f"people will be wiped out and join {tvashtri.get_name(True)}'s army in a grand march",
                         "to the ends of the world. But I don't believe that we are without hope yet.",
                         "",
                         "You. The Spark has guided me to you, and I believe that you, once",
                         "your memories are unlocked, will be able to help us uncover the",
                         f"secret of {Color.CYAN} The Honored One{Color.END}'s disappearance, and help",
                         "them return once again."])
    
    character_prompt(eyma, "So, will you help us then?", ["Yes"])
    
    character_txt(eyma, ["Wonderful, I am so glad to hear it. Do you remember, from your dream,",
                         "a large, dark figure who fought you? This is the gatekeeper to your",
                         "living self.",
                         ""
                         "A part of the necrotic arts, that monster keeps you from regaining",
                         "your body, your memories, and your own soul back. If you can conquer",
                         "it, then all of that will be yours once more."])
    
    character_txt(eyma, ["I have no doubt that the monster was powerful before, but that is",
                         "where the Spark can assist you."])
    
    print_art("MEDALLION")
    
    txt([f"{eyma.get_name(True)} pulls from her neck a medallion made of tree root.",
         "Holding it in both hands, it begins to glow with the same warm",
         "light that she does."])
    
    character_txt(eyma, ["The power of the Spark will even out the dark powers that made",
                        "the protector so strong the first time. By wearing this, you will",
                        "stand a chance against it. If you can defeat it, you will return here",
                        "with all of yourself back once more."])
    
    choices = ["Yes", "Not yet"]
    choice = character_prompt(eyma, "Are you ready to face it?", choices)
    
    if choice == 0:
        txt([f"{eyma.get_name(True)} walks gracefully over to you and places the medallion",
             "around your neck."])
        character_txt(eyma, f"I wish you luck {player.get_name(True)}.")
        txt(["Your eyelids begin to get heavier and heavier, and you",
             "feel a deep drowsiness coming over you. You fall to your",
             "knees, and then an arcane sleep overtakes you."])
        
    elif choice == 1:
        character_txt(kheah, ["We don't have time to waste on you! Get in there!"])
        txt([f"{kheah.get_name(True)}, with lightning fast reflexes, snags the",
             f"medallion from {eyma.get_name(True)} and slings it around your neck."])
        txt(["Your eyelids begin to get heavier and heavier, and you",
             "feel a deep drowsiness coming over you. You fall to your",
             "knees, and then an arcane sleep overtakes you."])
    else:
        raise NotImplementedError
    
    return story_0_guardian

def story_0_guardian(player: Character) -> callable:
    
    player.rest()
    
    txt(["...",
         "...",
         "..."
         "Your eyes shoot open.",
         "Where are you?",
         "What happened?"])
    
    txt(["All around you is shifting darkness besides the same great",
         "stained glass frame where you stood the last time. From your",
         "neck hangs the same treeroot pendant, glowing with a warm",
         "flicker. It offers the only sense of peace you can feel here."])
    
    txt(["For the first time, you notice the art within the glass pane",
         "where you stand. Between the same circular panes of weapons",
         "is a crown made of marble. It radiates a crisp azure light",
         "that reflects nobility and honor."])
    
    txt(["Suddenly, an unheard voice cuts through your thoughts."])
    
    guardian = bbg("???")
    character_txt(guardian, "Thou hast returned.")
    
    choices = ["My body back.", "I want my memories back!", f"To find out the truth about {Color.CYAN}The Honored One.{Color.END}"]
    choice = character_prompt(guardian, "What seekest thou?", choices)
    
    character_txt(player, choices[choice])
    
    character_txt(guardian, ["What thou seekest hath been made forfeit by thine death.",
                             "Thine rights to it are no longer thine, but mine."])
    
    choices = ["*Brandish the medallion*"]
    choice = prompt("What do you do?", choices)
    
    character_txt(player, choices[choice])
    
    character_txt(guardian, ["I see the power with which thou hast come. If thou provest thyself",
                             "worthy, with this power thou mayest take what thou seekest. Take up",
                             "thy weapon, and fall not to the shadows."])
    
    allies = [player]
    enemies = [enemy("Shadow 1")]
    battle_text = "A single shadow emerges from the floor of the stained\nglass floor and lunges at you."
    if combat(allies, enemies, battle_text, 0): return story_0_guardian
    
    shadow_mage = Mage("Shadow Mage")
    shadow_mage.set_color(Color.RED)
    shadow_mage.set_MP_MAX(20)
    enemies = [enemy("Shadow 1"), enemy("Shadow 2"), shadow_mage]
    battle_text = "As the shadow disolves, three more take its place. One\nholds aloft a great staff of darkness."
    if combat(allies, enemies, battle_text, 0): return story_0_guardian
    
    txt(["With the other foes now vanquished, you feel the medallion",
         "pulse with light, and you feel completely restored to your",
         "full prior strength."])
    
    player.rest()
    
    character_txt(guardian, ["You have done well. Now, thy final test. Thou shalt",
                             "face me. If thou winnest, then shall I grant thee that",
                             "which I have been tasked with protecting."])
    
    txt(["A colossal shadowy figure emerges from the darkness. Two",
        "bright yellow, pupiless eyes shine through. Its head",
        "is adorned with spikes, and it rocks the great glass pane",
        "when it steps down."])
    
    txt(["At the moment it steps down, the medallion pulses once again.",
         "A ray of golden light shines from it onto the creature,",
         "who shrieks in pain. When the ray stops, the monster",
         "has lost nearly half its height, and is now riddles with holes."])
    
    guardian = Guardian("The Guardian")
    allies = [player]
    enemies = [guardian]
    if combat(allies, enemies, f"{guardian.get_name(True)} steps towards you. Now is your chance!", 1): return story_0_guardian
    
    txt([f"{guardian.get_name(True)} falls to one knee, and then down to two. Pieces",
         "of shadow fall like ash from it, and its eyes begin to darken.",
         "",
         "You hear its voice, much softer than before."])
    
    character_txt(guardian, ["Thou hast done well. All that thou seekest, shall be thine."])
    
    txt(["At that moment, somewhere out in the darkness behind it, a single",
         "star begins to shine. It grows brighter, and brighter, until the",
         "light becomes absolutely blinding.",
         "",
         "The whole world goes white for a minute."])
    
    return story_0_honored_one_talk
    
def story_0_honored_one_talk(player: Character) -> callable:
    
    txt(["When the light finally disappates, you find yourself standing in",
         "a beautiful wheat field. Rolling hills surround you, and the",
         "setting sun casts an orange hue across the land. You can feel the",
         "crunch of the plants underneath your feet, and the breeze carries",
         "soft chirps of distant birds."])
    
    txt(["You turn your eyes to where the monster had been, only to find",
         "something completely different there.",
         "",
         "An older man stands before you. He has long white hair and a",
         "beard that hangs below the collar of his white robes. Apart",
         "from his robes, the man wears a steel shield on his back, a",
         "leather belt that sheathes a dagger, and a marble crown.",
         "He doesn't lean on the oak staff in his hand, but sparks",
         "of all colors dance around the top of it.",
         "",
         "What stands out to you most, however, are his eyes. A brilliant",
         "cyan color that seems to twinkle in the sunset. They have an",
         "incredible kindness to them, and when he looks towards you, a",
         "sense of joy and serenity fill you at that moment."])
    
    print_art("HONORED_ONE")
    
    h1 = HonoredOne("The Honored One")
    character_txt(h1, [f"Ah {player.get_name(True)}, it has been too long old friend."])
    
    txt(["As the man embraces you, everything comes flooding back. Of course!",
         "how could you have ever forgotten him!",
         "",
         f"You had been saved by {Color.CYAN}The Honored One{Color.END} from a dragon attack when",
         "you were young. At his request, you returned with him to his",
         f"castle where you studied under him in the path of the {player.get_color()}{type(player).__name__}{Color.END}.",
         "",
         "He was the kindest of men and treated everyone equally. There",
         "was not a member of his court that was lesser than himself, and",
         "no land that he didn't care for."])
    
    txt(["He never gave you his name, nor did he give it to anyone. He",
         "cared for his title, and tried to make sure that everything he",
         "did would reflect on his title so the people could always come",
         f"to trust {Color.CYAN}The Honored One{Color.END}. To him, it was a symbol of peace and",
         "of hope, something he worked everyday to preserve."])
    
    character_txt(h1, ["It is a pleasure to see you again. You should probably see",
                       "yourself again when you can, you'll find yourself returned to",
                       "proper body and form. I'm sure that will be quite pleasant after",
                       "the ordeals you have gone through these many years."])
    
    character_txt(h1, [f"I'm sorry I couldn't protect you more {player.get_name(True)}. To watch",
                       "you and everyone that I love be massacred time and time again",
                       "has been the greatest hell I never knew I could endure.",
                       "",
                       "But no one need worry any longer, you have freed me! And I",
                       "pray that in doing so, you may have freed all of us."])
    
    tvashtri = enemy("Tvashtri")
    
    choices = ["What happened to us?", "Why were you trapped here?", "Continue"]
    choice = character_prompt(h1, "We have a limited time here, but what questions do you have for me?", choices)
    
    while choice != 2:
        
        character_txt(player, choices[choice])
        
        if choice == 0:
            
            character_txt(h1, ["Your memories will continue to return over time, but I'm confident",
                               "I know why you still can't remember that.",
                               "",
                               f"While {Color.CYAN}The Honored One{Color.END} can see a great deal, the magic of darkness",
                               "has powerful concealing abilities. There were rumors of trolls in",
                               "the east countries. Normally an easy encounter, it proved to be",
                               "more challenging than expected when what we arrived to was an army",
                               "of over 100 enraged and bewitched trolls.",
                               "",
                               "We came out victorious, but not without casualties among the high",
                               "court, and not without using most of my own strength as well. When we",
                               "had returned to the castle, I found, waiting in the throne room, the",
                               f"dark necromancer that you know now. They called themseleves {tvashtri.get_name(True)}",
                               f"and told me they had come to steal the powers of {Color.CYAN}The Honored One{Color.END}."])
            
            character_txt(h1, [f"{tvashtri.get_name(True)} unleashed a colossal wave of stored necrotic magic, and",
                               "I knew we had lost. I'm afraid I had little time to react, and",
                               "little strength left, so while I wished I could have saved everyone",
                               "in the castle, I was forced instead to focus on protecting the powers",
                               f"of {Color.CYAN}The Honored One{Color.END}. I hid them deep into the core of my soul, ensuring",
                               "while the necromancer may steal my body, he could never get those",
                               "sacred powers without bringing myself back.",
                               "",
                               f"While the world lost {Color.CYAN}The Honored One{Color.END}, it ensured that they needn't",
                               f"have to fight against {Color.CYAN}The Honored One{Color.END} themselves, a battle that",
                               "would surely be lost."])
        
        elif choice == 1:
            
            character_txt(h1, [f"After hiding the powers deep within my soul, I was forced to wait",
                               f"in that dark place of death. I'm afraid that over time, the dark",
                               "powers corrupted much of my heart. While pieces of myself remained",
                               "intact, I was forced to guard the gate to life again. I was forced",
                               "to watch with horror as the dark wizard continued marching on the",
                               "lands I had loved so dearly."])
            
            character_txt(h1, ["That is, until now. You have done it, and with the magic that you",
                               "brought with you, have gotten your soul back. And now, now you know",
                               "the truth. I believe you can help us end this and bring back hope",
                               "into this bleak world."])
        
        elif choice == 2:
            break
        
        else:
            raise NotImplementedError
        
        choice = character_prompt(h1, "We have a limited time here, but what questions do you have for me?", choices)
    
    character_txt(h1, ["I'm afraid our time is running short my old friend.",
                       "I must ask now for your help. Despite your victory",
                       "and helping me regain myself, I am trapped here. If",
                       f"I return, I will surely be taken by {tvashtri.get_name(True)} before",
                       "I have the chance to act. This must not be allowed to",
                       "happen.",
                       "",
                       "While the world has been devastated already, there is",
                       f"much more that will be lost if {Color.CYAN}The Honored One{Color.END}'s powers",
                       "fall into the hands of the necromancer."])
    
    character_txt(h1, [f"{tvashtri.get_name(True)} must be stopped. And I'm afraid that there is",
                       "no army in the lands that could, at their current",
                       f"strength stand up to the beast. We need {Color.CYAN}The Honored One{Color.END}."])
    
    character_txt(h1, [f"{player.get_name(True)}, it is time for you to take the powers",
                       f"of {Color.CYAN}The Honored One{Color.END}.",
                       "",
                       f"{tvashtri.get_name(True)} will be alerted that someone has broken free. You will",
                       "not have long. But I believe that with the magic you used",
                       f"to come back to this place and the powers of {Color.CYAN}The Honored One{Color.END}",
                       "that you will be able to vanquish the foe and stop this endless",
                       "cycle of blood and death."])
    
    txt(["He looks at you and smiles one last time, then slowly takes",
        "the marble crown from his head and places it on yours. Using",
        "his staff, he draws some runes on the ground next to you."])
    
    character_txt(h1, [f"I now bestow upon you, {player.get_color()}{player.get_name(False)} the {type(player).__name__}{Color.END}, the sacred powers",
                       f"of {Color.CYAN}The Honored One{Color.END}. These powers are a gift passed",
                       "down from generation to generation, containing pieces of the",
                       "magics and gifts of the lands of this kingdom, given in trust",
                       "that the one wielding them would be their protector and shield",
                       "against all that may oppose them. May you always honor them as",
                       "they honor you."])
    
    txt(f"{player.get_name(True)} has become {Color.CYAN}The Honored One{Color.END}")
    player = HonoredOne(player.get_name(False))
    player.set_user_controlled(True)
    txt(str(player))
    
    txt(["The man smiles at you, and his eyes trade their arcane",
         "azure color for a light shade of green. Then, he begins",
         "to fade away before your very eyes."])
    
    character_txt(player, ["Wait! Don't go!"])
    
    character_txt(h1, "Go, and save them all my friend.")
    
    eyma = Mage("Eyma")
    kheah = Assassin("Kheah")
    
    txt(["He disappears into the wind.",
         "",
         "The world begins to lose it's light as the sun sets,",
         "and before you know it, you find yourself right where",
         f"you had fallen aslseep before, with {eyma.get_name(True)}",
         f"and {kheah.get_name(True)} standing above you, waiting for your",
         "return."])
    
    return story_0_tvashtri_setup
    
def story_0_tvashtri_setup(player: Character) -> callable:
    
    eyma = Mage("Eyma")
    kheah = Assassin("Kheah")
    
    tvashtri = enemy("Tvashtri")
    
    txt([f"Before either {eyma.get_name(True)} or {kheah.get_name(True)} have a chance to say",
         "anything, a bright crackling energy begins to circle around you.",
         "The women run back and a deep crack of thunder resounds through",
         "the clearing. Azure light flows into a pillar around you. You",
         "look down at your hands and see that shadow is being replaced by",
         "real human flesh. You watch in awe as your undeath is slowly",
         "replaced with life, and you become the person that you used to be.",
         "You feel your eyes begin to take real form again, followed by",
         "a peculiar warm feeling as they begin to change color as well."])
    
    txt(["Where your apparel was, slowly shifts into a flowing white robe.",
         "You feel a shield placed on your back, a dagger on your belt, and",
         "a staff placed in your hand. Finally, a Marble Crown materializes",
         f"perfectly fitted to you. You have truly become {Color.CYAN}The Honored One{Color.END}.",
         "Power surges through you and you can feel the strength of all those",
         "who came before you and who offered their gifts unto your successors...",
         "",
         "And now, to you."])
    
    txt(["After a period of bewilderment and confusion, you share with the",
         "women what you saw and experienced. When you finish the story,",
         "they ask you several questions about what you are feeling and",
         "what you now remember. After some time and conversation, a subtle",
         "eeriness begins to fill your heart. The words that were spoken to you",
         f"fill your mind, and you remember that {tvashtri.get_name(True)} now knows where",
         "you are.",
         "",
         "A weirder sensation yet, with a little bit of searching your mind",
         f"you find you know exactly where {tvashtri.get_name(True)} is. In the back of",
         "your mind, and with focus, you can see the chamber where the",
         f"necromancer resides. In {Color.CYAN}The Honored One{Color.END}'s castle, where",
         "a marble throne used to be is now a pile of bones reaching high",
         f"into the air, at the top of which, {tvashtri.get_name(True)} has fashioned a",
         "throne of corpses.",
         "",
         "The necromancer seems to be waiting.",
         "",
         "Waiting for you."])
    
    txt(["Before your eyes sprouts a dark, pillar of shadow. A portal.",
         "",
         f"A portal leading right to {tvashtri.get_name(True)}."])
    
    character_txt(eyma, [f"I cannot see what will happen next {player.get_name(True)}. Are",
                         "you sure that you are ready to face this?"])
    
    choices = ["Yes.", "Not sure I have a choice really."]
    choice = prompt("What do you say?", choices)
    
    if choice == 0:
        character_txt(eyma, ["Thank you for being willing to stand. I praise the Spark that",
                             "we were led to a warrior as noble as yourself.",
                             "",
                             "Take the medallion. It may yet do you good."])
    elif choice == 1:
        character_txt(eyma, ["I'm afraid we all lost our choice in this fight sometime ago.",
                             "However, we are profoundly thankful for someone willing to",
                             "stand and fight for those that cannot fight for themselves.",
                             "",
                             "Take the medallion. It may yet do you good in this fight."])
    else:
        raise NotImplementedError
    
    txt(["The time has come.",
         "",
         "You step through the portal."])
    
    txt(["As the darkness closes in behind you and you, you enter a cold,",
         "dark stone throne room. Subtle memories of what this room used",
         "to be add sickening contrast to the decay and rot that fill it now.",
         "",
         "Across the room is the column of bones that you saw before.",
         "Perched at the top, lounging in a carved out ledge, is the same",
         "hooded figure who had raised you earlier this week. Into your",
         "mind flows memories now, however, of countless other lifetimes",
         "waking up to the same figure and being sent out into the battle",
         "field."])
    
    txt(["The silence is cut through by a distored, gravelly voice."])
    
    character_txt(tvashtri, ["So, someone finally found the old man. No matter, now I can take",
                             "from you what I should have taken from him all those years ago."])
    
    choices = ["I'm here to kill you.", "I'm here to talk."]
    choice = character_prompt(tvashtri, "So, what did you hope to gain by coming here?", choices)
    
    character_txt(player, choices[choice])
    
    if choice == 0:
        return story_0_tvashtri_fight
    elif choice == 1:
        return story_0_tvashtri_talk
    else:
        raise NotImplementedError
    
def story_0_tvashtri_fight(player: Character) -> callable:
    
    tvashtri = Mage("Tvashtri")
    tvashtri.set_color(Color.RED)
    
    character_txt(tvashtri, ["You really believe you stand a chance? Need I remind you that",
                             "nations have knelt at my coming, legions have fallen by my hand",
                             "and that even he, the \"Honored One\" could not defend himself,",
                             "nor his court from my arts. Even you have served me for many,",
                             "many years."])
    
    character_txt(tvashtri, ["Do not pretend now to be a hero. You have killed thousands with",
                             "your own hands. Not just the men, but the women, and the children",
                             "too. You slaughtered them like animals.",
                             "",
                             "Yet now you think you can redeem yourself? Redeem yourself by",
                             "killing me no less?",
                             "*laughs*"])
    
    character_txt(tvashtri, ["As you wish.",
                             "And after I kill you—",
                             "I'll be taking your powers with me."])
    
    allies = [player]
    enemies = [tvashtri]
    
    battle_text = f"{tvashtri.get_name(True)} leaps from the make-shift throne with a staff of bones in hand."
    if combat(allies, enemies, battle_text, 0): return story_0_tvashtri_fight
    
    txt([f"With your final attack, {tvashtri.get_name(True)}'s face coverings fall to the floor."])
    
    character_txt(tvashtri, ["*chuckes*",
                             "...", 
                             "...",
                             "If you really want me dead that bad—",
                             "...",
                             "...",
                             "You're going to have to try a lot harder than that."])
    
    txt([f"{tvashtri.get_name(True)} moves to throw off their robes, and for a split second,",
         "the briefest glimpse of an azure vision fills your mind.",
         "",
         f"{tvashtri.get_name(True)} uses the same explosion of stored necrotic magic that",
         "wiped out the entire court 800 years ago. You will die and",
         f"the powers of {Color.CYAN}The Honored One{Color.END} will be stolen."])
    
    choices = ["Grab the medallion"]
    prompt("What do you do?", choices)
    
    txt([f"As you reach for the medallion strung around your neck, {tvashtri.get_name(True)}",
         "throws the purple robes off. The shadow and the yellow eyes that",
         "previously occupied the robe begin to fade away, and standing",
         "in front of you now...",
         "...",
         "is a little girl."])
    
    txt(["Guant faced,",
         "No more than 7 years old,",
         "wearing her black hair in pig tails,",
         "and a black mourning dress."])
    
    txt(["One word escapes her lips:"])
    
    character_txt(tvashtri, "die.")
    
    txt(["An explosion of death rockets from her person in every direction,",
         "shooting fissures through every inch of the marble floor. The shadow",
         "screams towards you faster than you could have ever anticipated.",
         "",
         "You grab the medallion and brace for impact—"])
    
    txt(["...",
         "But the impact never comes.",
         "...",
         "You open your eyes.",
         "...",
         "The darkness rushes around you, but fails to reach you within the",
         "orb of golden light that now surrounds you. The medallion beams",
         "as it continuously exerts this magic power."])
    
    txt(["Moments pass in an eternity, and the dark wave finally ceases.",
         "The golden barrier drops and the tree root medallion shatters."])
    
    tvashtri = LordOfDeath("Tvashtri")
    character_txt(tvashtri, ["You survived? What a pity.",
                             "No one will see my true form and live.",
                             "...",
                             "I'm afraid you've sealed your own fate then.",
                             "...",
                             "You leave me no choice."])
    
    txt(["The girl's airy voice carries a terrifying edge. She turns",
         "from you to the pile of corpses behind her. The bones begin",
         "to wrattle with an awful sound as they scrape together."])
    
    txt(["The bones begin to shoot out from the pile, impaling themselves",
         "into the little girl's arms and legs. Her eyes roll back",
         "into her head as the bones climb together, lifting her higher",
         "and higher into the air."])
    
    print_art("LORD_OF_DEATH")
    
    txt(["Before long, the girl is no longer visible. Before you stands",
         "an awful amalgamation of bone and rotting flesh. Standing over",
         "6 meters high and wielding a club of bone, this monster is truly",
         "horrifying."])
    
    allies = [player]
    enemies = [tvashtri]
    battle_text = "The skeletal monster begins to radiate deep black and \npurple magic, and begins running towards you."
    if combat(allies, enemies, battle_text, 0): return story_0_tvashtri_fight
    
    return story_0_tvashtri_killed
    
# TODO: events.story_0_tvashtri_killed()
def story_0_tvashtri_killed(player: Character) -> None:
    
    tvashtri = LordOfDeath("Tvashtri")
    
    txt(["As you land your final blow, the bone titan shatters",
         "into thousands of fragments, covering the marble floor",
         "in rubble. The girl falls to the ground, where she lays",
         "breathing heavily."])
    
    choices = ["Why did you do it?",
                "Who are you?",
                "How do you live with yourself?"]
    choice = prompt("What do you ask?", choices)
    character_txt(player, choices[choice])
        
    character_txt(tvashtri, ["...",
                                "Years ago, my people had been blessed with power over the",
                                "darkness. Each of us were unique, but our gifts most centered",
                                "on shifting life, like draining a sunflower to heal an arm.",
                                "...",
                                "One day, we were visited by a magic user from a foreign land.",
                                "He called our powers \"Unholy\" and \"Unnatural\".",
                                "...",
                                "He tried to forbid us from using our gifts."])
    
    character_txt(tvashtri, ["...",
                                "He came back many years later, and was appalled that",
                                "we had continued to use our arts.",
                                "...",
                                "There was a prophecy among our people that one day, a child",
                                "would be born with the power over death itself, that by it,",
                                "immortality may be granted to the people."
                                "...",
                                "The man was frightened of our power. So he took matters",
                                "into his own hands."])
    
    character_txt(tvashtri, ["...",
                                "I hid in the woods as that man set fire to everything",
                                "I had ever loved. I was orphaned at the age of 6.",
                                "...",
                                "And I would have forever to live with that hate."])
    
    character_txt(tvashtri, ["...",
                                f"That man became the first {Color.CYAN}Honored One{Color.END}, and I",
                                "became the first person to master arcane immortality.",
                                "...",
                                "I vowed to avenge my people, to take the power that was given",
                                "undeservingly, and to exact my revenge until all have suffered",
                                "as I have."])
    
    character_txt(tvashtri, ["...",
                                "I'm sure you won't understand. Those who die never will.",
                                "...",
                                "But my pain has been eternal...",
                                "Just as my life was supposed to be...",
                                "...",
                                "And that truly breeds an anger no one will ever understand."])
    
    character_txt(tvashtri, ["...",
                             "When the powers slipped from my grasp, the nations",
                             "began to march on this place with armies.",
                             "...",
                             "It was them or me.",
                             "...",
                             "They would soon find I would not fall so easily."])
    
    character_txt(tvashtri, ["...",
                                "I suppose if it must end now, then at least this nightmarish",
                                "existence has finally come to an end.",
                                "...",
                                "And maybe...",
                                "...",
                                "Maybe I'll get to see them, again.",
                                "...",
                                "I'm coming mom."
                                "..",
                                ".",
                                "",
                                ""])
    
    txt([f"{tvashtri.get_name(True)} heaves one final breath, and seems to let go. From",
            "her body rises a tiny, golden flicker. It rises through the roof",
            "to find a patch of soil somewhere beyond the castle walls."])

def story_0_tvashtri_talk(player: Character) -> callable:
    
    tvashtri = Mage("Tvashtri")
    tvashtri.set_color(Color.RED)
    
    character_txt(tvashtri, ["You only delay the inevitable, I will be taking the powers",
                             "you now hold, whether you give them to me willingly or I pry",
                             "them from your lifeless body. Speak, before I lose my patience."])
    
    choices = ["Who are you?",
               "What do you want?",
               "Why have you taken us to war?",
               "Continue"]
    
    choice = prompt("What do you say?", choices)
    while choice != 3:
        
        character_txt(player, choices[choice])
        
        if choice == 0:
            character_txt(tvashtri, ["Who am I? Why, I'm the grand wizard to his royal",
                                     "majesty of course."])
            txt(["The necromancer gestures to a skeleton slumped against the far",
                           "wall. Pieces of a crumbled marble crown still hang to the",
                           "corpse's head."])
        elif choice == 1:
            character_txt(tvashtri, ["To spread the glory of our kingdom everywhere! To show",
                                     "everyone the impermanence of death. To spread this same",
                                     "gift to all the people everywhere!"])
        elif choice == 2:
            character_txt(tvashtri, ["The world thought I was dangerous, so they marched here",
                                     "with their armies, and their mages, and their assassins.",
                                     "",
                                     "They did not stop me. They can't stop me."])
        elif choice == 3:
            break
        else:
            raise NotImplementedError
        
        choice = prompt("What do you say?", choices)
        
    
    character_txt(tvashtri, ["I now have a question for you."])
    
    choices = ["It feels like strength.", "It feels like power.", "It feels like hope."]
    prompt_text = "What do your new powers feel like?"
    choice = character_prompt(tvashtri, prompt_text, choices)
    
    if choice == 0:
        character_txt(tvashtri, ["Then you are just as selfish as any holder ever has been.",
                                 "This is why powers of this nature should never have ended",
                                 "up in the hands of the weak-hearted."])
    elif choice == 1:
        character_txt(tvashtri, ["Then you are just as pitiful as any holder ever has been.",
                                 "This is why the people's power never should have been put",
                                 "in someone who was weak without them."])
    elif choice == 2:
        character_txt(tvashtri, ["Interesting. But what do you seek hope from? Hope in the",
                                 "end of the fighting? Hope in a new life? Or hope you can",
                                 "survive my hand? No matter. Your hope is vain. You are too",
                                 "weak to wield them as they ever should have been."])
    else:
        raise NotImplementedError
    
    character_txt(tvashtri, ["My patience is wearing thin. You came here with a",
                             "purpose, did you not?"])
    
    return story_0_tvashtri_fight

# TODO: story_1_0  
def story_1_start(player: Character) -> callable:
    
    tvashtri = Mage("Tvashtri")
    character_txt(tvashtri, ["No more delays, they need you out there on the front lines.",
                             "The 32nd batallion sent word they needed reinforcements hours ago.",
                             "You'll find them a kilometer north-west of here. Go fast and fight",
                             "for your country."])
    
    txt(["As you exit the wizard's tent, you find only carnage awaiting.",
         "Pools of orange and black liquid pools around strewn corpses."])
    
    choice = 0
    while choice != 2:
        choice = prompt("What do you do?", ["Inspect the Goblins", "Inspect the Knights", "Continue down the Road"])
        
        # Inspect Goblin
        if choice == 0:
            txt(["You're not sure what you were expecting when you heard Goblins,",
                 "but it sure wasn't this.",
                 "",
                 "Before you lies a huddled figure looking all too human. A large",
                 "spear, embedded through her ribs into the ground keeps her from",
                 "ever reaching the grass. The slightest green tint to her skin,",
                 "and a little point to her ears are the only distinguishing",
                 "features from what you'd think is a normal person.",
                 "",
                 "Then again, what would you know about being a normal person",
                 "these days?",
                 "",
                 "The \"Goblin\" woman's face still shows the agony from her final",
                 "moments. Her hand is reaching for something, tucked into her belt.",
                 "Before you have a chance to reach for it, a breeze carries a small,",
                 "white envelope from her hand. You see a scrawling print on it as it",
                 "is carried by the wind far into the fields."])
        
        # Inspect Knight
        elif choice == 1:
            txt(["Where you expected to find a body, you find only a pile of armor",
                "with a sword plunged directly through the breastplate.",
                "The ground around the armor, however, is coated in a shadowy liquid",
                "reminiscent of blood, but much different. It feels more magical",
                "then biological."])
            
            soldier = Knight("Dying Soldier")
            character_txt(soldier, "*groan*")
            
            txt(["You are surprised to see one mass clinging to life and rush to",
                 "his side. Below the waist cannot be found, and shadow slowly",
                 "seeps from where you believe his torso should begin."])
            
            character_txt(soldier, ["*cough*",
                                    "...",
                                    "Is someone there?",
                                    "I can't see anything, it's all going black.",
                                    "..."])
            
            dialogue_options = ["*Grab his hand* I'm here.", "What's happening to you?", "*Stay silent*", "*End His Suffering*"]
            dialogue_choice = prompt("What do you do?", dialogue_options)
            
            if dialogue_choice == 0:
                character_txt(player, dialogue_options[dialogue_choice])
                character_txt(soldier, ["*groan*",
                                        "...",
                                        "Thank you...",
                                        "...",
                                        "I didn't want to die alone...",
                                        "...",
                                        "I think—",
                                        "...",
                                        "I think my memories are starting to come back...",
                                        "...",
                                        "Jane..."])
                txt(["As you hear these words, the man seems to let go."])
            elif dialogue_choice == 1:
                character_txt(player, dialogue_options[dialogue_choice])
                character_txt(soldier, ["*groan*",
                                        "...",
                                        "I'm dying? I think I'm dying.",
                                        "...",
                                        "You think...",
                                        "...",
                                        "It would be a familiar feeeling at this point.",
                                        "...",
                                        "But I think I'm less scared of dying...",
                                        "...",
                                        "And more scared of where I'll wake up next time."])
                txt(["These words send shivers running down your spine.",
                     "What could the man have meant?"])
            elif dialogue_choice == 2:
                character_txt(soldier, ["*groan*",
                                        "If you can hear me...",
                                        "...",
                                        "Run."])
            else:
                txt(["You unsheath your weapon and plunge it into the soldier's helmet.",
                     "However merciful you thought your action, the man screams in one",
                     "last burst of mortal pain."])
                
            txt(["You see a small golden spark float up from the soldier's breastplate.",
                 "The soldier's armor falls as the remnants of his dark form falls apart",
                 "like a cloud as it hits a mountainside. The same black liquid coats",
                 "the ground where the figure touched and the stench of death fills the air.",
                 "",
                 "The small spark flickers in a way that seems... living. It falls like a",
                 "snowflake to the nearest open spot of ground. As it enters the soil,",
                 "the ground glows softly, and a small sapling sprouts before your eyes."])
            
    txt(["As you continue down the road, you reach a cross roads. On your left,",
         "you see the north-west road. From around a bend in the trees rings",
         "steel clashing with steel. On your right, another road curves into",
         "the branches, and a small, worn sign says \"Feldershire\"."])
    
    choice = prompt("Which road do you take?", ["The North-West Road to the Battle", "The Road to Feldershire"])
    if choice == 0:
        return story_1_north_west_road
    elif choice == 1:
        return story_0_feldershire
    else:
        raise NotImplementedError

def story_1_north_west_road(player: Character) -> callable:
    
    txt(["As you turn down the road, the sounds of battle become more",
         "and more anguished. You begin to sprint down the path."])
    
    txt(["Though you know there are more important things right now,",
         "you are amazed that you're not getting tired at all.",
         "The armor doesn't feel heavy, and you're not out of breath.",
         "",
         "Well, you're not even breathing actually."])
    
    txt(["As you turn the corner, you see one remaining knight,",
         "frantically swinging at four large wolf-like creatures, each",
         "lunging and biting ferociously at the warrior. While there are",
         "several downed wolves, the panicked man is oozing black liquid",
         "and losing strength fast."])
    
    soldier1 = Knight("Soldier 1")
    soldier1.change_HP(-18)
    
    character_txt(soldier1, ["Oy, you! Yeah, you! I need your 'elp over 'ere! Quick",
                             "Before these bloody wolves eat the both of us!"])
    
    pack_leader = enemy("Pack Leader")
    pack_leader.set_HP_MAX(20)
    pack_leader.set_HP(20)
    enemies = [enemy("Wolf 1"), enemy("Wolf 2"), enemy("Wolf 3"), pack_leader]
    battle_text = "Some of the wolves begin to eye you warily and then a set of razor sharp fangs comes right for you."
    if combat([soldier1, player], enemies, battle_text, 0): return story_1_north_west_road
    
    if soldier1.get_HP() <= 0:
        txt(["The poor soldier heaves a couple of pained last breaths and is gone.",
             "The armor he was wearing seems to fall apart, and his body disperses",
             "like a cloud. From his chest rises a single golden flicker. It floats",
             "gently down to the ground and in a flash of golden light, a tree sapling",
             "springs up from the ground."])
    else:
        soldier1.set_name("Phil")
        character_txt(soldier1, ["Wasn't that a right bit of melarky right there!? Dang goblins and",
                                 "their dang wolves! I woulda had me arm bitten clean off without",
                                 f"you! I owe you a right debt of gratitude. Me name's {soldier1.get_name(True)}, pleasure",
                                 "to make your acquaintance. If I was you, and we might be, I would",
                                 "get the bloody 'eck outta—"])
        txt([f"The other words never leave his mouth, as {soldier1.get_name(True)} falls dead,",
             "an arrow sticking out of the center of his helmet."])
        
    txt(["With war crys and bows at the ready, a group of 20 goblin women",
         "exit the forest. They stand a little shorter than five feet tall",
         "each, and outside of a slightly greenish tint to their skin and a",
         "little point to their ears, look astoundingly human. Clothed in",
         "makeshift leather armor over commoner's tunics, they glare you",
         "down with a fiery hatred."])
    
    kheah = enemy("Kheah")
    choice = character_prompt(kheah, "DROP YOUR WEAPONS AND SURRENDER! NOW!", ["*Surrender*", "*Run*"])
    if choice == 0:
        
        txt(["You drop your sword, which clatters loudly against the fallen",
             "soldier's armor. A woman runs and kicks your sword out of reach.",
             "The leader walks slowly up to you, pointing her dagger at you.",
             "She scans the battlefield and looks with horror upon the strewn",
             "goblin corpses, then snaps back to you."])
        
        character_txt(kheah, ["You dirty animal. These were people you stole from us today!"])
        
        txt([f"From her belt, {kheah.get_name(True)} retrieves a poultice, into",
             "which she sinks her dagger."])
        
        
        eyma = enemy("Eyma")
        character_txt(kheah, [f"Time to see if this stuff really works {eyma.get_name(True)}."])
        
        txt(["In a flash, the woman is at your side and the dagger slashes",
            "your neck. Pain flashes across your face, but is immediately",
            "drowned out in exhaustion.",
            "",
            "You can't quite keep your eyes open.",
            "",
            "You're falling...",
            "",
            "The last thing you see is the woman standing above you. Her",
            "eyes brimming with a sense of pride, as you slowly drift",
            "into a dreamless sleep."])
        
        return story_0_captured
    elif choice == 1:
        
        txt(["You slowly lower your sword, as if to put it on the ground. In",
            "a flash you leap backwards, rolling over your own shoulder and",
            "twisting, landing right on your feet with scary prowess. Hoisting",
            "your shield to cover your back and neck, you begin cutting and",
            "weaving to avoid the incoming arrow onslaught."])
        
        txt(["You hear the thuds as several arrows are deflected by your shield",
             "and you've almost reached the treeline. However, your shield isn't",
             "large enough to cover your entire body."])
        
        txt(["Right before you reach the cover of the trees, three arrows find",
             "their marks, burying deep into your calves and ankle. You scream,",
             "but manage to keep your footing and make it into the dense brush."])
        
        player.change_HP(-player.get_HP()+1)
        
        txt(["The sounds of bow strings follow through the forest, but none are",
             "getting any closer now. Black liquid oozes from your wounds. After",
             "what feels like several hours, you find yourself right next to a",
             "winding road, and decide to rest behind the cover of trees for a time."])
        
        player.rest()
        
        txt(["You wake up from a short nap and you are completely healed. Your armor",
             "shows the same puncture wounds, but below is just the shadowy form that",
             "is growing more and more normal to see."])
        
        return story_0_feldershire
         
    else:
        raise NotImplementedError

# TODO: story_1_b()
def story_0_feldershire(player: Character) -> callable:
    
    txt(["The trail weaves it's way in and out of the white aspens,",
         "growing more and more run down. No sign of footprints makes",
         "this road even more peculiar."])
    
    txt(["After about an hour of travel, the sound of a branch snapping",
         "cuts through the air."])
    
    txt([f"You flip around to see a {Color.RED}Grizzly Bear{Color.END} walk out",
         "from the foliage."])
    
    allies = [player]
    bear = enemy("Grizzly Bear")
    bear.set_HP_MAX(20)
    bear.set_HP(20)
    bear.set_ATK(3)
    bear.set_DEF(2)
    enemies = [bear]
    battle_text = "It stands up on two legs and lets out a mighty roar."
    if combat(allies, enemies, battle_text, 0): return story_0_feldershire
    
    txt(["As the great beast falls to the forest floor, you let out",
         "a sigh of relief.",
         "",
         "From the light on the trees, you can tell you don't have more",
         "than a couple hours until the sun sets. You'd better not be in",
         "the forest when light runs out, or this won't be your last",
         "encounter with the local wildlife."])
    
    txt(["Gentle breezes cause the leaves to flutter as you pass. The",
         "ocassional wildflower reminds you of the beautiful contrast",
         "of this part of the land to the carnage of the battlefield you",
         "left behind."])
    
    txt(["As the sun begins to drop behind the tree-line, you exit the",
         "forest into a great plain where before you lies an abandoned",
         "town.",
         "",
         "Feldershire looks like it used to be a lumber town, poised",
         "right next to a great supply. The homes and buildings are",
         "built from the same wood, but show great age and weathering."])
    
    txt(["You soon begin to understand the emptiness as you find old",
         "blood stains on sections of the road and even on the outside",
         "of some of the homes.",
         "",
         "The town is rather big, and you have a limited time before",
         "you lose light."])
    
    choices = ["Look for weapons.",
               "Look for armor.",
               "Look for potions."]
    choice = prompt("What do you do?", choices)
    
    if choice == 0:
        
        txt(["Towards where you entered lies a building with a large chimney.",
             "What better place to look then the home of a smith.",
             "",
             "As you go to push the door open, the entire thing falls off of",
             "it's hinges."])
        
        txt(["The bellows has been quiet for some time, and all weapons seem",
             "to have been taken in a hurry. What you do find is a simple whetstone."])
        
        choices = ["Yes", "No"]
        choice = prompt("Do you use the whetstone?", choices)
        
        if choice == 0:
            txt([f"{player.get_name(True)} uses a whetstone.",
                 f"  > {player.get_name(True)}'s ATK increases by 1!",
                 f"  > Old ATK: {player.get_ATK()}",
                 f"  > New ATK: {player.get_ATK() + 1}"])
            player.set_ATK(player.get_ATK() + 1)
        
    elif choice == 1:
        
        txt(["On the east side of town, some of the last tracks",
             "show many individuals running circles around sets of",
             "wooden racks."])
        
        txt(["At the base of one of these racks lies the only remnant",
             "a pair of metal gauntlets, much sturdier than your",
             "current wrappings."])
        
        choices = ["Yes", "No"]
        choice = prompt("Do you equip the gauntlets?", choices)
        
        if choice == 0:
            txt([f"{player.get_name(True)} equips gauntlets.",
                 f"  > {player.get_name(True)}'s DEF increases by 1!",
                 f"  > Old DEF: {player.get_DEF()}",
                 f"  > New DEF: {player.get_DEF() + 1}"])
            player.set_DEF(player.get_DEF() + 1)
        
    elif choice == 2:
        
        txt(["In the center of town, you find a little square, the kind",
             "you'd expect to find merchants at. This area contains a lot",
             "of blood stains, and a great deal of crushed wooden",
             "structures.",
             "",
             "As you walk through, something catches your eye."])
        
        txt(["A small piece of fabric sticks out from the dirt. You reach",
             "down and grab it. Up comes the bright red silk of a doll's",
             "dress.",
             "",
             "As you look at this, a blinding headache rocks you",
             "momentarily, and you can almost see the little girl to whom",
             "this used to belong. As quick as it came, the feeling passes",
             "and you are able to continue down the street."])
        
        txt(["As your feet crunch atop the wreckage of a cart, you hear the",
             "slightest tinkling of glass. You lift up the strewn wood and",
             "find a crate underneath it.",
             "",
             "After carefully removing the crate from the earth, you find",
             "three bottles. Each bottle used to have a label, but age has",
             "worn off any ink that used to be there.",
             "",
             "There is, however, engraved on the side of the box are a cross",
             "a fire emblem, and a skull."])
        
        import random
        
        bottles = ["Health", "Magic", "Death"]
        random.shuffle(bottles)
        
        drank_health_potion = False
        drank_magic_potion = False

        choices = ["Bottle 1", "Bottle 2", "Bottle 3", "None"]
        choice = prompt("Do you drink a potion?", choices)
        
        while choice != len(choices)-1:
            
            if choice == 3:
                
                txt(["You place the crate on the ground, and continue your",
                    "march through town."])
            
            elif bottles[choice] == "Health":
                txt(["The liquid has a soft taste of melon, and it seems to",
                    "coat the insides of your throat as you swallow."])
                txt(["You begin to feel incredible, more alive than you've",
                    "felt since you were called up before."])
                txt([f"{player.get_name(True)} drinks a {Color.GREEN}Health Potion{Color.END}.",
                    f"  > {player.get_name(True)}'s HP increases by 10!",
                    f"  > Old HP: {player.get_HP_MAX()}",
                    f"  > New HP: {player.get_HP_MAX() + 10}"])
                player.set_HP_MAX(player.get_HP_MAX() + 10)
                player.set_HP(player.get_HP_MAX())
                drank_health_potion = True
                
            elif bottles[choice] == "Magic":
                txt(["The liquid has a sharp taste of blackberries, sending",
                    "a jolt down your spine as you swallow."])
                txt(["Your arms become tingly and the fibers on your shirt",
                    "stand on end. A sharp crack of thunder rings through",
                    "the air, and you feel your magic power grow."])
                txt([f"{player.get_name(True)} drinks a {Color.BLUE}Magic Potion{Color.END}.",
                    f"  > {player.get_name(True)}'s MP increases by 10!",
                    f"  > Old HP: {player.get_MP_MAX()}",
                    f"  > New HP: {player.get_MP_MAX() + 10}"])
                player.set_MP_MAX(player.get_MP_MAX() + 10)
                player.set_MP(player.get_MP_MAX())
                drank_magic_potion = True
            
            elif bottles[choice] == "Death":
                from combat import user_died
                
                txt(["The liquid has a light cucmber taste to it, bringing a sense",
                    "of calm as you swallow."])
                txt(["Without warning, every muscle in your body tenses. You begin",
                    "to feel the most excruciating pain around your neck, and",
                    "collapse to the ground.",
                    "",
                    "Aroud your neck, a ring of arcane fire squeezes tighter and",
                    "tigher, until the world begins to go dark."])
                txt([f"{player.get_name(True)} drinks {Color.RED}Merchant's Poison{Color.END}.",
                    f"  > {player.get_name(True)}'s HP drops to 0.",
                    f"  > Old HP: {player.get_HP()}",
                    f"  > New HP: 0"])
                
                # Revert back health and magic if potions were drank
                if drank_health_potion:
                    player.set_HP_MAX(player.get_HP_MAX() - 10)
                    
                if drank_magic_potion:
                    player.set_MP_MAX(player.get_MP_MAX() - 10)
                
                player.die()
                if user_died(): return story_0_feldershire
            else:
                raise NotImplementedError
            
            del bottles[choice]
            del choices[choice]
            
            choice = prompt("Do you drink a potion?", choices)
        
    else:
        raise NotImplementedError
    
    return story_0_flynn
    
# TODO: story_0_flynn
def story_0_flynn(player: Character) -> callable:
    pass

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
        time.sleep(0.25)
        print(text)
    elif isinstance(text, list):
        for line in text:
            time.sleep(0.25)
            print(line)
    next()
    print()
    
def character_txt(speaker: Character, text: Union[str, list[str]]) -> None:
    if isinstance(text, str):
        time.sleep(0.25)
        print(f"{Color.BOLD}{Color.UNDERLINE}{speaker.get_name(True)}: " + text)
    elif isinstance(text, list):
        for i in range(len(text)):
            time.sleep(0.25)
            if i == 0:
                print(f"{Color.BOLD}{Color.UNDERLINE}{speaker.get_name(True)}: " + text[i])
            else:
                print((" " * len(speaker.get_name(False))) + "  " + text[i])
    next()
    
def prompt(prompt: str, choices: list[str]) -> int:
    while True:
        time.sleep(0.25)
        print(prompt)
        
        for i in range(len(choices)):
            time.sleep(0.25)
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
                time.sleep(0.25)
                print("  > Not a valid choice. Please try again.")
                print()
                continue
        else:
            for i in range(len(choices)):
                if user_choice.upper() == choices[i].upper():
                    print()
                    return i
            time.sleep(0.25)
            print("  > Not a valid choice. Please try again.")
            print()
            continue
        
def character_prompt(speaker: Character, prompt: str, choices: list[str]) -> int:
    while True:
        time.sleep(0.25)
        print(f"{Color.BOLD}{Color.UNDERLINE}{speaker.get_name(True)}: {prompt}")
        
        for i in range(len(choices)):
            time.sleep(0.25)
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
                time.sleep(0.25)
                print("  > Not a valid choice. Please try again.")
                print()
                continue
        else:
            for i in range(len(choices)):
                if user_choice.upper() == choices[i].upper():
                    print()
                    return i
            time.sleep(0.25)
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
    print()

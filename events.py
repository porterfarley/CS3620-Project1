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
    
    combat(allies, enemies, "Shadows suddenly begin to stir all around you. Eyes appear, and slender\nfaceless humanoid figures run from the shadows, directly at you.", 1)
    
    txt("The last shadow dissapates as you finish it off. Then, the air begins to vibrate once more.")
    
    character_txt(shadow, "Do not delight in thyself, warrior. You are far from the honor you yet seek.")
    
    enemies = [shadow]
    player.set_user_controlled(False)
    allies = [player]
    combat(allies, enemies, "Around the eyes materializes a dark figure with spikes rising from its head.\nOne great step rocks the great glass pane, and it swings at you with a giant, outstretched fist.", -1)
    
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
    
    guard1 = enemy("Tristan")
    kheah = enemy("kheah")
    
    character_txt(guard1, ["Oy! You awake in there?"])
    
    choices = ["Hello? Who's there?", "Let me out of here or I'll kill you.", "*Say Nothing*"]
    choice = prompt("What do you say?", choices)
    
    character_txt(player, choices[choice])
    if choice == 0:
        character_txt(guard1, ["Uh, nobody!", "I mean, everybody!", "I mean, a great warrior, that's for sure!", 
                               "I'd be scared if I was you!", "But I'll let you off easy this time, since you're",
                               f"awake, I'll go get {kheah.get_name(True)}"])
    elif choice == 1:
        character_txt(guard1, ["*jumps*", "*shakily* You couldn't if you tried, I'm a tough warrior mate.",
                               f"But, I'm...retired! Right, I'm retired. So uh...",
                               f"I'll go get {kheah.get_name(True)}, she'll sort you out!"])
    elif choice == 2:
        character_txt(guard1, ["Well.... uh.....",
                               "Are you sure you're not there?",
                               "Oh man, they'll get mad at me if it's a false alarm...",
                               "But I'm NOT going in there...",
                               "Fine, maybe I'll go get her to be sure."])
        character_txt(guard1, ["*knocks on door*",
                               "Hello in there!",
                               "You should probably wake up, I'm going to go get",
                               f"{kheah.get_name(True)}, she's going to interrogate you now!"])
    else:
        raise NotImplementedError
    
    txt(["Little footsteps run hurriedly down the cobblestone hallway.",
        "The boy can't be over 10 years old, and the fear of you was",
        "clear in his voice."])
    
    txt(["You look down at your hands, and thick iron chains keep you",
         "in place, and from moving your arms much higher than your waist.",
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
        txt(["The moment the chains come unbolted for the ground,",
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
    
    txt(["After one more flight of stairs, you exit through a set of doors",
         "into a huge balcony area. Covered in grass and encircled by large",
         "stone thrones, carved into the natural outcroppings.",
         "On the far side sits a woman, no more than 25, adorned in a royal",
         "blue robe. Her eyes are covered by a white blindfold, yet she still",
         "looks up at you upon your arrival."])
    
    eyma = Mage("Eyma")
    eyma.set_color(Color.RED)
    character_txt(eyma, ["Ah, you are here. Thank you for coming."])
    
    txt(["You notice something changing about the girl. She begins to glow",
         "softly, a warm golden light that feels inviting. You have not felt",
         "magic like this before. Her eyes, underneath the blindfold, begin",
         "to radiate the same goldent hue, as she stares at you. It feels",
         "almost sacred to be in her presence."])
    
    print_art("EYMA")
    
    eyma.set_color(Color.BLUE)
    kheah.set_color(Color.ORANGE)
    
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
                                 f"{guard1.get_name(True)} here is one of the few survivors."])
            character_txt(eyma, ["So, to answer your question, I'm afraid it is not us who is at war with",
                                 "the imperials, but the imperials who are at war with us. We simply wish",
                                 "to preserve our people."])
        elif choice == 2:
            character_txt(eyma, ["Yes, I believe I can. Your life was made forfeit by imperial magic, and",
                                 "I believe you have a right to it again. I believe that my powers are the",
                                 "only ones that may offer you that chance."])
        elif choice == 3:
            character_txt(eyma, ["Hmm... it is justified to ask this. I'm afraid you were brought here in",
                                 "... less than ideal circumstances for sure. You have to understand our",
                                 "caution. Your kind have killed many of our people.",
                                 "...",
                                 "Ah, I believe I have a question for you in return then: who else would",
                                 "you trust?"
                                 ""
                                 "Surely being \"called up\", handed a weapon, and pointed in a general",
                                 "direction was not the most trustworthy of eginnings either."])
            character_txt(eyma, ["I'd ask you to hear us out, and make the choice that seems most",
                                 "logical to you. But I'm also afraid that you know more than we can",
                                 "afford to let slip at this time in our fight against the imperials.",
                                 "I will not threaten your life, but I will return you to the cell",
                                 "you were in before until such a time you agree to comply."])
            txt(["The woman's voice holds no malice and doesn't seem to be",
                 "threatening. Instead, her words seem very matter of fact."])
        elif choice == 4:
            break;
        else:
            raise NotImplementedError
        
        choice = prompt("What do you say?", choices)
        
    character_txt(player, ["So what does this have to do with me?"])
    
    character_txt(eyma, ["An excellent question indeed, where do you fit into all of this?"])
    
    choices = ["Yes, I did.", "*Say Nothing*"]
    character_prompt(eyma, f"{player.get_name(True)} before you were called up, did you dream of anything?")
    
    character_txt(["The Spark shows more than the temporal things; I have seen your",
                   "vision too. Even more, I have seen visions of your past."])
    
    txt([f"{eyma.get_name(True)} begins to glow even more and you can now see the irises of her",
         "eyes through the blindfold now. Her voice becomes more authoratative and",
         "a somber feeling fills the air."])
    
    character_txt(eyma, ["Over 1000 years ago, the lands were united together by faith and magic.",
                         "Though separated over great distances, each people shared a portion of",
                         "their gifts with a wise and powerful ruler. The ruler used the shared",
                         "powers to protect every land in the kindgom. They never imposed taxes",
                         "or shared burdens, but helped to create prosperity and shared strength."])
    
    character_txt(eyma, ["Wielding all kinds of magic and weaponry skills, the ruler ensured the",
                         "safety of all of their people. When their time came, they would pass on",
                         "the powers to their successor.",
                         "",
                         "This warrior was revered and beloved by all the people, and soon earned",
                         f"the title of {Color.CYAN}Honored One{Color.END}."])
    
    tvashtri = enemy("Tvashtri")
    
    character_txt(eyma, [f"About 800 years ago, without warning, the {Color.CYAN}Honored one{Color.END} disappeared.",
                         f"No one knows where the last {Color.CYAN}Honored One{Color.END} went. And unfortunately,",
                         "the Spark can't see that either.",
                         "",
                         f"What I can see, is that 100 years after this, a dark necromancer named {tvashtri.get_name(True)}",
                         "began a march with legions of undead soldiers, wiping out the lands originally under",
                         "the Honored One's protection. Surely, this could not have been a mere coincidence."])
    
    character_txt(eyma, [f"And this is where you come in {player.get_name(True)}. You are one of these undead",
                         f"soldiers. I believe that the {tvashtri.get_name(True)}'s soldiers are stolen souls from the",
                         "time of the last Honored One, recycled upon their deaths over and over again.",
                         ""
                         "I apologize if this sounds callous. I can only imagine how I would feel",
                         "if I just found this out for the first time as well. But I believe that",
                         "you, and your fellow compatriots, have been under his command and",
                         "made the ultimate sacrifice an innumerable amount of times in the last",
                         "700 years."])
    
    character_txt(eyma, [f"{player.get_name(True)}, we are losing this war. Before long, my entire",
                         f"people will be wiped out and join {tvashtri.get_name(True)}'s army in a grand march",
                         "to the ends of the world. But I don't believe that we are without hope yet.",
                         "",
                         "You. The Spark has guided me to you, and I believe that you, once",
                         "your memories are unlocked, will be able to help us uncover the",
                         f"secret of the {Color.CYAN}Honored One{Color.END}'s disappearance, and help",
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


# TODO: story_0_guardian
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
         "is a crown made of marble. It radiates a crisp Azure light",
         "that reflects nobility and honor."])
    
    txt(["Suddenly, a deep voice cuts through the darkness."])
    
    guardian = bbg("???")
    character_txt(guardian, "O warrior, how hast thou entered this place again?")
    
    choices = ["My body back.", "I want my memories back!", "To find out the truth about the Honored One."]
    choice = character_prompt(guardian, "What seekest thou?", choices)
    
    character_txt(player, choices[choice])
    
    character_txt(guardian, ["What thou seekest hath been made forfeit by thine death.",
                             "Thine rights to it are no longer thine, but mine."])
    
    choices = ["*Brandish the medallion*"]
    choice = prompt("What do you do?", choices)
    
    character_txt(player, choices[choice])
    
    character_txt(guardian, ["I see. Then prepare to prove thyself. Take up thy",
                             "weapon, and fall not to the shadows."])
    
    allies = [player]
    enemies = [enemy("Shadow 1")]
    combat(allies, enemies, "A single shadow emerges from the floor of the stained\nglass floor and lunges at you.", 0)
    
    shadow_mage = Mage("Shadow Mage")
    shadow_mage.set_color(Color.RED)
    shadow_mage.set_MP_MAX(20)
    enemies = [enemy("Shadow 1"), enemy("Shadow 2"), shadow_mage]
    combat[allies, enemies, "As the shadow disolves, three more take its place. One\nholds aloft a great staff of darkness."]
    
    txt(["With the other foes now vanquished, you feel the medallion",
         "pulse with light, and you feel completely restored to your",
         "full prior strength."])
    
    player.rest()
    
    character_txt(guardian, ["You have done well. Now, thy final test. Thou shalt",
                             "face me. And if you win, then shall I grant thee what",
                             "I have been tasked with protecting."])
    
    txt(["A colossal shadowy figure emerges from the darkness. Two",
        "bright yellow, pupil-less eyes shine through. Its head",
        "is adorned with spikes, and it rocks the great glass pane",
        "when it steps down."])
    
    txt(["At the moment it steps down, the medallion pulses once again.",
         "A ray of golden light shines from it onto the creature,",
         "who shrieks in pain. When the ray stops, the monster",
         "has lost nearly half its height, and is now riddles with holes."])
    
    
    

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
                 "and a little point to her ears are the only distinguishing"
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
        return story_1_feldershire
    else:
        raise NotImplementedError

# TODO: story_1_a()
def story_1_north_west_road(player: Character) -> callable:
    
    txt(["As you turn down the road, the sounds of become more and",
         "more anguished. You begin to sprint down the path."])
    
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
    combat([soldier1, player], enemies,
           "Some of the wolves begin to eye you warily and then a set of razor sharp fangs comes right for you.", 0)
    
    if soldier1.get_HP() <= 0:
        txt(["The poor soldier heaves a couple of pained last breaths and is gone.",
             "The armor he was wearing seems to fall apart, and his body disperses",
             "like a cloud. From his chest rises a single golden flicker. It floats",
             "gently down to the ground and in a flash of golden light, a tree sapling",
             "springs up from the ground."])
    else:
        soldier1.set_name("Phil")
        character_txt(soldier1, ["Wasn't that a right bit of melarky right there!? Dang goblins and",
                                 "they're dang wolves! I woulda had me arm bitten clean off without",
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
        
        return story_1_feldershire
         
    else:
        raise NotImplementedError
    

# TODO: story_1_b()
def story_1_feldershire():
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
        time.sleep(0.5)
        print(text)
    elif isinstance(text, list):
        for line in text:
            time.sleep(0.5)
            print(line)
    next()
    print()
    
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
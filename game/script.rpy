# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define character.g = Character("Griff Ironstride", image="griff")
default g.health = 100

define character.k = Character("Kaelen Swiftblade", image="kaelen")
default k.health = 100

define m = Character("[player_name]", image="player")
default m.health = 100
define m.inventory = {}
# TODO: player stats

# NPCS
define character.goaneli = Character("???", image="goaneli")
define goaneli.relevance = "Not Encountered"
define goaneli.know_name = False

define character.maci = Character("???", image="maci")
define maci.known = "Not Encountered"
define maci.know_name = False

define n = nvl_narrator


# The game starts here.

label start:

# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

    $ player_name = renpy.input("What is your name?", length=32)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="John"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg on_ship

    # These display lines of dialogue.

label ep1:

    "You and your friends (Kaelen Swiftblade and Griff Ironstride),
    each receive a cryptic invitation or message, beckoning them to the city in their time of need."

    scene bg letter

    n """Dear [player_name],

    You and your companions, Kaelen Swiftblade and Griff Ironstride, are hereby cordially invited to answer a
    most peculiar summons from a realm shrouded in mystery and need.

    This cryptic message, like an elusive whisper in the wind, calls upon you to embark on an extraordinary journey.

    From the depths of an unknown sender's identity, this missive arrived, intriguing in its enigma.

    There are dire circumstances plaguing this distant city, a realm beset
    by strange and unsettling natural disasters that defy explanation.

    The land cries out for aid, and its people yearn for heroes who possess the courage and valor to confront the inexplicable.

    Prepare yourselves for an epic journey that will test your mettle and unravel the secrets shrouding the city."""

    "Intrigued by the enigmatic nature of the message, you, Kaelen Swiftblade, and Griff Ironstride, heed the call to adventure."
    "Your determination to unravel the mysteries surrounding these bizarre phenomena and your compassion for the suffering people of this distant city make you the perfect candidates to face this enigmatic challenge."

    "If you succeed, you will be hailed as heroes and saviors of the city"

    scene bg on_ship
    
    "You sail towards the city, the sea grows rough and the ship rocks violently."
    "You see the city in the distance, a dark cloud looming over it."
    "Suddenly, the ship is hit by a powerful gust of wind and it crashes into some rocks, sending debris flying everywhere."

    g "What was that???"

    jump .ship_crash


label .ship_crash:

    hide griff
    $ dice = renpy.random.randint(0, 20) # TODO: Dexterity stat
    if dice >= 19:
        "You manage to stay on your feet."
        jump .post_crash
    elif dice >= 13:
        "You get thrown onto the floor, but manage to get up back on your feet after."
        jump .post_crash
    elif dice >= 8:
        scene bg on_ship_side
        "You fall off the ship, but manage to grab onto the side."
        menu:
            "Pull yourself up.": 
                #TODO: Strength stat
                $ dice = renpy.random.randint(0, 20)
                if dice >= 10:
                    "You manage to gather all your strenth and pull yourself up onto the ship."
                    jump .post_crash    
                elif dice >= 5:
                    "You try to pull yourself up but don't have enough strength."
                    "Luckily, Griff notices you and pulls you up back onto the ship."
                    g "Next time try to stay on the ship."
                    m angry "What was I meant to do???"
                    jump .post_crash
                else:
                    "In an attempt to pull yourself up, your grip fails and you plunge into the cold ocean below." 
                    jump .in_ocean
            "Let go.":
                "You let go of the side of the ship, plunging into the cold ocean below."
                m """{i}Why did I do that?{/i}"""

            "Do nothing.":
                m """{i}What do I do now?{/i}"""
                pause 1.5
                "Griff notices you hanging off the side of the ship."
                g "Hang on, I'll pull you up."
                m "What else would I do?"
                jump .post_crash
    elif dice >= 5:
        "Your fingers just miss the side of the ship and fall into the cold ocean below."
        jump .in_ocean
    else:
        "You get thrown off the side of the ship, plunging into the cold ocean below."
        jump .in_ocean

    label .in_ocean:
        scene bg in_ocean
        "What do you do now?"
        menu .in_ocean_choices:
            "Swim to shore":
                "It's too far away."
                jump .in_ocean_choices
            "Swim to a plank of wood":
                "You swim to a plank of wood and grab onto it."
                "Griff Ironstride notices you."
                g shout "Swim to the boat, I'll pull you up!"
                m "Ok!"
                jump .post_crash
            "Climb onto the ship":
                "You try to climb the ship but can't get a good grip anywhere."
                jump .in_ocean_choices

label .post_crash:
    g "Who's steering this thing?"
    k "My bad..."
    g "How is this thing still floating anyway?"
    k "No idea!"

    jump ep2

label ep2:
    "You have arrived"
    m "{i}This place has been wrecked by the natural disasters.{/i}"
    goaneli "Hello!"
    $ goaneli.relevance = "Encountered"
    menu .goaneli_interaction:
        "Hi!":
            m "Hi!"
            goaneli "..."
            jump .goaneli_interaction
        "Who are you?":
            m "Who are you?"
            goaneli "I'm one of the locals here."
            menu .goaneli_interaction_a:
                "What's your name?":
                    if goaneli.relevance = "Encountered":
                        goaneli "Oh right,{nw}"

                        $ character.goaneli = Character("Goaneli", image="goaneli")
                        $ goaneli.know_name = True

                        goaneli "Oh right,{fast} I'm Goaneli."
                    elif goaneli.know_name = True:
                        goaneli "I already told you, I'm Goaneli."
                    jump .goaneli_interaction_a

                "{i}Back{/i}":
                    jump .goaneli_interaction
        "What happened?":
            m "What happened here?"
            goaneli "Do you really not know?"

            menu .goaneli_interaction_b:
                "No.":
                    m "No, I really don't."
                    goaneli "Some really powerful natural disasters struck."
                    goaneli " This whole city got wrecked, and others too."
                    goaneli "And it's going to happend again."
                    jump .goaneli_interaction
                "Yes.":
                    m "Oh wait, I remember now."
                    jump .goaneli_interaction
                "{i}Back{/i}":
                    jump .goaneli_interaction

        "How to stop?":
            m "How do we stop this mess?"
            goaneli "No idea."
            goaneli "You should probbably talk to the mayor about that."
            $ how_to_stop_interaction = True
            jump .goaneli_interaction

        "Where is mayor?" if 'how_to_stop_interaction' in locals():
            m "Where could I find the mayor?"
            goaneli "The mayor the tallest in the city."
            m "Ok, thanks."
            $ where_is_mayor = True
            jump .goaneli_interaction
        
        "Bye!":
            m "Bye!"
            goaneli "Wait."
            goaneli "After you finish that, can you help me find the Whispering Stone?"
            menu:
                "Sure.":
                    m "Sure."
                    goaneli "Thanks!"
                    goaneli "I'll be waiting here."
                "What's that?":
                    m "What's that?"
                    goaneli "I'll tell you later."

    if how_to_stop_interaction:
        m "{i}We should probabbly go talk to the mayor then...{/i}"
    menu:
        "Talk to the person again." if not goaneli.know_name:
            jump .goaneli_interaction
        
        "Talk to Goaneli" if goaneli.know_name:
            jump .goaneli_interaction

        "Find the mayor" if where_is_mayor:
            m "{i}He did say the mayor was in the tallest building in the city.{/i}"
            m "{i}Shouldn't be {b}too{/b} hard to find."
            m "We should go find the mayor."
            k "Where is the mayor?"
            m "In a tall building."
            k "Which one?"
            m "The tallest one here."
            m "You should be able to see it."
            k "I see it."
            m "Let's go."
            g "We just arrived!"
            g "Can't it wait until tomorrow?"
            menu:
                "Wait until tomorrow.":
                    m "I guess we {b}could{/b} wait until tomorrow..."
                    k "Where would we even go to rest?"
                    m "I guess we could find somwhere..."
                    g "Follow me, I know an inn where we can stay."
                    m "Sure."
                    jump .inn_first_time
                "Go now.":
                    m "We have to go now."
                    g "Fine."
                    jump .mayor_building

label .inn_first_time:
    scene bg inn
    "You arrive at the inn."
    """The inn is a two-storey building of stone walls, with several stained glass windows and a tiled mosaic floor.
    Accomodations consist of several small rooms with beds and woolen mattresses."""
    "You are greeted by an elf."
    $ maci.relevance = "Encountered"
    jump inn

label inn:
    maci "Hello, welcome to the inn."
    menu .maci_interaction:
        "Hello.":
            m "Hello."
            maci "What can I help you with?"
            jump .maci_interaction
        "Who are you?":
            m "Who are you?"
            maci "I'm Maci{nw}"
            $ character.maci = Character("Maci", image="maci")
            $ maci.know_name = True
            maci "I'm Maci{fast}, the owner of this inn."
            jump .maci_interaction
        "How much is a room?":
            m "How much is a room?"
            maci "It's 5 gold coins per night."
            jump .maci_interaction
        "Rent a room.":
            m "I'd like to rent a room."
            maci "Sure, that'll be 5 gold coins."
            if m.inventory['gold'] >= 5:
                m "Here you go."
                $ m.inventory['gold'] -= 5
                maci "Here's your key."
                $ m.inventory['inn key'] = 1
                m "Thanks."
                jump inn_room
            else:
                m "I don't have enough."
                maci "Come back when you do."
                $ need_gold = True
            maci "Here's your key."
            m "Thanks."
            jump .inn_first_time
        "Bye!":
            m "Bye!"
            maci "Bye!"
    if need_gold in locals():
        m "{i}We need to find some gold.{/i}"
        m "{cps=*2}We need to find some gold{/cps}"
    pass

label inn_room:
    scene bg inn_room
    "{b}This bit hasn't been finished yet.{/b}"
    # TODO: finish inn room

label .mayor_building:
    scene bg mayor_building
    "{b}This bit hasn't been finished yet.{/b}"
    # TODO: finish mayor building
    pass
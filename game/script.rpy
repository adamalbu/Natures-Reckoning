# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define character.g = Character("Griff Ironstride", image="griff")
default g.health = 100

define character.k = Character("Kaelen Swiftblade", image="kaelen")
default k.health = 100

define m = Character("[player_name]", image="player")
default m.health = 100

define all_npcs = {0: {"name": "Nathan", "known": False, "character": Character("???")}}

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
    each receive a cryptic invitation or message, beckoning them to the kingdom in their time of need."

    scene bg letter

    n """Dear [player_name],

    You and your companions, Kaelen Swiftblade and Griff Ironstride, are hereby cordially invited to answer a
    most peculiar summons from a realm shrouded in mystery and need.

    This cryptic message, like an elusive whisper in the wind, calls upon you to embark on an extraordinary journey.

    From the depths of an unknown sender's identity, this missive arrived, intriguing in its enigma.

    There are dire circumstances plaguing this distant kingdom, a realm beset
    by strange and unsettling natural disasters that defy explanation.

    The land cries out for aid, and its people yearn for heroes who possess the courage and valor to confront the inexplicable.

    Prepare yourselves for an epic journey that will test your mettle and unravel the secrets shrouding the kingdom."""

    "Intrigued by the enigmatic nature of the message, you, Kaelen Swiftblade, and Griff Ironstride, heed the call to adventure."
    "Your determination to unravel the mysteries surrounding these bizarre phenomena and your compassion for the suffering people of this distant kingdom make you the perfect candidates to face this enigmatic challenge."

    scene bg on_ship
    
    "You sail towards the kingdom, the sea grows rough and the ship rocks violently."
    extend " You see the kingdom in the distance, a dark cloud looming over it."
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
                    extend " Luckily, Griff notices you and pulls you up back onto the ship."
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
                extend " Griff Ironstride notices you."
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
    "???" "Hello!"

    define npc_0 = "???"
    $ npc_0 = all_npcs[0]['character']
    menu .npc_0_interaction:
        "Hi!":
            m "Hi!"
            npc_0 "..."
            jump .npc_0_interaction
        "Who are you?":
            m "Who are you?"
            npc_0 "I'm one of the locals here."
            menu .npc_0_interaction_a:
                "What's your name?":
                    if all_npcs[0]['known'] == False:
                        npc_0 "Oh right."

                        $ npc_0_name = all_npcs[0]['name']
                        $ all_npcs[0]['known'] = True
                        $ all_npcs[0]['character'] = Character(all_npcs[0]['name'])
                        $ npc_0 = all_npcs[0]['character']

                        extend " I'm [npc_0_name]."
                    else:
                        npc_0 "I already told you."
                        $ npc_0_name = all_npcs[0]['name']
                        extend " I'm [npc_0_name]."
                    jump .npc_0_interaction_a

                "{i}Back{/i}":
                    jump .npc_0_interaction
        "What happened?":
            m "What happened here?"
            npc_0 "Do you really not know?"

            menu .npc_0_interaction_b:
                "No.":
                    m "No, I really don't."
                    npc_0 "Some really powerful natural disasters struck, almost all at once."
                    extend " This whole kingdom got wrecked."
                    npc_0 "And it's going to happend in the future."
                    extend " Prettey soon too, I think"
                    jump .npc_0_interaction
                "Yes.":
                    m "Oh wait, I remember now."
                    jump .npc_0_interaction
                "{i}Back{/i}":
                    jump .npc_0_interaction

        "How to stop?":
            m "How do we stop this mess?"
            npc_0 "No idea."
            extend " You should probbably talk to the mayor about that."
            $ how_to_stop_interaction = True
            jump .npc_0_interaction

        "Where is mayor?" if 'how_to_stop_interaction' in locals():
            m "Where could I find the mayor?"
            npc_0 "In that building over there."
            npc_0 "That really tall one."
            extend " It's the tallest in the kingdom."
            m "Ok, thanks."
            $ where_is_mayor = True
            jump .npc_0_interaction
        
        "Bye!":
            m "Bye!"
            npc_0 "Bye!"

    if how_to_stop_interaction:
        m "{i}We should probabbly go talk to the mayor then...{/i}"
    "What do you want to do?"
    menu:
        "Talk to the person again." if not all_npcs[0]['known']:
            jump .npc_0_interaction
        
        "Talk to [npc_0_name]" if all_npcs[0]['known']:
            jump .npc_0_interaction

        "Find the mayor" if where_is_mayor:
            m "{i}He did say the mayor was in the tallest building in the city.{/i}"
            m "{i}Shouldn't be {b}too{/b} hard to find."
            m "We should go find the mayor."
            k "Where is the mayor?"
            m "In a tall building."
            k "Which one?"
            m "The tallest one here."
            extend " You should be able to see it."
            k "I see it."
            m "Let's go."
            g "We just arrived!"
            g "Can't it wait until tomorrow?"
            menu:
                "Wait until tomorrow.":
                    m "I guess we {i}could{/i} wait until tomorrow."
                    # TODO: finish
                "Go now.":
                    m "We have to go now."
                    # TODO: finish
            # TODO: finish
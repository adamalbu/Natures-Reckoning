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
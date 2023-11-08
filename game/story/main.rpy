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
            jump inn_room
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
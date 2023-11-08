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
                    if goaneli.relevance == "Encountered":
                        goaneli "Oh right,{nw}"

                        $ character.goaneli = Character("Goaneli", image="goaneli")
                        $ goaneli.know_name = True

                        goaneli "Oh right,{fast} I'm Goaneli."
                    elif goaneli.know_name == True:
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
                    jump .mayor_building # FIXME: .mayor_building is not in ep2, make ep3 then add it there

label .inn_first_time:
    scene bg inn
    "You arrive at the inn."
    """The inn is a two-storey building of stone walls, with several stained glass windows and a tiled mosaic floor.
    Accomodations consist of several small rooms with beds and woolen mattresses."""
    "You are greeted by an elf."
    $ maci.relevance = "Encountered"
    jump inn
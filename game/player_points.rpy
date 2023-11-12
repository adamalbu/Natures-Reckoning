screen player_points():
        tag menu

        add gui.main_menu_background

        $ strength = m.stats["strength"]
        $ dexterity = m.stats["dexterity"]
        $ constitution = m.stats["constitution"]
        $ intelligence = m.stats["intelligence"]
        $ wisdom = m.stats["wisdom"]
        $ charisma = m.stats["charisma"]

        frame:
                xalign 0.5
                yalign 0.5
                xpadding 30
                ypadding 30

                hbox:
                        spacing 40
                        
                        vbox:
                                spacing 10
                                text "Strength" size 40
                                text "Dexterity" size 40
                                text "Constitution" size 40
                                text "Intelligence" size 40
                                text "Wisdom" size 40
                                text "Charisma" size 40
                        
                        vbox:
                                spacing 10
                                text "[strength]" size 40
                                text "[dexterity]" size 40
                                text "[constitution]" size 40
                                text "[intelligence]" size 40
                                text "[wisdom]" size 40
                                text "[charisma]" size 40
                
                        textbutton "Back" action Jump("after_start")
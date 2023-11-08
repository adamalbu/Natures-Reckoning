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
default goaneli.relevance = "Not Encountered"
default goaneli.know_name = False

define character.maci = Character("???", image="maci")
default maci.known = "Not Encountered"
default maci.know_name = False

define n = nvl_narrator
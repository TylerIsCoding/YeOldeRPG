##### Imports #####
from Game import *
from Utility import TextSpeed
###################

game = Game()
Utility.menu = TextSpeed.instant
Utility.story = TextSpeed.instant
game.player_name()
game.steven_fight()
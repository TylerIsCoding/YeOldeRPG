##### Imports #####
from Game import *
from Utility import TextSpeed
###################

game = Main()
Utility.menu = TextSpeed.instant
Utility.story = TextSpeed.instant
game.player_name()
game.kingsmen()
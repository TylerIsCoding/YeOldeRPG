##### Imports #####
from Game import *
from Utility import TextSpeed
###################

game = Game()
Utility.menu = TextSpeed.instant
Utility.combat = TextSpeed.fast
Utility.story = TextSpeed.instant
game.player_name()
game.nick_fight()
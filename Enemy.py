##### Imports #####
from Dice import *
from Utility import *
###################


### Enemy Setup ###

class Enemy:
    
    additional_damage = 0
    additional_defense = 0


class Nick(Enemy):

    max_attack_str = "1d6"
    defense = "1d4"
    
    def __init__(self):
        self.name = "Nick the Scav"
        self.type = "Enemy"
        self.hp = 6
        self.max_hp = 6
        self.mp = 4
        self.blk = Dice.d_4
        self.atk = Dice.d_6
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_4
        self.skills = [Bush, Legshot]
        


class Steven(Enemy):

    max_attack_str = "1d8"
    defense = "1d6"

    def __init__(self):
        self.name = "Sweaty Steven"
        self.type = "Enemy"
        self.hp = 8
        self.max_hp = 8
        self.mp = 4
        self.blk = Dice.d_6
        self.atk = Dice.d_8
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_4
        self.skills = [ExitCamp, Aim]
        

class Shturman(Enemy):

    max_attack_str = "1d10"
    defense = "1d6"

    def __init__(self):
        self.name = "Shturman"
        self.type = "Enemy"
        self.hp = 10
        self.max_hp = 10
        self.mp = 4
        self.blk = Dice.d_6
        self.atk = Dice.d_10
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_4
        self.skills = [Goons, Grenade]
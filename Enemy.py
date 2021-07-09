##### Imports #####
from Dice import *
from Utility import *
###################


### Enemy Setup ###

class Enemy:
    
    additional_damage = 0


class Nick(Enemy):

    max_attack_str = "1d8"
    defense = "1d4"
    
    def __init__(self):
        self.name = "Nick the Scav"
        self.type = "Enemy"
        self.hp = Dice.d_8()
        self.max_hp = ''
        self.mp = Dice.d_8()
        self.blk = Dice.d_4
        self.atk = Dice.d_8
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_4
        self.skills = [Bush, Legshot]
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 15 or total_skill_points <= 8 and self.hp <= 5:
            self.hp = Dice.d_8()
            self.mp = Dice.d_6()
            total_skill_points = (self.hp + self.mp)

class Steven(Enemy):

    max_attack_str = "1d10"
    defense = "1d6"

    def __init__(self):
        self.name = "Sweaty Steven"
        self.type = "Enemy"
        self.hp = Dice.d_8()
        self.max_hp = ''
        self.mp = Dice.d_10()
        self.blk = Dice.d_6
        self.atk = Dice.d_10
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_4
        self.skills = [ExitCamp, Aim]
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 15 or total_skill_points <= 8 and self.hp <= 7:
            self.hp = Dice.d_8()
            self.mp = Dice.d_4()
            total_skill_points = (self.hp + self.mp)

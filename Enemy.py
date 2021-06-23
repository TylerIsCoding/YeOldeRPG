from Dice import *
from Game import *
from Player import *
from Skills import *


### Enemy Setup ###

class Enemy:
    
    additional_damage = 0


class Nick(Enemy):
    
    def __init__(self):
        self.name = "Nick the Scav"
        self.type = "Enemy"
        self.hp = Dice.d_8()
        self.mp = Dice.d_8()
        self.blk = Dice.d_4
        self.atk = Dice.d_8
        self.def_buff = BuffSkill.default
        self.atk_buff = BuffSkill.default
        self.mprecover = Dice.d_4
        self.skills = [
            BuffSkill.bush,
            AttackSkill.legshot
        ]
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 15 or total_skill_points <= 8:
            self.hp = Dice.d_8()
            self.mp = Dice.d_6()
            total_skill_points = (self.hp + self.mp)

class Steven(Enemy):
        
    def __init__(self):
        self.name = "Sweaty Steven"
        self.type = "Enemy"
        self.hp = Dice.d_8()
        self.mp = Dice.d_10()
        self.blk = Dice.d_6
        self.atk = Dice.d_10
        self.def_buff = BuffSkill.default
        self.atk_buff = BuffSkill.default
        self.mprecover = Dice.d_4
        self.skills = [
            BuffSkill.exit_camp,
            AttackSkill.aim
        ]
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 15 or total_skill_points <= 8:
            self.hp = Dice.d_8()
            self.mp = Dice.d_4()
            total_skill_points = (self.hp + self.mp)

from Dice import *
from Game import *
from Player import *


### Enemy Setup ###

class Enemy:
    
    additional_damage = 0


class Nick(Enemy):
    
    def __init__(self):
        self.name = "Nick the Scav"
        self.hp = Dice.d_8()
        self.mp = Dice.d_6()
        self.blk = Dice.d_4
        self.atk = Dice.d_8
        self.mprecover = Dice.d_4
        self.skill1 = AttackSkill.legshot
        self.skill2 = AttackSkill.fireball
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 15 or total_skill_points <= 8:
            self.hp = Dice.d_8()
            self.mp = Dice.d_6()
            total_skill_points = (self.hp + self.mp)

class Steven(Enemy):
        
    def __init__(self):
        self.name = "Sweaty Steven"
        self.hp = Dice.d_8()
        self.mp = Dice.d_4()
        self.blk = Dice.d_6
        self.atk = Dice.d_10
        self.mprecover = Dice.d_4
        self.skill1 = AttackSkill.legshot
        self.skill2 = AttackSkill.legshot
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 15 or total_skill_points <= 8:
            self.hp = Dice.d_8()
            self.mp = Dice.d_4()
            total_skill_points = (self.hp + self.mp)

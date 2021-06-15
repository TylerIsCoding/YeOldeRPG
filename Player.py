from Dice import *
from Enemy import *
from Utility import *

### Player Setup ###

class Player:

    additional_damage = 0
    
    def __init__(self, name):
        self.name = name

class Mage(Player):

    max_attack_str = "1d6"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Mage"
        self.hp = Dice.d_6()
        self.mp = Dice.d_10()
        self.blk = Dice.d_4()
        self.atk = Dice.d_6()
        self.mprecover = Dice.d_4()
        self.additional_damage = 0
        self.skill1 = RecoverySkill.heal_minor
        self.skill2 = AttackSkill.fireball
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_6()
            self.mp = Dice.d_10()
            self.blk = Dice.d_4()
            total_skill_points = (self.hp + self.mp + self.blk)
    

class Warrior(Player):

    max_attack_str = "1d12"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Warrior"
        self.hp = Dice.d_20()
        self.mp = Dice.d_6()
        self.blk = Dice.d_8()
        self.atk = Dice.d_12()
        self.mprecover = Dice.d_2()
        self.additional_damage = 0
        self.skill1 = AttackSkill.overhead_slash
        self.skill2 = AttackSkill.shield_bash
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_20()
            self.mp = Dice.d_6()
            self.blk = Dice.d_8()
            total_skill_points = (self.hp + self.mp + self.blk)


class Rogue(Player):

    max_attack_str = "1d6"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Rogue"
        self.hp = Dice.d_8()
        self.mp = Dice.d_8()
        self.blk = Dice.d_10()
        self.atk = Dice.d_6()
        self.mprecover = Dice.d_2()
        self.additional_damage = 0
        self.skill1 = BuffSkill.shadows
        self.skill2 = AttackSkill.backstab
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_8()
            self.mp = Dice.d_8()
            self.blk = Dice.d_10()
            total_skill_points = (self.hp + self.mp + self.blk)

class Barb(Player):

    max_attack_str = "1d8"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Barbarian"
        self.hp = Dice.d_12()
        self.mp = Dice.d_6()
        self.blk = Dice.d_6()
        self.atk = Dice.d_8()
        self.mprecover = Dice.d_2()
        self.additional_damage = 0
        self.skill1 = AttackSkill.flurry
        self.skill2 = RecoverySkill.heal_minor
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_12()
            self.mp = Dice.d_6()
            self.blk = Dice.d_6()
            total_skill_points = (self.hp + self.mp + self.blk)

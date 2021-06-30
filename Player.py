##### Imports #####
from Dice import *
from Utility import *
###################

### Player Setup ###

class Player:

    additional_damage = 0
    
    def __init__(self, name):
        self.name = name


class Mage(Player):

    max_attack_str = "1d6"
    defense = "1d6"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Mage"
        self.type = "Player"
        self.hp = Dice.d_6()
        self.mp = Dice.d_10()
        self.blk = Dice.d_4
        self.atk = Dice.d_6
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_4
        self.additional_damage = 0
        self.skillpoints = 15
        self.skills = []
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_6()
            self.mp = Dice.d_10()
            total_skill_points = (self.hp + self.mp)
    

class Warrior(Player):

    max_attack_str = "1d10"
    defense = "1d8"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Warrior"
        self.type = "Player"
        self.hp = Dice.d_12()
        self.mp = Dice.d_6()
        self.blk = Dice.d_8
        self.atk = Dice.d_10
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_2
        self.additional_damage = 0
        self.skillpoints = 10
        self.skills = []
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_20()
            self.mp = Dice.d_6()
            total_skill_points = (self.hp + self.mp)


class Rogue(Player):

    max_attack_str = "1d6"
    defense = "1d10"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Rogue"
        self.type = "Player"
        self.hp = Dice.d_8()
        self.mp = Dice.d_8()
        self.blk = Dice.d_10
        self.atk = Dice.d_6
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_2
        self.additional_damage = 0
        self.skillpoints = 12
        self.skills = []
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_8()
            self.mp = Dice.d_8()
            total_skill_points = (self.hp + self.mp)

class Barb(Player):

    max_attack_str = "1d8"
    defense = "1d6"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Barbarian"
        self.type = "Player"
        self.hp = Dice.d_12()
        self.mp = Dice.d_6()
        self.blk = Dice.d_6
        self.atk = Dice.d_8
        self.def_buff = Default
        self.atk_buff = Default
        self.mprecover = Dice.d_2
        self.additional_damage = 0
        self.skillpoints = 10
        self.skills = []
        total_skill_points = (self.hp + self.mp)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_12()
            self.mp = Dice.d_6()
            total_skill_points = (self.hp + self.mp)

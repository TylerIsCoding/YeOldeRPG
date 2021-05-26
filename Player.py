from Dice import *

### Player Setup ###

class Player:

    additional_damage = 0
    def __init__(self, name):
        self.name = name


class Mage(Player):

    max_attack = "1d6"
    def __init__(self, name):
        super().__init__(name)
        self.role = "Mage"
        self.hp = Dice.d_6()
        self.mp = Dice.d_10()
        self.blk = Dice.d_4()
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_6()
            self.mp = Dice.d_6()
            self.blk = Dice.d_4()
            total_skill_points = (self.hp + self.mp + self.blk)
    
    def attack(self, enemy):
        atk = Dice.d_6() + self.additional_damage
        enemy.hp = (enemy.hp + enemy.blk) - atk


class Warrior(Player):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Warrior"
        self.hp = Dice.d_20()
        self.mp = Dice.d_6()
        self.blk = Dice.d_8()
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_20()
            self.mp = Dice.d_6()
            self.blk = Dice.d_8()
            total_skill_points = (self.hp + self.mp + self.blk)

    def attack(self, enemy):
        atk = Dice.d_12() + self.additional_damage
        enemy.hp = (enemy.hp + enemy.blk) - atk


class Rogue(Player):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Rogue"
        self.hp = Dice.d_8()
        self.mp = Dice.d_8()
        self.blk = Dice.d_10()
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_8()
            self.mp = Dice.d_8()
            self.blk = Dice.d_10()
            total_skill_points = (self.hp + self.mp + self.blk)

    def attack(self, enemy):
        atk = Dice.d_6() + self.additional_damage
        enemy.hp = (enemy.hp + enemy.blk) - atk


class Barb(Player):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Barbarian"
        self.hp = Dice.d_12()
        self.mp = Dice.d_6()
        self.blk = Dice.d_6()
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_12()
            self.mp = Dice.d_6()
            self.blk = Dice.d_6()
            total_skill_points = (self.hp + self.mp + self.blk)

    def attack(self, enemy):
        atk = Dice.d_8() + self.additional_damage
        enemy.hp = (enemy.hp + enemy.blk) - atk
        print("You dealt " + str((enemy.hp + enemy.blk) - atk) + " to the enemy!")


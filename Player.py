from Dice import *

### Player Setup ###

class Player:

    def __init__(self, name):
        self.name = name


class Mage(Player):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Mage"
        self.hp = Dice.d_6()
        self.mp = Dice.d_10()
        self.blk = Dice.d_4()
        self.atk = Dice.d_10()
        total_skill_points = (self.hp + self.mp + self.blk + self.atk)
        while total_skill_points >= 25 or total_skill_points <= 20:
            self.hp = Dice.d_6()
            self.mp = Dice.d_10()
            self.blk = Dice.d_4()
            self.atk = Dice.d_10()
            total_skill_points = (self.hp + self.mp + self.blk + self.atk)


class Warrior(Player):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Warrior"
        self.hp = Dice.d_20()
        self.mp = Dice.d_6()
        self.blk = Dice.d_8()
        self.atk = Dice.d_12()
        total_skill_points = (self.hp + self.mp + self.blk + self.atk)
        while total_skill_points >= 25 or total_skill_points <= 20:
            self.hp = Dice.d_20()
            self.mp = Dice.d_6()
            self.blk = Dice.d_8()
            self.atk = Dice.d_12()
            total_skill_points = (self.hp + self.mp + self.blk + self.atk)


class Rogue(Player):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Rogue"
        self.hp = Dice.d_8()
        self.mp = Dice.d_8()
        self.blk = Dice.d_10()
        self.atk = Dice.d_6()
        total_skill_points = (self.hp + self.mp + self.blk + self.atk)
        while total_skill_points >= 25 or total_skill_points <= 20:
            self.hp = Dice.d_8()
            self.mp = Dice.d_8()
            self.blk = Dice.d_10()
            self.atk = Dice.d_6()
            total_skill_points = (self.hp + self.mp + self.blk + self.atk)


class Barb(Player):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Barbarian"
        self.hp = Dice.d_12()
        self.mp = Dice.d_6()
        self.blk = Dice.d_6()
        self.atk = Dice.d_8()
        total_skill_points = (self.hp + self.mp + self.blk + self.atk)
        while total_skill_points >= 25 or total_skill_points <= 20:
            self.hp = Dice.d_12()
            self.mp = Dice.d_6()
            self.blk = Dice.d_6()
            self.atk = Dice.d_8()
            total_skill_points = (self.hp + self.mp + self.blk + self.atk)


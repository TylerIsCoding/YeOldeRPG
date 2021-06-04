from Dice import *
from Utility import *
from Enemy import *

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
        self.skills = Skills.fireball, Skills.icewall 
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_6()
            self.mp = Dice.d_6()
            self.blk = Dice.d_4()
            total_skill_points = (self.hp + self.mp + self.blk)
    
    def attack(self, enemy):

        atk = Dice.d_6() + self.additional_damage
        final_attack = atk - enemy.blk if (atk - enemy.blk) >= 0 else 0
        enemy.hp -= final_attack
        if enemy.hp > 0:
            Utility.typingPrint("\nYou dealt " + str(final_attack) + " points of damage to " + str(enemy.name))
            Utility.typingPrint("\n" + str(enemy.name) + " has " + str(enemy.hp) + " hit points remaining.")
            enemy.attack(self)
        elif enemy.hp <= 0:
            Utility.typingPrint("\nYou did a devastating " + str(final_attack) + " points of damage! " + str(enemy.name) + " has been slain!")


class Warrior(Player):

    max_attack_str = "1d12"

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
        final_attack = atk - enemy.blk if (atk - enemy.blk) >= 0 else 0
        enemy.hp -= final_attack
        if enemy.hp > 0:
            Utility.typingPrint("\nYou dealt " + str(final_attack) + " points of damage to " + str(enemy.name) + '.')
            Utility.typingPrint("\n" + str(enemy.name) + " has " + str(enemy.hp) + " hit points remaining.")
            enemy.attack(self)
        elif enemy.hp <= 0:
            Utility.typingPrint("\nYou did a devastating " + str(final_attack) + " points of damage! " + str(enemy.name) + " has been slain!")


class Rogue(Player):

    max_attack_str = "1d6"

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
        final_attack = atk - enemy.blk if (atk - enemy.blk) >= 0 else 0
        enemy.hp -= final_attack
        if enemy.hp > 0:
            Utility.typingPrint("\nYou dealt " + str(final_attack) + " points of damage to " + str(enemy.name) + '.')
            Utility.typingPrint("\n" + str(enemy.name) + " has " + str(enemy.hp) + " hit points remaining.")
            enemy.attack(self)
        elif enemy.hp <= 0:
            Utility.typingPrint("\nYou did " + str(final_attack) + " points of damage. " + str(enemy.name) + " has been slain!")


class Barb(Player):

    max_attack_str = "1d8"

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
        final_attack = atk - enemy.blk if (atk - enemy.blk) >= 0 else 0
        enemy.hp -= final_attack
        if enemy.hp > 0:
            Utility.typingPrint("\nYou dealt " + str(final_attack) + " points of damage to " + str(enemy.name) + '.')
            Utility.typingPrint('\n' + str(enemy.name) + " has " + str(enemy.hp) + " hit points remaining.")
            enemy.attack(self)
        elif enemy.hp <= 0:
            Utility.typingPrint("\nYou did a devastating " + str(final_attack) + " points of damage! " + str(enemy.name) + " has been slain!")
        
    

class Skills:


    fireball = {
        'name': 'Fireball',
        'description': str("This causes flame damage"),
        'damage': Dice.d_10(),
        'mpcost': 4
    }

    icewall = {
        'name': 'Ice Wall',
        'description': str("This causes ice damage"),
        'damage': Dice.d_8(),
        'mpcost': 4
    }
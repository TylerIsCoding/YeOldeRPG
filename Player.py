from Dice import *
import Utility
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
        self.skill1 = AttackSkills.fireball
        self.skill2 = AttackSkills.icewall
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_6()
            self.mp = Dice.d_10()
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
        self.skill1 = AttackSkills.shieldbash
        self.skill2 = AttackSkills.whirlwind
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
        self.skill1 = AttackSkills.backstab
        self.skill2 = AttackSkills.kick
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
        self.skill1 = AttackSkills.overhead
        self.skill2 = AttackSkills.kick
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
        
    

class AttackSkills:

    fireball = {
        'name': 'Fireball',
        'des': str("\nYou unleash a mighty fireball!"),
        'damage': Dice.d_10(),
        'damagedice': "1d10",
        'mpcost': 5
    }

    icewall = {
        'name': 'Ice Wall',
        'des': str("\nA solid sheet of ice emerges from your fingertips!"),
        'damage': Dice.d_8() + Dice.d_4(),
        'damagedice': "1d8 + 1d4",
        'mpcost': 4
    }

    shieldbash = {
        'name': 'Sheild Bash',
        'des': str("\nYou throw your weight behind your sheild into the enemy!"),
        'damage': Dice.d_6() + Dice.d_6(),
        'damagedice': "2d6",
        'mpcost': 3
    }

    whirlwind = {
        'name': 'Whirlwind',
        'des': str("\nYou take your weapon and unleash a fury of attacks!"),
        'damage': Dice.d_8() + Dice.d_8(),
        'damagedice': "2d8",
        'mpcost': 4
    }

    kick = {
        'name': 'Powerful Kick',
        'des': str('\nYou kick the enemy with all of your power!'),
        'damage': Dice.d_6() + Dice.d_4(),
        'damagedice': "1d6 + 1d4",
        'mpcost': 3
    }

    backstab = {
        'name': 'Back Stab',
        'des': str("\nYou glide behind the enemy and attack from the rear!"),
        'damage': Dice.d_6() + 2,
        'damagedice': "1d6 + 2",
        'mpcost': 2
    }

    overhead = {
        'name': 'Overhead Swing',
        'des': str('\nYou swing your weapon downward with both hands as hard as you can!'),
        'damage': Dice.d_8() + Dice.d_4(),
        'damagedice': "1d8",
        'mpcost': 5
    }

class PassiveSkills:

    shadows = {
        'name': "Hide in Shadows",
        'des': str("\nYou attempt to hide in the shadows."),
        'mpcost': 4,
        'effectdice': Dice.d_4(),
        'effectdes': ("\nYour defense raises by {0} for this turn!".format('effectdice')),
        'effect': ' '#This needs to player.blk += the effect dice... 
    }

class BuffSkills:

    minorhealing = {
        'name': "Minor Healing",
        'des': str('\nYou attempt to heal yourself of minor wounds.'),
        'mpcost': 6,
        'effectdice': Dice.d_4(),
        'effectdes': ("\nYou heal yourself for {0} hit points!".format('effectdice')),
        'effect': ' '#This needs to player.hp += the effect dice...
    }

    majorhealing = {
        'name': "Major Healing",
        'des': str('\nYou attempt to heal yourself of major wounds.'),
        'mpcost': 8,
        'effectdice': Dice.d_6(),
        'effectdes': ("\nYou heal yourself for {0} hit points!".format('effectdice')),
        'effect': ' '#This needs to player.hp += the effect dice...
    }
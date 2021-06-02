from Dice import *
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
            Utility.typingPrint("You dealt " + str(final_attack) + " points of damage to the enemy!")
            Utility.typingPrint("They have " + str(enemy.hp) + " hit points remaining.")
            """Code for enemy turn here"""
        elif enemy.hp <= 0:
            Utility.typingPrint("You did a devastating " + str(final_attack) + " points of damage! The enemy has been slain!")


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
            Utility.typingPrint("You dealt " + str(final_attack) + " points of damage to the enemy!")
            Utility.typingPrint("They have " + str(enemy.hp) + " hit points remaining.")
            """Code for enemy turn here"""
        elif enemy.hp <= 0:
            Utility.typingPrint("You did a devastating " + str(final_attack) + " points of damage! The enemy has been slain!")


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
            Utility.typingPrint("You dealt " + str(final_attack) + " points of damage to the enemy!")
            Utility.typingPrint("They have " + str(enemy.hp) + " hit points remaining.")
            """Code for enemy turn here"""
        elif enemy.hp <= 0:
            Utility.typingPrint("You did a devastating " + str(final_attack) + " points of damage! The enemy has been slain!")


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
            Utility.typingPrint("\nYou dealt " + str(final_attack) + " points of damage to the enemy!")
            Utility.typingPrint("\nThey have " + str(enemy.hp) + " hit points remaining.")
            """Code for enemy turn here"""
        elif enemy.hp <= 0:
            Utility.typingPrint("You did a devastating " + str(final_attack) + " points of damage! The enemy has been slain!")

class Skills():

    def fireball(self, enemy):
        fire_atk = Dice.d_6() + 2
        final_fire_dmg = fire_atk - enemy.blk if (fire_atk - enemy.blk) >= 0 else 0
        enemy.hp -= final_fire_dmg
        if self.myPlayer.mp < 5:
            Utility.typingPrint("You do not have enough Mana.")
            self.player_combat_prompt(enemy)
        elif self.myPlayer.mp >= 5:
            self.myPlayer.mp -= 5
            Utility.typingPrint("You unleash a mighty fireball and deal " + str(final_fire_dmg) + " points of damage!")
            if enemy.hp > 0:
                Utility.typingPrint("They have " + str(enemy.hp) + " hit points remaining.")
                """Code for enemy turn here"""
            elif enemy.hp <= 0:
                Utility.typingPrint("You have burned the enemy to a crisp! You are victorious.")
    
    def iceblast(self, enemy):
        ice_atk = Dice.d_4() + 2
        final_ice_dmg = ice_atk - enemy.blk if (ice_atk - enemy.blk) >= 0 else 0
        enemy.hp -= final_ice_dmg
        if self.myPlayer.mp < 4:
            Utility.typingPrint("You do not have enough Mana.")
            self.player_combat_prompt()
        elif self.myPlayer.mp <= 4:
            self.myPlayer.mp -= 4
            Utility.typingPrint("You extend your arm, release a blast of ice, and deal " + str(final_ice_dmg) + " points of damage!")
            if enemy.hp > 0:
                Utility.typingPrint("They have " + str(enemy.hp) + " hit points remaining.")
                """Code for enemy turn here"""
            elif enemy.hp <= 0:
                Utility.typingPrint("You have frozen the enemy solid! They collapse and shatter. You are victorious.")



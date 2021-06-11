from Dice import *
import Utility
from Enemy import *

### Player Setup ###

class Player:

    additional_damage = 0
    
    def __init__(self, name):
        self.name = name

    def attack(player, enemy):
        damage = (player.atk + Player.additional_damage) - enemy.blk if (player.atk + Player.additional_damage) - enemy.blk > 0 else 0
        enemy.hp -= damage
        Utility.typingPrint(f'\nYou rolled a {player.atk} on your damage dice and {enemy.name} blocked {enemy.blk} of it. \
            You have dealt {damage} points of damage. The enemy has {enemy.hp} hit points remaining.')

    def skill1(player, enemy):
        if player.skill1 in AttackSkill:
            Utility.typingPrint(f"\n{player.skill1['effectdes']}")
            damage = player.skill1['effect'](player, enemy)
            enemy.hp -= damage
            player.mp -= player.skill1['mpcost']
        elif player.skill1 in BuffSkill:
            Utility.typingPrint(f"\n{player.skill1['effectdes']}")
            player.skill1['effect'](player)
            player.mp -= player.skill1['mpcost']
        elif player.skill1 in RecoverySkill:
            Utility.typingPrint(f"\n{player.skill1['effectdes']}")
            player.skill1['effect'](player)
            player.mp -= player.skill1['mpcost']

    def skill2(player, enemy):
        if player.skill2 in AttackSkill:
            Utility.typingPrint(f"\n{player.skill1['effectdes']}")
            damage = player.skill2['effect'](player, enemy)
            enemy.hp -= damage
            player.mp -= player.skill2['mpcost']
        elif player.skill2 in BuffSkill:
            Utility.typingPrint(f"\n{player.skill2['effectdes']}")
            player.skill2['effect'](player)
            player.mp -= player.skill2['mpcost']
        elif player.skill2 in RecoverySkill:
            Utility.typingPrint(f"\n{player.skill2['effectdes']}")
            player.skill2['effect'](player)
            player.mp -= player.skill2['mpcost']
    
    

class Mage(Player):

    max_attack_str = "1d6"

    def __init__(self, name):
        super().__init__(name)
        self.role = "Mage"
        self.hp = Dice.d_6()
        self.mp = Dice.d_10()
        self.blk = Dice.d_4()
        self.atk = Dice.d_6()
        self.additional_damage = 0
        self.skill1 = AttackSkill.shield_bash
        self.skill2 = AttackSkill.shield_bash
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
        self.additional_damage = 0
        self.skill1 = AttackSkill.shield_bash
        self.skill2 = AttackSkill.shield_bash
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
        self.additional_damage = 0
        self.skill1 = AttackSkill.shield_bash
        self.skill2 = AttackSkill.shield_bash
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 20 or total_skill_points <= 15:
            self.hp = Dice.d_12()
            self.mp = Dice.d_6()
            self.blk = Dice.d_6()
            total_skill_points = (self.hp + self.mp + self.blk)


class AttackSkill:

    def slash_damage(player, enemy):
        damage = (Dice.d_6() + player.additional_damage) - enemy.blk if (Dice.d_6() + player.additional_damage) - enemy.blk < 0 else 0
        enemy.hp -= damage
        Utility.typingPrint(f'\nYou dealt {damage} points of slash damage to {enemy.name}.')
        Utility.typingPrint(f'\n{enemy.name} has {enemy.hp} hit points remaining.')

    def fire_damage(player, enemy):
        damage = (Dice.d_8() + player.additional_damage) - enemy.blk if (Dice.d_6() + player.additional_damage) - enemy.blk < 0 else 0
        enemy.hp -= damage
        Utility.typingPrint(f'\nYou dealt {damage} points of fire damage to {enemy.name}.')
        Utility.typingPrint(f'\n{enemy.name} has {enemy.hp} hit points remaining.')

    def crushing_damage(player, enemy):
        damage = (Dice.d_6() + player.additional_damage) - enemy.blk if (Dice.d_6() + player.additional_damage) - enemy.blk < 0 else 0
        enemy.hp -= damage
        Utility.typingPrint(f'\nYou dealt {damage} points of crushing damage to {enemy.name}.')
        Utility.typingPrint(f'\n{enemy.name} has {enemy.hp} hit points remaining.')

    overhead_slash = {
        'name': "Overhead Slash",
        'mpcost': 4,
        'effect': slash_damage,
        'skilldes': "\nA powerful overhead slash. Does 1d6 damage.",
        'effectdes': "\nYou swing your weapon from overhead!"
    }
    
    shield_bash = {
        'name': "Shield Bash",
        'mpcost': 4,
        'effect': crushing_damage,
        'skilldes': "\nAttacks with the player's shield. Does 1d6 damage.",
        'effectdes': f"\nYou throw the weight of your shield into the enemy!"
    }

class BuffSkill:

    def raise_blk(player):
        effect = Dice.d_4()
        player.blk += effect

class RecoverySkill:

    def mp_recovery(player):
        recovery = Dice.d_4()
        player.mp += recovery
        Utility.typingPrint(f'\nYou recovered {recovery} MP this turn.')
    
    def minor_hp_recovery(player):
        recovery = Dice.d_4()
        player.hp += recovery
        Utility.typingPrint(f'\nYou recovered {recovery} HP this turn.')
    
    def major_hp_recovery(player):
        recovery = Dice.d_6()
        player.hp += recovery
        Utility.typingPrint(f'\nYou recovered {recovery} HP this turn.')
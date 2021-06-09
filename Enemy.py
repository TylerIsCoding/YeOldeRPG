from Dice import *
from Game import *
from Player import *
from Utility import *
import random

### Enemy Setup ###

class Enemy:
    
    additional_damage = 0

class Nick(Enemy):
    
    def __init__(self):
        self.name = "Nick the Scav"
        self.hp = Dice.d_8()
        self.mp = Dice.d_6()
        self.blk = Dice.d_4()
        self.skill1 = Skills.bushes
        self.skill2 = Skills.sweat
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 15 or total_skill_points <= 8:
            self.hp = Dice.d_8()
            self.mp = Dice.d_6()
            self.blk = Dice.d_4()
            total_skill_points = (self.hp + self.mp + self.blk)
    
    def attack(self, playerchar):
        skill1 = self.skill1
        skill2 = self.skill2
        if self.mp > self.skill1['mpcost'] and self.mp > self.skill2['mpcost']:
            skillchoice = random.choice((skill1, skill2))
            if skillchoice == skill1:
                atk = self.skill1['damage']
                dmg = atk
                final_attack = dmg - playerchar.blk if (dmg - playerchar.blk) >= 0 else 0
                playerchar.hp -= final_attack
                if playerchar.hp > 0:
                    Utility.typingPrint(f"\n\n{self.skill1['des']}")
                    Utility.typingPrint(f"\n{self.name} uses {self.skill1['name']} on {playerchar.name} for {final_attack} damage!")
                    Utility.typingPrint("\n\nThey dealt " + str(final_attack) + " points of damage to you.")
                    Utility.typingPrint("\nYou have " + str(playerchar.hp) + " hit points remaining.")
                    self.mp += randint(1, 2)
                    Utility.player_combat_prompt(playerchar, self)
                elif playerchar.hp <= 0:
                    Utility.typingPrint(f"\n\n{self.name} uses {self.skill1['name']} on {playerchar.name} for {final_attack} damage!")
                    Utility.typingPrint("\nYou have been killed!")
                    Utility.gameOver(self)
            elif skillchoice == skill2:
                atk2 = self.skill2['damage']
                dmg2 = atk2
                final_attack2 = int(dmg2) - playerchar.blk if (int(dmg2) - playerchar.blk) >= 0 else 0
                playerchar.hp -= final_attack2
                if playerchar.hp > 0:
                    Utility.typingPrint(f"\n\n{self.skill2['des']}")
                    Utility.typingPrint(f"\n\n{self.name} uses {self.skill2['name']} on {playerchar.name} for {final_attack2} damage!")
                    Utility.typingPrint("\n\nThey dealt " + str(final_attack2) + " points of damage to you.")
                    Utility.typingPrint("\nYou have " + str(playerchar.hp) + " hit points remaining.")
                    self.mp += randint(1, 2)
                    Utility.player_combat_prompt(playerchar, self)
                elif playerchar.hp <= 0:
                    Utility.typingPrint(f"\n\n{self.name} uses {self.skill2['name']} on {playerchar.name} for {final_attack2} damage!")
                    Utility.typingPrint("\nYou have been killed!")
                    Utility.gameOver(self)      
        else:
            atk = Dice.d_8() + self.additional_damage
            final_attack = atk - playerchar.blk if (atk - playerchar.blk) >= 0 else 0
            playerchar.hp -= final_attack
            if playerchar.hp > 0:
                Utility.typingPrint("\n\n" + str(self.name) + " attacks!")
                Utility.typingPrint("\n\nThey dealt " + str(final_attack) + " points of damage to you.")
                Utility.typingPrint("\nYou have " + str(playerchar.hp) + " hit points remaining.")
                self.mp += randint(1, 2)
                Utility.player_combat_prompt(playerchar, self)
            elif playerchar.hp <= 0:
                Utility.typingPrint("\n\n" + str(self.name) + " attacks!")
                Utility.typingPrint("\nThey did " + str(final_attack) + " points of damage! You have been killed!")
                Utility.gameOver(self)
    

class Steven(Enemy):
        
    def __init__(self):
        self.name = "Sweaty Steven"
        self.hp = Dice.d_8()
        self.mp = Dice.d_4()
        self.blk = Dice.d_6()
        self.skill1 = Skills.sweat
        self.skill2 = Skills.bushes
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 15 or total_skill_points <= 8:
            self.hp = Dice.d_8()
            self.mp = Dice.d_4()
            self.blk = Dice.d_6()
            total_skill_points = (self.hp + self.mp + self.blk)
    
    def attack(self, playerchar):
        if self.mp > self.skill1['mpcost']:
            skill1 = self.skill1
            skill2 = self.skill2
            choice = random.choice((skill1, skill2))
            if choice == skill1:
                self.mp -= self.skill1['mpcost']
                damage = self.skill1['damage']
                final_skill_damage = int(damage) - playerchar.blk if (int(damage) - playerchar.blk) >= 0 else 0
                playerchar.hp -= final_skill_damage
                Utility.typingPrint('\n{0} used {1} for {2} damage!'.format(str(self.name), str(self.skill1['name']), str(damage)))
                Utility.player_combat_prompt(playerchar, self)
            elif choice == skill2:
                self.mp -= self.skill2['mpcost']
                damage = self.skill2['damage']
                final_skill_damage = int(damage) - playerchar.blk if (int(damage) - playerchar.blk) >= 0 else 0
                playerchar.hp -= final_skill_damage
                Utility.typingPrint('\n{0} used {1} for {2} damage!'.format(str(self.name), str(self.skill2['name']), str(damage)))
                if playerchar.hp > 0:
                    Utility.player_combat_prompt(playerchar, self)
                elif playerchar.hp <= 0:
                    Utility.typingPrint('\nYou were killed!')
                    Utility.gameOver(self)
            else:
                Utility.typingPrint(f'\n{self.name} got confused and dropped his weapon and skipped their turn!')
                Utility.player_combat_prompt(playerchar, self)
        elif self.mp < self.skill1['mpcost']:
            atk = Dice.d_8() + self.additional_damage
            final_attack = atk - playerchar.blk if (atk - playerchar.blk) >= 0 else 0
            playerchar.hp -= final_attack
            if playerchar.hp > 0:
                Utility.typingPrint("\n\n" + str(self.name) + " attacks!")
                Utility.typingPrint("\n\nThey dealt " + str(final_attack) + " points of damage to you.")
                Utility.typingPrint("\nYou have " + str(playerchar.hp) + " hit points remaining.")
                Utility.player_combat_prompt(playerchar, self)
            elif playerchar.hp <= 0:
                    Utility.typingPrint("\nThey did " + str(final_attack) + " points of damage! You have been killed!")
                    Utility.gameOver(self)


class Skills:

    bushes = {
        'name': 'Hide in the Bushes',
        'des': str('\nThe enemy hides in the bushes!'),
        'damage': Dice.d_6(), #Temporarily just doing damage
        'mpcost': 4
    }

    sweat = {
        'name': 'Get Sweaty',
        'des': str('\n sweats all over you!'),
        'damage': Dice.d_6, #Temporarily just doing damage
        'mpcost': 4
    }
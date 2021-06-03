from Dice import *
from Utility import *
from Game import *
from Player import *

### Enemy Setup ###

class Enemy:
    
    additional_damage = 0

class Nick(Enemy):
    
    def __init__(self):
        self.name = "Nick the Scav"
        self.hp = Dice.d_6()
        self.mp = Dice.d_4()
        self.blk = Dice.d_4()
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 15 or total_skill_points <= 8:
            self.hp = Dice.d_6()
            self.mp = Dice.d_4()
            self.blk = Dice.d_4()
            total_skill_points = (self.hp + self.mp + self.blk)
    
    def attack(self, playerchar):
        atk = Dice.d_6() + self.additional_damage
        final_attack = atk - playerchar.blk if (atk - playerchar.blk) >= 0 else 0
        playerchar.hp -= final_attack
        if playerchar.hp > 0:
            Utility.typingPrint("\n\n" + str(self.name) + " attacks!")
            Utility.typingPrint("\n\nThey dealt " + str(final_attack) + " points of damage to you.")
            Utility.typingPrint("\nYou have " + str(playerchar.hp) + " hit points remaining.")
            Utility.player_combat_prompt(playerchar, self)
        elif playerchar.hp <= 0:
            Utility.typingPrint("\nThey did " + str(final_attack) + " points of damage! You have been killed!")
            Utility.gameOver()


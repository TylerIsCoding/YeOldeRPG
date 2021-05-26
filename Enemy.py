from Dice import *

### Enemy Setup ###

class Enemy:
    
    additional_damage = 0

class Nick(Enemy):
    def __init__(self):
        self.name = "Nick the Scav"
        self.hp = Dice.d_4()
        self.mp = Dice.d_4()
        self.blk = Dice.d_4()
        total_skill_points = (self.hp + self.mp + self.blk)
        while total_skill_points >= 15 or total_skill_points <= 8:
            self.hp = Dice.d_4()
            self.mp = Dice.d_4()
            self.blk = Dice.d_4()
            total_skill_points = (self.hp + self.mp + self.blk)
    
    def attack(self, playerchar):
        atk = Dice.d_4() + self.additional_damage
        final_attack = atk - playerchar.blk
        playerchar.hp -= final_attack
        if playerchar.hp > 0:
            print("They dealt " + str(final_attack) + " of damage to you!")
            print("You have " + str(playerchar.hp) + " hit points remaining.")
        elif playerchar.hp <= 0:
            print("They did a devastating " + str(final_attack) + " points of damage! You have been killed!")

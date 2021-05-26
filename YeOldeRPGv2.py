import cmd
import textwrap
import sys
import os
import datetime
import random

### Dice Rolls ###
class Dice:
    @staticmethod
    def d_20():
        return random.randint(1, 20)
    @staticmethod
    def d_12():
        return random.randint(1, 12)
    @staticmethod
    def d_10():
        return random.randint(1, 10)
    @staticmethod
    def d_8():
        return random.randint(1, 8)
    @staticmethod
    def d_6():
        return random.randint(1, 6)
    @staticmethod
    def d_4():
        return random.randint(1, 4)


### Player Setup ###

class Player:
    def __init__(self):
        self.name = ''
        self.role = ''
        self.hp = 0
        self.mp = 0
        self.blk = 0
        self.atk = 0
        self.skill_1 = ''
        self.skill_2 = ''
        self.skill_3 = ''

class Warrior:
    def roll_warrior(self):
        myPlayer.role = "Warrior"
        myPlayer.hp = Dice.d_20()
        myPlayer.mp = Dice.d_6()
        myPlayer.blk = Dice.d_8()
        myPlayer.atk = Dice.d_12()
        total_skill_points = (myPlayer.hp + myPlayer.mp + myPlayer.blk + myPlayer.atk)
        if total_skill_points >= 25 or total_skill_points <= 20:
            Warrior.roll_warrior(self)
        else:
            return

class Mage:
    def roll_mage(self):
        myPlayer.role = "Mage"
        myPlayer.hp = Dice.d_6()
        myPlayer.mp = Dice.d_10()
        myPlayer.blk = Dice.d_4()
        myPlayer.atk = Dice.d_10()
        total_skill_points = (myPlayer.hp + myPlayer.mp + myPlayer.blk + myPlayer.atk)
        if total_skill_points >= 25 or total_skill_points <= 20:
            Mage.roll_mage(self)
        else:
            return

class Rogue:
    def roll_rogue(self):
        myPlayer.role = "Rogue"
        myPlayer.hp = Dice.d_8()
        myPlayer.mp = Dice.d_8()
        myPlayer.blk = Dice.d_10()
        myPlayer.atk = Dice.d_6()
        total_skill_points = (myPlayer.hp + myPlayer.mp + myPlayer.blk + myPlayer.atk)
        if total_skill_points >= 25 or total_skill_points <= 20:
            Rogue.roll_rogue(self)
        else:
            return

class Barb:
    def roll_barb(self):
        myPlayer.role = "Barbarian"
        myPlayer.hp = Dice.d_12()
        myPlayer.mp = Dice.d_6()
        myPlayer.blk = Dice.d_6()
        myPlayer.atk = Dice.d_8()
        total_skill_points = (myPlayer.hp + myPlayer.mp + myPlayer.blk + myPlayer.atk)
        if total_skill_points >= 25 or total_skill_points <= 20:
            Barb.roll_barb(self)
        else:
            return

myPlayer = Player()

class Enemy:
    def __init__(self, name, hp, mp, blk, atk):
        self.name = ''
        self.hp = self
        self.mp = self
        self.blk = self
        self.atk = self


### Enemy List ###

Enemy.nick_the_scav = Enemy("Nick the Scav", Dice.d_6(), Dice.d_4(), Dice.d_4(), Dice.d_4())
Enemy.shturman = Enemy("Shturman", Dice.d_12(), Dice.d_6(), Dice.d_6(), Dice.d_6())
Enemy.hitch = Enemy("Hitch the Fan", Dice.d_6(), Dice.d_4(), Dice.d_4(), Dice.d_4())


### Main Menu ###

class Menu:
    def main_menu(self):
        print("############################")
        print("Welcome to Ye Olde Text RPG!")
        print("############################")
        print("       --(P)lay--           ")
        print("       --(Q)uit--           ")
        main_menu_selection = input("\n>>> ")
        if "p" in main_menu_selection.lower():
            Setup.player_setup_name(self)
        elif "q" in main_menu_selection.lower():
            quit()
        else:
            print("\n" * 100)
            print("You must select Play or Quit.\n")
            Menu.main_menu(self)


### Player setup. Naming the character and picking the class ###

class Setup:
    def player_setup_name(self):
        print("\nWhat is your name?")
        myPlayer.name = input(">>> ").title()
        Setup.player_setup_class(self)

    def player_setup_class(self):
        print("Are you a (W)arrior, (M)age, (R)ogue, or (B)arbarian?")
        answer_2 = input("\n>>> ")
        if "w" in answer_2.lower():
            Warrior.roll_warrior(self)
            Setup.confirmation(self)
        elif "m" in answer_2.lower():
            Mage.roll_mage(self)
            Setup.confirmation(self)
        elif "r" in answer_2.lower():
            Rogue.roll_rogue(self)
            Setup.confirmation(self)
        elif "b" in answer_2.lower():
            Barb.roll_barb(self)
            Setup.confirmation(self)
        else:
            self.player_setup_class()

    def confirmation(self):
        print("\n   " + myPlayer.name + " the " + myPlayer.role)
        print("########################")
        print("Hit Points: " + str(myPlayer.hp))
        print("Mana Points: " + str(myPlayer.mp))
        print("Defence: " + str(myPlayer.blk))
        print("Attack Points: " + str(myPlayer.atk))

        print("\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n>>> ")
        if "n" in answer_3:
            ChapterOne.intro_chap_one(self)
        elif "y" in answer_3:
            Setup.player_setup_class(self)
        else:
            print("\n\nYou have to choose (Y)es or (N)o")
            Setup.confirmation(self)


### The game starts here ###

class ChapterOne:

    def intro_chap_one(self):
        print("\n" * 100)
        print("############################")
        print("#       Chapter One        #")
        print("############################")
        print("\n"*5)


Menu.main_menu(Menu)

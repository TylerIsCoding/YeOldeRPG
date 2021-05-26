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


myPlayer = Player()


class Enemy:
    def __init__(self, name, hp, mp, blk, atk):
        self.name = ''
        self.hp = self
        self.mp = self
        self.blk = self
        self.atk = self


### Enemy List ###

Enemy.nick_the_scav = Enemy("Nick the Scav", d_6, d_4, d_4, d_4)
Enemy.shturman = Enemy("Shturman", d_12, d_6, d_6, d_6)
Enemy.


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
            self.main_menu()


### Player setup. Naming the character and picking the class ###

class Setup:
    def player_setup_name(self):
        print("\nWhat is your name?")
        myPlayer.name = input(">>> ")
        Setup.player_setup_class(self)

    def player_setup_class(self):
        print("Are you a (W)arrior or a (M)age?")
        answer_2 = input("\n>>> ")
        if "w" in answer_2.lower():
            myPlayer.role = 'Warrior'
            myPlayer.hp = Dice.d_20
            myPlayer.mp = Dice.d_6
            myPlayer.blk = Dice.d_8
            myPlayer.atk = Dice.d_12
            myPlayer.skill_1 = "Shield Bash"
            myPlayer.skill_2 = "Double Suplex"
            Setup.confirmation(self)
        elif "m" in answer_2.lower():
            myPlayer.role = 'Mage'
            myPlayer.hp = Dice.d_6
            myPlayer.mp = Dice.d_10
            myPlayer.blk = Dice.d_6
            myPlayer.atk = Dice.d_8
            myPlayer.skill_1 = "Fireball"
            myPlayer.skill_2 = "Ice Shard"
            myPlayer.skill_3 = "Healing"
            Setup.confirmation(self)
        else:
            self.player_setup_class()

    def confirmation(self):
        print("\nSo, you are " + myPlayer.name + " the " + myPlayer.role + "?")
        print("\n#############################")
        print("Hit Points: " + str(myPlayer.hp))
        print("Mana Points: " + str(myPlayer.mp))
        print("Defence: " + str(myPlayer.blk))
        print("Attack Points: " + str(myPlayer.atk))

        if myPlayer.skill_1:
            print("Skill 1: " + str(myPlayer.skill_1))
        if myPlayer.skill_2:
            print("Skill 2: " + str(myPlayer.skill_2))
        if myPlayer.skill_3:
            print("Skill 3: " + str(myPlayer.skill_3))

        print("\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n>>> ")
        if "n" in answer_3:
            ChapterOne.intro_chap_one(self)
        elif "y" in answer_3:
            Setup.player_setup_class(self)


### The game starts here ###

class ChapterOne:

    def intro_chap_one(self):
        print("\n" * 100)
        print("############################")
        print("#       Chapter One        #")
        print("############################")


Menu.main_menu(Menu)

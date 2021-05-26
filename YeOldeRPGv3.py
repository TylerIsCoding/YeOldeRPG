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


class Game:

    myPlayer = Player("name")

    def main_menu(self):
        print("############################")
        print("Welcome to Ye Olde Text RPG!")
        print("############################")
        print("       --(P)lay--           ")
        print("       --(Q)uit--           ")
        main_menu_selection = input("\n>>> ")
        if "p" in main_menu_selection.lower():
            self.player_setup()
        elif "q" in main_menu_selection.lower():
            quit()
        else:
            print("\n" * 100)
            print("You must select Play or Quit.\n")
            Self.main_menu(self)

    def player_setup(self):
        print("\nWhat is your name?")
        player_name = input(">>> ").title()
        print("Are you a (W)arrior, (M)age, (R)ogue, or (B)arbarian?")
        answer_2 = input("\n>>> ")
        if "w" in answer_2.lower():
            self.myPlayer = Warrior(player_name)
        elif "m" in answer_2.lower():
            self.myPlayer = Mage(player_name)
        elif "r" in answer_2.lower():
            self.myPlayer = Rogue(player_name)
        elif "b" in answer_2.lower():
            self.myPlayer = Barb(player_name)
        else:
            self.player_setup()
        while self.confirmation():
            if "w" in answer_2.lower():
                self.myPlayer = Warrior(player_name)
            elif "m" in answer_2.lower():
                self.myPlayer = Mage(player_name)
            elif "r" in answer_2.lower():
                self.myPlayer = Rogue(player_name)
            elif "b" in answer_2.lower():
                self.myPlayer = Barb(player_name)


    def confirmation(self):
        print("\n   " + self.myPlayer.name + " the " + self.myPlayer.role)
        print("########################")
        print("Hit Points: " + str(self.myPlayer.hp))
        print("Mana Points: " + str(self.myPlayer.mp))
        print("Defence: " + str(self.myPlayer.blk))
        print("Attack Points: " + str(self.myPlayer.atk))
        print("\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n>>> ")
        if "n" in answer_3:
            return False
        elif "y" in answer_3:
            return True
        else:
            print("\n\nYou have to choose (Y)es or (N)o")
            return False

game = Game()
game.main_menu()

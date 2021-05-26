from Dice import *
from Player import *
from Enemy import *

class Game:

    myPlayer = Player("name")
    nick = Nick()

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
            self.main_menu(self)

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
            return True
    
    def chapter_one(self):
        print("Placeholder")
        while self.myPlayer.hp > 0 and self.nick.hp > 0:
            combat_choice = input("Do you use a (S)kill or do you (A)ttack?!\n>>> ")


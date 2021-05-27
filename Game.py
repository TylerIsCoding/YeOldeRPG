from Dice import *
from Player import *
from Enemy import *

class Game:

    myPlayer = Player("name")
    nick = Nick()


    def main_menu(self):
        print("\n" * 100) 
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
        print("\nAre you a (W)arrior, (M)age, (R)ogue, or (B)arbarian?")
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
        print("Attack Dice: " + self.myPlayer.max_attack_str)
        print("\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n>>> ")
        if "n" in answer_3:
            return False
        elif "y" in answer_3:
            return True
        else:
            print("\n\nYou have to choose (Y)es or (N)o")
            return True
    

    def chapter_one_begin(self):
        print("\n" * 100)
        print("#########################")
        print("#      Chapter One      #")
        print("#########################")
        print("\n\n\nAs night falls you enter a small tavern on the crossroads.")
        print("There aren't many patrons in the tavern but the fireplace burns bright and the ale seems to be flowing.\n")
        self.table_answers()


    def table_answers(self):   
        print("Do you (C)all the Ale Wench or do you (R)est a bit before ordering?")
        answer = input(">>> ")
        if "c" in answer.lower():
            print("\nThe Ale Wench is passing by when you raise your hand to order. You order a large pint of cold ale and sit at the nearest empty table.")
            print("You feel tense and tired from the harsh travel of the road. You take a moment to reflect on where you're headed...")
            self.fame_or_escape()
        elif "r" in answer.lower():
            print("You find the nearest table and put down your pack and weapon. The dust from the road fills the air as \nyou kick the toes of your boots on the table leg.")
            print("You sit back in the wooden chair. A small creature approaches and hops into the vacant chair in front of you.")
            self.doge_convo()


    def fame_or_escape(self):
        print("\nAre you (L)ooking for fame and fortune on the road or are you trying to (E)scape an evil ruler's imprisonment?")
        answer_2 = input(">>> ")
        if "l" in answer_2.lower():
            print("\nYou've heard that there's gold and fame to be gained in this region. \nMany travelers have come to this area seeking it, but few have survived.")
            print("\nAs you daydream of a better life filled with treasure and women, \nyou see a small creature hop into the empty seat across the table from you")
            self.doge_convo()
        elif "e" in answer_2.lower():
            print("\nThe royal guard seems to be getting closer and closer to catching you. \nYou hear murmurs of Kingsman being spotted nearby in the last few days.")
            print("As you anxiously sip the ale that was just set in front of you, a small creature hops into the empty chair at the table.")
            self.doge_convo()
        
    
    def doge_convo(self):
        print("\n\n\n##################################################################################")
        print("#                                                               ▄▀▀▀█            #")
        print("#                                                           ,▄▀    █▌            #")
        print("#                                                           ▄█      j█           #")
        print("#                   ,▄▄                                    █▀ ▄      █           #")
        print("#                   ▐▌ ▀█▄                               ▄█  █▀      █           #")
        print("#                    █    ▀▄                           ,█▀  ▄▀       █           #")
        print("#                    ▐▌     ▀█▄                     ▄▄█▀   ▄█  ▄▄███  █          #")
        print("#                    ▐▌       ▀█▄           ,▄▄&▀▀▀▀`     █▌  █████▌  ▐▌         #")
        print("#                    █       ▀▀▀▀▀▀▄▄  ▄▄▀▀▀▀        ▄ ,██▀   ,█████  ▐▌         #")
        print("#                    █▄█▀           `▀▀-             `▀██▌   ▄████▀   ▐▌         #")
        print("#                  ▄█▀                                  --  ███▀      █▌         #")
        print("#               ▄█▀-                   ▄▄                            ,█          #")
        print("#            ,█▀-     ▀▀█▄          ,▄▀▀▀▀▄                          █           #")
        print("#           ▄█           █▌       ▄█▀      ▀█▄,                      █⌐          #")
        print("#          ▐▌            ▀Γ                   ▀█▄                     █          #")
        print("#          █▌    ▄███▀█▄               ▄██▀█▄▄  ▐█                    `█         #")
        print("#          █   ▄█████▌ █▌            ▄███▄▄████▄                       `█,       #")
        print("#         ▄█   █,▐██████        █ ▀██`▐█████████C                        █▄      #")
        print("#        ╒█     ▀██████         ▐▌  ▀▀████████▀                      ▀█   █▌     #")
        print("#        █          ▄█           ▀▌      ---                          ▐█   █⌐    #")
        print("#       █▌        ▄▀              ▀        ▄▄██▌                     ▐▌    └█    #")
        print("#      ▐█      ,█▀                    '▀▀▀▀▀`                       ██      ▐▌   #")
        print("#      █     ▄█▀                                                 ,▄▄▀        █   #")
        print("#     █▀   ▄█▀▄▄▄,▀█▄                                                        █   #")
        print("#     █   ▐██████████`                                                       █   #")
        print("#     █⌐  ▐▌███████▀  ▄ ,                                                   ▐█   #")
        print("#      █ ╒█  ▀███▀  ▀  '─4                                                  ▐▌   #")
        print("#      ▐█▐█ ∞,▀█▄     ` ª        ,▄█▀▀                                      ▐▌   #")
        print("#     ▄█▀█ ▀█▄▄████▄          ▄▄▀▀                                       ,   █   #")
        print("#   ,█▀  █  █████████████████▀                                      ,▄▐█▀▀   █-  #")
        print("#   █-   █▌  ╙█ ▀▀▀          ,▄▄▄▄▄▄                             ▄█▄█▀       █▌  #")
        print("#   █▄    ▀▄   ▀█▄  ,▄▄▄▄▄█▀▀▀                  ,█▀             ▀▀           ▐█  #")
        print("#   ▄█      █▄   `▀▀`                         ,▄█                            █▀  #")
        print("# ╒█▀        '▀█▄                          ,▄█▀                             ▄█,  #")
        print("#▄█              ▀▀█▄                ▄▄▄▀▀▀▀                                  █▄ #")
        print("#▀                  -▀▀▀▄▄▄▄▄,,,▄▄█▀▀                                          █▌#")
        print("#                           --▀▀                                               ▐█#")
        print("##################################################################################")





        #while self.myPlayer.hp > 0 and self.nick.hp > 0:
            #combat_choice = input("Do you use a (S)kill or do you (A)ttack?!\n>>> ")
            #if "s" in combat_choice.lower():
                #pass
            #elif "a" in combat_choice.lower():
                #self.myPlayer.attack(self.nick)
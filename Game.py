from Dice import *
from Player import *
from Enemy import *
from Utility import *

class Game:

    myPlayer = Player("name")
    nick = Nick()


    def main_menu(self):
        print("\n" * 100) 
        typingPrint("\n############################")
        typingPrint("\nWelcome to Ye Olde Text RPG!")
        typingPrint("\n############################")
        typingPrint("\n       --(P)lay--")
        typingPrint("\n       --(Q)uit--")
        print('\n' * 10)
        main_menu_selection = input("\n>>> ")
        if "p" in main_menu_selection.lower():
            self.player_setup()
        elif "q" in main_menu_selection.lower():
            quit()
        else:
            print("\n" * 100)
            typingPrint("\nYou must select Play or Quit.\n")
            self.main_menu(self)


    def player_setup(self):
        typingPrint("\nWhat is your name?")
        player_name = input("\n>>> ").title()
        typingPrint("\nAre you a (W)arrior, (M)age, (R)ogue, or (B)arbarian?")
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
        typingPrint("\n   " + self.myPlayer.name + " the " + self.myPlayer.role)
        typingPrint("\n########################")
        typingPrint("\nHit Points: " + str(self.myPlayer.hp))
        typingPrint("\nMana Points: " + str(self.myPlayer.mp))
        typingPrint("\nDefence: " + str(self.myPlayer.blk))
        typingPrint("\nAttack Dice: " + self.myPlayer.max_attack_str)
        typingPrint("\n\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n>>> ")
        if "n" in answer_3:
            return False
        elif "y" in answer_3:
            print('\n' * 10)
            return True
        else:
            typingPrint("\n\nYou have to choose (Y)es or (N)o")
            return True
    

    def chapter_one_begin(self):
        print("\n" * 100)
        fastTypingPrint("\n                            #########################")
        fastTypingPrint("\n                            #      Chapter One      #")
        fastTypingPrint("\n                            #########################")
        typingPrint("\n\n\nAs night falls you enter a small tavern on the crossroads.")
        typingPrint("\n\nThere aren't many patrons in the tavern but the fireplace \nburns bright and the ale seems to be flowing.\n\n\n")
        typingPrint('\n...............')
        print("\n##################################################################################")
        print("#                                                                                #")
        print("#                                  ▄▄▄▄▄,                                        #")                     
        print("#                      ▄█▀▀▀▀▀█▄██▀      ▀█,██▀▀▀█▄█▀▀▀██,                       #")                    
        print("#                  ▄███                    `             ▀██,                    #")                    
        print("#                 █▌                                        ▀█                   #")                 
        print("#                ██  ▐█                                   ▐█▀                    #")                  
        print("#               ██    ▀█▀                            ,,    ██                    #")                 
        print("#              █▀                                  ,▄█  ▄,  ██                   #")                 
        print("#              █▄   █████▀████▀▀██████r         ▄▄█▀  ,████▀▀                    #")               
        print("#               █  █▌                 ▀██▄           █▌   █▌      ,▄█▄           #")        
        print("#              ▐█ ██                     ██        ███▄▄█████████▀▀  ╙█          #")      
        print("#               ███▀▀▀█████▄▄▄██████▀▀▀▀███▀▀█▌    ▀██ ,,  █          ╘█         #")      
        print("#              ▄███            ,▄▄▄,         █     ▄█   ██ ██ ▄████    ▐█        #")     
        print("#             ▐█ █▌           ▐█   ▀█        █   ▄█   ███▀,▄█▀    █▌    ▐█       #")     
        print("#               ▀██▄           █▄,,▄█        ▀██▀   ,▄▄██▀▀█▌      █▄    █▌      #")    
        print("#                █▌ ▀▀███▄▄▄▄▄▄▄▄▄▄▄,,,,,,,▄██▀▀▀▀▀▀▀      ▐█       █    ▐█      #")    
        print("#                █                 ▀▀▀▀▀▀▀▀▀         ▐      █      █▌    j█      #")    
        print("#                █▌     ▐U                ▐W         ▌      █▌      █▌   j█      #")     
        print("#                █▌     ▐                  ▌         █       █      █▌   ▐█      #")    
        print("#                █      █                  █         █      ▐█      █▌   █▌      #")    
        print("#               ▐█      █                  █          ▌      █▄     █▌   ▐█      #")   
        print("#               ██      █                  █          █       █    █▀    ▐█      #")   
        print("#               █▌      ▌                  █          █       █,▄██      █       #")    
        print("#               █       ▌                  ▐          ▐      ▄██      ,▄██       #")     
        print("#              █▌      ▐                   ▐r            ,▄██▀ █▌  ▄█▀           #")       
        print("#              ██      █                    ▌       ,▄██▀▀▀▄,  ▐█▀▀              #")          
        print("#            ▄███▀█▄,,                       ,▄▄██▀▀▀     ▄ █r ██                #")           
        print("#           ▐█ █▌    `▀▀▀▀▀▀▀▀▀▀█████████▀▀▀▀`            ███▄███▌               #")           
        print("#            ▀██              ▄█▀▀▀█                    ,▄██▀    █               #")           
        print("#              █▄             █,   █▌              ,▄██▀▀▌      ▐█               #")           
        print("#              ████▄▄,         ▀▀▀▀`   ,,,▄▄▄▄███▀▀      █      █▌               #")          
        print("#              █     `█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀`    ▐▌           █      █                #")          
        print("#              █▌     █                     ▐             ▌   ▄█▀                #")           
        print("#              ██     █                     ▐             █,█▀                   #")           
        print("#                ▀█▄  █                     ▐  ,▄▄▄▄▄▄▄███▀▀                     #")          
        print("#                  ▀▀██▄▄▄,       ,,▄▄▄▄▄▄▄██▀▀`                                 #")         
        print("#                         ▀▀▀▀▀▀▀▀``                                             #")         
        print("#                                                                                #")
        print("##################################################################################")
        self.table_answers()


    def table_answers(self):   
        typingPrint("\n\nDo you (C)all the Ale Wench or do you (R)est a bit before ordering?")
        answer = input("\n\n>>> ")
        if "c" in answer.lower():
            typingPrint("\n\nThe Ale Wench is passing by when you raise your hand to order. You order a large pint of cold ale and sit at the nearest empty table.")
            typingPrint("\nYou feel tense and tired from the harsh travel of the road. You take a moment to reflect on where you're headed...")
            self.fame_or_escape()
        elif "r" in answer.lower():
            typingPrint("\n\nYou find the nearest table and put down your pack and weapon. The dust from the road fills the air as \nyou kick the toes of your boots on the table leg.")
            typingPrint("\nYou sit back in the wooden chair. A small creature approaches and hops into the vacant chair in front of you.")
            self.doge_convo()


    def fame_or_escape(self):
        typingPrint("\n\nAre you (L)ooking for fame and fortune on the road or are you trying to (E)scape an evil ruler's imprisonment?")
        answer_2 = input("\n>>> ")
        if "l" in answer_2.lower():
            typingPrint("\n\nYou've heard that there's gold and fame to be gained in this region. \nMany travelers have come to this area seeking it, but few have survived.")
            typingPrint("\nAs you daydream of a better life filled with treasure and women, \nyou see a small creature hop into the empty seat across the table from you")
            self.doge_convo()
        elif "e" in answer_2.lower():
            typingPrint("\n\nThe royal guard seems to be getting closer and closer to catching you. \nYou hear murmurs of Kingsman being spotted nearby in the last few days.")
            typingPrint("\n\nAs you anxiously sip the ale that was just set in front of you, a small creature hops into the empty chair at the table.")
            self.doge_convo()
        
    
    def doge_convo(self):
        typingPrint('\n' * 10)
        print("\n\n##################################################################################")
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

        typingPrint('\n\n"Hello there, traveler! What is your name?"')
        typingPrint("\n\nDo you (T)ell him or do you (R)emain silent?")
        answer = input("\n>>> ")
        if "t" in answer.lower():
            typingPrint("\nYou tell him your name is " + self.myPlayer.name + " and he wags his puffy tail happily.")
        elif "r" in answer.lower():
            typingPrint('\n"...The silent type, I see. Well then, I shall call you Booba!"')
            self.myPlayer.name = "Booba"
            typingPrint('\n\n"My name is Meelon Husk. It\'s a pleasure to meet you,' + self.myPlayer.name + '. I can see by your outfit and your gear, \nthat you appear to be an adventurer.')
        else:
            pass

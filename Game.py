import typing
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
            self.main_menu()


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
            else:
                break


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
            typingPrint("\n\nYou have to choose (Y)es or (N)o\n")
            return True
    

    def chapter_one_begin(self):

        print("\n" * 100)
        fastTypingPrint("\n                            #########################")
        fastTypingPrint("\n                            #      Chapter One      #")
        fastTypingPrint("\n                            #########################")
        typingPrint("\n\n\nAs night falls you enter a small tavern on the crossroads.")
        typingPrint("\n\nThere aren't many patrons in the tavern but the fireplace \nburns bright and the ale seems to be flowing.\n\n\n")
        typingPrint('\n                         ')
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
            typingPrint("\n\nThe Ale Wench is passing by when you raise your hand to order. \nYou order a large pint of cold ale and sit at the nearest empty table.")
            typingPrint("\nYou feel tense and tired from the harsh travel of the road. \nYou take a moment to reflect on where you're headed...")
            self.fame_or_escape()
        elif "r" in answer.lower():
            typingPrint("\n\nYou find the nearest table and put down your pack and weapon. The dust from the road fills the air as \nyou kick the toes of your boots on the table leg.")
            typingPrint("\n\nYou sit back in the wooden chair. A small creature approaches and hops into the vacant chair in front of you.")
            self.doge_convo()


    def fame_or_escape(self):

        typingPrint("\n\nAre you (L)ooking for fame and fortune on the road or are you trying to (E)scape an evil ruler's imprisonment?")
        answer_2 = input("\n>>> ")
        if "l" in answer_2.lower():
            typingPrint("\n\nYou've heard that there's gold and fame to be gained in this region. \nMany travelers have come to this area seeking it, but few have survived.")
            typingPrint("\n\nAs you daydream of a better life filled with treasure and women, \nyou see a small creature hop into the empty seat across the table from you.")
            self.doge_convo()
        elif "e" in answer_2.lower():
            typingPrint("\n\nThe royal guard seems to be getting closer and closer to catching you. \nYou hear murmurs of Kingsman being spotted nearby in the last few days.")
            typingPrint("\n\nAs you anxiously sip the ale that was just set in front of you, a small creature hops into the empty chair at the table.")
            self.doge_convo()
        
    
    def doge_convo(self):

        typingPrint('\n' * 4)
        typingPrint('                         ')
        print("\n##################################################################################")
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
            typingPrint('\n"It is very nice to meet you, ' + self.myPlayer.name + '! \nI can tell by looking at you that you must be a ' + self.myPlayer.role.lower() + '."')
            self.cross_roads()
        elif "r" in answer.lower():
            print('\n')
            slowTypingPrint('...')
            typingPrint('\n\n"The silent type, I see. Well then, I shall call you Booba!"')
            self.myPlayer.name = "Booba"
            typingPrint('\n\n"My name is Meelon Husk. It\'s a pleasure to meet you, ' + self.myPlayer.name + '. I can see by your outfit and your gear, \nthat you must be a ' + self.myPlayer.role.lower() + '.')
            self.cross_roads()
        else:
            self.doge_convo()
    

    def cross_roads(self):

        typingPrint('\n\n"Listen, I have some information that you may find valuable. \n\nI know that we don\'t know one another,\nbut we should talk in private."')
        typingPrint('\n\n"Let\'s go outside and speak near the stables..."\n')
        typingPrint('\nDo you (F)ollow the doge or do you (R)emain seated?')
        answer = input("\n>>> ")
        if "f" in answer.lower():
            self.stables()
        elif "r" in answer.lower():
            typingPrint('\n\nYou hesitate to rise from your seat. You\'re having trouble trusting a doge you just met...')
            typingPrint('\nMeelon turns and notices that you have not gotten up from the table.')
            typingPrint('\n"Listen, ' + self.myPlayer.name + '... \nYou\'re just going to have to trust me. This is imporant information."')
            self.stables()
        else:
            typingPrint('You must choose one of the two options.')
            self.cross_roads()
    
    def stables(self):

        typingPrint('                         ')                                                                                            
        print('\n\n\n##################################################################################')
        print('#               ~      ,,                                                        #')               
        print('#              ▓       ╙▄>),                                                     #')               
        print('#             ╒M]▀      ▓Ü┐"φ                                                    #')               
        print('#             ▐ ▐ ▀,    ]╢ % ╬     .⌐=╖, ,,                                      #')               
        print('#             ▐     █▄∞0$▓▌  ]]*▄,`"*      ╙▀╙╝  "W.                             #')               
        print('#              ▌ ,▄▀`√"   ▓█╓] $   ▀▌```````""ⁿM∞╖╓` ╚╜[ ═,                      #')               
        print('#              ╙█▀ / `     ∩╙█▌▐     L               `*w,  ▀Xw,                  #')               
        print('#              ▓  `,`     NΓ  " .. ⌐                      "ª▄▌ ▀╚D═,             #')               
        print('#             ▓* ▓╒`      Ü▌                                  ▀▄ ║  █            #')               
        print('#             ▌,╣ ▌            Γ       ╘           ~            ╙N  ╟▌▄,         #')               
        print('#            ╒▄ `█ ¿ ▐ ╒,▓              b             "~           ▀,╙ ▌▐▄,      #')               
        print('#            ▓ j▐▒   ▐ ╢╢               ▐                 \.         ▀,▀  Ü█,    #')               
        print('#           Æ  ]▌║   █ ▌        \        ▌                   \\        ▀,  ▓"▄   #')               
        print('#         ▄▀   ▐ ▐ ┐ ▐ C        ▐  ░     ╘                     "┐        N   █,  #')               
        print('#          █   ]  U" ² ░ ,     `  /┘      ▌                            `  ╙ ²▐▐▄ #')               
        print('#          ╘µ     ▓L\╘` ╩█   ]   ,]       ▐                              \ ╚  ┘▐ #')               
        print('#          ▌      ▓ \k  ▀▓m═`             C                                ╚  ║▀ #')            
        print('#           ▌      `▌ ╙╕       ¿           ▌                             ╙   ╙,  #')           
        print('#          ▐                  ^            ▌                                   N #')         
        print('#          ▓                  U^           ▌ ]           `.                 «    #')         
        print('#          ▌                 ▓ ~,         ▐ j               ~                    #')       
        print('#         ]                               ▌ ╝r                                   #')      
        print('#         ▐ j                            ▓                                       #')     
        print('#         ▌ `       ┌    `         ╙╦  ▄▀                                        #')     
        print('#               ┌   Γ  ╒         ┌  ▐▀    ^      ,                               #')      
        print('#        ▐      `                  ╔`                                            #')          
        print('#        ▓                   ─^   Æ         ▐     ]                              #')         
        print('#        ▌                    ¡ ¿`           r                         ┘         #')         
        print('#       ▐                ,,   ,┘             ▌     ├                             #')         
        print('#       ▌      ▄██▄  L . ▄▐▌¿`               ▐                         ┌         #')               
        print('#      ▐       █████   ,█  █                 ]      L                  v         #')              
        print('#       ▀▄     ▌ ]█▀╛P,▀ ╓ ▓                  ▌     ╢                 ,[         #')       
        print('#         ╙N▄, ▀▀▀    █ ╒╜"                   ▓     ▐                 ^          #')           
        print('#              ▀N▄▄mÆ▌═²`                     ▐                                  #')            
        print('#                                              ▌                              ¿" #')               
        print('#                                              ▀     L                      ¿    #')               
        print('#                                               L    |             -`,^          #')               
        print("##################################################################################")
                                                                                                                                                                                      
        typingPrint('\n\n\nThe two of you walk out of the tavern and into the cool, dark night. \nYou hear the sounds of sleeping horses in the stables as you approach.')
        typingPrint('\n\nThe small doge looks around before he begins to speak.')
        typingPrint('\n\n"There is a patch of woods nearby... It has been said that a very powerful foe lies in those woods..."')
        typingPrint('\n"He goes by the name of')
        slowTypingPrint('...')
        typingPrint(' Shturman."')
        typingPrint('\n\n"We must make our way to the Woods and see if we can find him. He poses a very real threat upon the Land of Olde."')
        typingPrint('\n\nBefore Meelon can finish explaining the situation you hear something behind a nearby tree.')
        typingPrint('\n\n\n"CHEEKIE BREEKIE!"')
        self.nick_fight()


    def nick_fight(self):
        typingPrint('\n                         ')
        print("\n\n\n#################################################################################################")
        print("#                                                                                               #")
        print("#                                  ▄▄▄▄▀▀▀▀▀▀▀▀▀▀█▄▄▄╓                                          #")
        print("#                              ╔▄▀▀▀  ▄     ╨       -▀▀▀█▄▄                                     #")
        print("#                            ▄█▀▄             Æ   ▀     ç ▀█▄                                   #")
        print("#                          ▄█╚       ╚`                     ▀▄                                  #")
        print("#                        ▄▀╚                 ▀   '        ╘¬ ▀█▄                                #")
        print("#                      ╒█╚    ▀  ╙                       ▀     ▀█                               #")
        print("#                      █`              ▀                        ▐█                              #")
        print("#                     █▀  ▀      ▀                               ▐█                             #")
        print("#                    ▄▌     ▀                                    ▐▌                             #")
        print("#                   ╔█ 7ⁿ                               ▄        █-                             #")
        print("#                   █C      Æ                  ▀▄.     ┌▌     ▄▀ █                              #")
        print("#                  ▐▌                            ▀&ç   █   ╓█▀-  ▐▌                             #") 
        print("#                   █   P            ╔▄▄▄▄▄╓      ╓╨▀    ,█▀,▄▄▄▄▄█▄              ▄█▀       ▄µ  #")
        print("#                   █▌      :        ▀═   ╛▀▀▀█▄▄¿╔▀▄   ▐█-█▀═████▀█▄          ;▄▀═       ▄█▀   #")
        print("#                ;▄▄█▌      -           ▄▄▄▄▄▄▄▄▄▄▀╝▌    ▀▄`██▀▀▀╔  █         ▄▀      ,▄█▀╙     #")
        print("#              ▄▀▀▄▄,▀▀▄⌐            ╒█▀▐█▄▄██µ ▄█▌       ▐▌ '▀▀▀   █        █▌     ╔█▀         #")
        print("#            ▄█═▄▀, ▀▀▄              ╘▀▄▄██████▀╝ ▌        █▄      ▄▀█▄      ╘█µ     ▀▄         #")
        print("#            █▄▐-    ▄▌                 ╙▀▀╝╙   ▄▀        ╓▄█    ,▄▌ ▐▌        ▀▄.    ▀█▄       #")
        print("#             ██   ▄▀ ▀▄                             ,▄█▀▀▀╚▀▀▀▀▀▀╚  ▐▌          ▀▄     ▀█⌐     #")
        print("#             ███▄▄⌠▀M▄▀                 ç▄▄▄▄▄▄▄███▀▀¬      ,  ▄▄▄  █L           ▐█.     █     #")
        print("#             ▐█  ▀▀▀▀██▄▄▄▄▄ççç▄▄▄▄▄▀▀▀▀╚╙-                 ▐█ ¬╙╛ `█           ▄▄▀-  ╓▄▀▀     #")
        print("#              ▀█          ¬╙╙╙╙╚╘            ▄▄▄▀██          █ ▐▄   █⌐      ,▄█▀▀  ▄▄▀▀        #")
        print("#              ▄█▀▄,                   ,▄▄▄█▀▀╩ ▄█▀    ¬▄▄▄▄▄▀▀  ▀   ▐▌     █▀- ▄▄▀▀¬           #")
        print("#              █` `▀▌                  ▀╛       ╚  ╓▄▀    '`          █    ▐█▄ █▌               #")
        print("#              ▀█                                ▄█▀                 █▀      ▀█∞▀               #")
        print("#               ╙█ ▀█▄▄,                       ▄█▀            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                  #")
        print("#          ▄▄▀÷  ▐▌   ╚▀▀▀█▄▄,                ▀╛             █   █▄          ███                #")
        print("#      ╔▄█▀▀      ▀█▌       ╛▀▀▀▀                             ▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀╚                 #")
        print("#   ╔▄▀▀           ▐█▌                                             -█  ╙▀▀▀▄▄▄▄                 #")
        print("# ▄█▀                █▄              '▀▄▄▄                      ▄█ⁿ▐▌         ╙▀▀█µ             #")
        print("# █                   ▀█▄                ╙▀▀▀█▄▄▄µ             ▀▌  █▌             █⌐            #")
        print("#                       ▀▀█▄▄                   ▄█                ▐▌              ▐█            #")
        print("#                           ╘▀█▄              4▀▀                 █r               █▌           #")
        print("#                              ▀██▄▄                 ╓▄▄µ        █5                ▐▌           #")
        print("#                                 └▀▀███▄▄µ    ,▄▄█▀▀▀╛└▀▀▀▀█▄▄▄▐▌                  ▀           #")
        print("#                                      '  ▀▀▀▀▀▀╘              ╨▀                               #")
        print("#################################################################################################")
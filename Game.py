import typing
from Dice import *
from Player import *
from Enemy import Nick
from Utility import Utility

class Game:

    myPlayer = Player("name")
    nick = Nick()


    def main_menu(self):

        print("\n" * 100) 
        Utility.typingPrint("\n############################")
        Utility.typingPrint("\nWelcome to Ye Olde Text RPG!")
        Utility.typingPrint("\n############################")
        Utility.typingPrint("\n       --(P)lay--")
        Utility.typingPrint("\n       --(Q)uit--")
        print('\n' * 10)
        main_menu_selection = input("\n>>> ")
        if "p" in main_menu_selection.lower():
            self.player_setup()
        elif "q" in main_menu_selection.lower():
            quit()
        else:
            print("\n" * 100)
            Utility.typingPrint("\nYou must select Play or Quit.\n")
            self.main_menu()


    def player_setup(self):

        Utility.typingPrint("\nWhat is your name?")
        player_name = input("\n>>> ").title()
        Utility.typingPrint("\nAre you a (W)arrior, (M)age, (R)ogue, or (B)arbarian?")
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

        Utility.typingPrint("\n   " + self.myPlayer.name + " the " + self.myPlayer.role)
        Utility.typingPrint("\n########################")
        Utility.typingPrint("\nHit Points: " + str(self.myPlayer.hp))
        Utility.typingPrint("\nMana Points: " + str(self.myPlayer.mp))
        Utility.typingPrint("\nDefence: " + str(self.myPlayer.blk))
        Utility.typingPrint("\nAttack Dice: " + self.myPlayer.max_attack_str)
        Utility.typingPrint("\n\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n>>> ")
        if "n" in answer_3:
            return False
        elif "y" in answer_3:
            print('\n' * 10)
            return True
        else:
            Utility.typingPrint("\n\nYou have to choose (Y)es or (N)o\n")
            return True
    

    def chapter_one_begin(self):

        print("\n" * 100)
        Utility.fastTypingPrint("\n                            #########################")
        Utility.fastTypingPrint("\n                            #      Chapter One      #")
        Utility.fastTypingPrint("\n                            #########################")
        Utility.typingPrint("\n\n\nAs night falls you enter a small tavern on the crossroads.")
        Utility.typingPrint("\n\nThere aren't many patrons in the tavern but the fireplace \nburns bright and the ale seems to be flowing.\n\n\n")
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
            Utility.typingPrint('\n                         ')
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

        Utility.typingPrint("\n\nDo you (C)all the Ale Wench or do you (R)est a bit before ordering?")
        answer = input("\n\n>>> ")
        if "c" in answer.lower():
            Utility.typingPrint("\n\nThe Ale Wench is passing by when you raise your hand to order. \nYou order a large pint of cold ale and sit at the nearest empty table.")
            Utility.typingPrint("\nYou feel tense and tired from the harsh travel of the road. \nYou take a moment to reflect on where you're headed...")
            self.fame_or_escape()
        elif "r" in answer.lower():
            Utility.typingPrint("\n\nYou find the nearest table and put down your pack and weapon. The dust from the road fills the air as \nyou kick the toes of your boots on the table leg.")
            Utility.typingPrint("\n\nYou sit back in the wooden chair. A small creature approaches and hops into the vacant chair in front of you.")
            self.doge_convo()


    def fame_or_escape(self):

        Utility.typingPrint("\n\nAre you (L)ooking for fame and fortune on the road or are you trying to (E)scape an evil ruler's imprisonment?")
        answer_2 = input("\n>>> ")
        if "l" in answer_2.lower():
            Utility.typingPrint("\n\nYou've heard that there's gold and fame to be gained in this region. \nMany travelers have come to this area seeking it, but few have survived.")
            Utility.typingPrint("\n\nAs you daydream of a better life filled with treasure and women, \nyou see a small creature hop into the empty seat across the table from you.")
            self.doge_convo()
        elif "e" in answer_2.lower():
            Utility.typingPrint("\n\nThe royal guard seems to be getting closer and closer to catching you. \nYou hear murmurs of Kingsman being spotted nearby in the last few days.")
            Utility.typingPrint("\n\nAs you anxiously sip the ale that was just set in front of you, a small creature hops into the empty chair at the table.")
            self.doge_convo()
        
    
    def doge_convo(self):
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
            Utility.typingPrint('\n' * 4)
            Utility.typingPrint('                         ')
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

            Utility.typingPrint('\n\n"Hello there, traveler! What is your name?"')
            Utility.typingPrint("\n\nDo you (T)ell him or do you (R)emain silent?")
            answer = input("\n>>> ")
            if "t" in answer.lower():
                Utility.typingPrint("\nYou tell him your name is " + self.myPlayer.name + " and he wags his puffy tail happily.")
                Utility.typingPrint('\n\n"It is very nice to meet you, ' + self.myPlayer.name + '! \nI can tell by looking at you that you must be a ' + self.myPlayer.role.lower() + '."')
                self.cross_roads()
            elif "r" in answer.lower():
                print('\n')
                Utility.slowTypingPrint('...')
                Utility.typingPrint('\n\n"The silent type, I see. Well then, I shall call you Booba!"')
                self.myPlayer.name = "Booba"
                Utility.typingPrint('\n\n"My name is Meelon Husk. It\'s a pleasure to meet you, ' + self.myPlayer.name + '. I can see by your outfit and your gear, \nthat you must be a ' + self.myPlayer.role.lower() + '.')
                self.cross_roads()
            else:
                self.doge_convo()
        

    def cross_roads(self):

        Utility.typingPrint('\n\n"Listen, I have some information that you may find valuable. \n\nI know that we don\'t know one another,\nbut we should talk in private."')
        Utility.typingPrint('\n\n"Let\'s go outside and speak near the stables..."\n')
        Utility.typingPrint('\nDo you (F)ollow the doge or do you (R)emain seated?')
        answer = input("\n>>> ")
        if "f" in answer.lower():
            Utility.typingPrint('\nYou rise from your chair and follow the doge to the tavern door.')
            self.stables()
        elif "r" in answer.lower():
            Utility.typingPrint('\n\nYou hesitate to rise from your seat. You\'re having trouble trusting a doge you just met...')
            Utility.typingPrint('\nMeelon turns and notices that you have not gotten up from the table.')
            Utility.typingPrint('\n"Listen, ' + self.myPlayer.name + '... \nYou\'re just going to have to trust me. This is imporant information."')
            self.stables()
        else:
            Utility.typingPrint('You must choose one of the two options.')
            self.cross_roads()
    
    def stables(self):

        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
            Utility.typingPrint('                         ')                                                                                            
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
                                                                                                                                                                                        
            Utility.typingPrint('\n\n\nThe two of you walk out of the tavern and into the cool, dark night. \nYou hear the sounds of sleeping horses in the stables as you approach.')
            Utility.typingPrint('\n\nThe small doge looks around before he begins to speak.')
            Utility.typingPrint('\n\n"There is a patch of woods nearby... It has been said that a very powerful foe lies in those woods..."')
            Utility.typingPrint('\n"He goes by the name of')
            Utility.slowTypingPrint('...')
            Utility.typingPrint(' Shturman."')
            Utility.typingPrint('\n\n"We must make our way to the Woods and see if we can find him. \nHe poses a very real threat upon the Land of Olde."')
            Utility.typingPrint('\n\nBefore Meelon can finish explaining the situation you hear something behind a nearby tree.')
            Utility.typingPrint('\n\n\n"CHEEKIE BREEKIE!"')
            Utility.typingPrint('\n\nA wild Nick the Scav appears!')
            self.nick_fight()


    def nick_fight(self):

        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
            Utility.typingPrint('\n                         ')
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
            
            result = Utility.initiative()
            if result:
                Utility.player_combat_prompt(self.myPlayer, self.nick)
            else:
                Nick.attack(self.nick, self.myPlayer)
            self.post_nick_fight()
            
    def post_nick_fight(self):
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:

            Utility.typingPrint('\n\n"Wow!" says Meelon. "It looks like you can fight... \nLook, he dropped this after you got him."')
            print('\n\n\n###########################################################################################################################')
            print("#                                                           ▄▄,,,                                                         #")  
            print("#                        █444444▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██╢╢▓╢██▄,,,,,,,,,,                                 ▄▄███▄     #") 
            print("#                       █▀     ██╢██╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╢███╢▓▓▓▓█▓▓█▓▓▓▓▓▓▓▓▓████████████████████████████████████████▄   #")
            print("#                     ▄█▀     ▐█╬██████████████████████████████████████████████████████████████████████████████████████   #") 
            print("#                   ▄█▀       █╢▓█▌                      ,,,▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄█████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     #") 
            print("#            ,▄▄▄█▀▀         █╣▓▓█                ▄▀             ,,,,▄▄▄▄▄▄▄▄▄▄Æ▀        ,^▄█                             #")
            print("#         ▐▀▀ ▌     ╚       ▐█╢╢█▌                 `▀▀▀▀▀`                    ,,,,...⌐∞'▄▄█▀                              #") 
            print("#         █   '     ▌       ▐█▓██           ,,,,..⌐¬∞∞═══^^''''``    ,,▄▄▄▄▄▄▄▄▄▄▄4▀▀▀▀▀                                  #") 
            print("#         █,,...⌐⌐¬════^^''''7▀▀`              ,,,▄▄▄▄▄▄▄▄&4▀▀▀▀▀▀▀▀▀▀ `                                                  #") 
            print("#         █            ,,,▄▄▄▄▄▄▄▄▄████████████▓▀                                                                         #") 
            print("#        ▐█4▀▀▀▀▀▀▀▀▀▀█▀██▀   ▐█ ╢█▓▓▓▓▓▓▓█▓▓███                                                                          #")
            print("#        ▐▌           █ ▀█  ,▄█╢ █╢▓▓▓▓▓▓╫█▓▓█╣▌                                                                          #")
            print("#        ▐▌      ,,, ▐█████████ ▓██▓▓▓▓▓▓█╢▓███                                                                           #")
            print("#       ,█     ,██▀-'   ▀▀   █ ▓▓▓██████╢▓▓▓█╣▌                                                                           #")
            print("#      ▄▀     ▄██            █▓▓▓▓▓▓▓▓▓▓▓▓▓▓█╣█                                                                           #")
            print("#    ╒█      ██▀            ██╢╢╢████████████▀                                                                            #")
            print("#    █       ██▌                                                                                                          #")
            print("#   █-       ▐██                                                                                                          #")  
            print("#  ▐█,      ,▄██                                                                                                          #") 
            print("#    `▀444████▀                                                                                                           #")
            print('###########################################################################################################################')  
            Utility.typingPrint('\n\nThe doge bends down and picks up a weapon off of the ground.')
            Utility.typingPrint('\nIt appears to be a TOZ-106! You pick it up. It adds (+ 1) to your damage roll.')
            self.myPlayer.additional_damage += 1
            Utility.typingPrint('\n\nYou now do ' + str(self.myPlayer.max_attack_str) + " + " + str(self.myPlayer.additional_damage) + ' points of damage.')
            
            continue_prompt_2 = input("\n\n>>> Hit enter to continue")
            if '' in continue_prompt_2:
                self.woods()


    def woods(self):
        pass
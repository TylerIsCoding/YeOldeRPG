##### Imports #####
from Player import *
from Enemy import *
from Utility import *
###################

class Game:

    myPlayer = Player("name")
    nick = Nick()
    steven = Steven()
    attack = Attack()
    buff = Buff()
    restore = Recovery()

    def title_screen(self):

        Utility.clear()

        print('##################################################################################################################################################################################')
        print('#                                                                                                                                                                                #')
        print('#                           ,▄Æ▀▀▀▀▄                                                                                                                                             #')
        print('#                       ▄▄▄ ▄██▄  ▄▄  ▀▄                                                                                                                 ,█▀▀▀▀▀▄,               #')
        print('#                     ,█`  ▀ ,,-▀▓▓▓▓ ██4▄                                               ▐█           ▄█▌                                            ▄A▄█▀ ,▄▄▄  ▀█              #')
        print('#                   █▌  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀ ▄█▄▄▄▄▄▄▄▄▄,,                                   █ ▀▄       ▄▀▐█                                           ▄▀  ▐▌ á▓▓▓▓▓L █▀▀▄            #')
        print('#             ▄▄▄▄▄▄A▀▀3▓▓▓▀▀▀▀▀▀▀▀▀▀▀╙         ,,▄▄▄▄██▀                     ▄         ╒█       ,▄▀  ▐▌  ,▄                               ,,,▄▀▀4█,╓▓▓▄╦&▓▓▓▓▓▓▓▓▓&&m▀▀▀&▄▄▄▄,  #')
        print('#           ▀▀▀P&æææææÆPP▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀-`                              ▀▄   ▀PPP▀  ▄▄▄æ▄▄▄     ▀▀▀                         ▄▄▄4▀▀▀`-   ╚▓▀▓▓▓▀▀▓▓▓▓████▄æN▀▀▀▀▀▀▀▀▀PP▀▀▀ #')
        print('#                                                                                █▄     ▄▀`       `▀▄     ▄▀                       `▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  `                         #')
        print('#                                                                                 █∩  ,█             ▀▄  j█    ,▄█████▄▄                                                         #')
        print('#                                                                             ▄▄▄▄▀   █               ▐µ   ,▄███╢▓▓█▀  ▀██▄                                                      #')
        print('#                                     ,▄████▄▄                                       ▐▌               ▐█▄███╢▓▓▓▓█▀       ▀█▄                                                    #')
        print('#                                  ,▄██▓█▀   ▀▀█▄                             ▀▀▄▄▄   █           ▄▄███▓▓▓██▌▓▓▓█▀       ,,,▀▀█▄▄,                                               #')
        print('#                               ▄███╢▓█▀        `▀█▄                              ,█   █▄   ▄▄█████╢▓▓▓▓▓▓▓╢██▀▀ ,,  ,▄▄▄▀      `▀▀▀█▄▄                                          #')
        print('#                           ▄▄███▓▓▓█▀             ▀█▄▄                         ╓█▀  ,▄▄████▓▓▓▓▓▓▓▓▓▓▓▓██▀▀   ▀▀ -▀▀▀                ▀▀██▄,                                   ▄ #')
        print('#                         ▄██╢▓▓▓▓█▀           ╖      ▀▀█▄▄                    ,▄▄████▓╢╣▓▓▓▓▓▓▓▓▓▓██▀▀                       ╙8,         "▀██▄,                           ,▄██▓ #') 
        print('#                      ,██╢▓▓▓╢▓█▀              ▓         ▀██▄,            ,▄███▓╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                               "╙ºæ,       `▀▀██▄▄▄▄,                 ▄██╢▓▓█ #')       
        print('#                  ,▄███╢▓▓██▀▀                  ▓           "██      ,▄▄███╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▀▀       ,@             w,              ╙&╗,           ▀▀▀▀█▄▄         ▄███▓▓█▀`  #')          
        print('#              ,▄███╢▓▓▓▓▓█▀                      ╙R⌐          ▀███████╢╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▀         ,▓                 ▐                  `               `▀▀█▄▄▄████▓▓▓▓█-    #')                 
        print('#         ,▄▄███▓╢▓▓▓▓╬█▀▀                ,                      ███╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▀-                               ╙W,                                ▄███▓╣▓▓▓▓▓▓██`     #')                   
        print('#    ,▄▄███╢▓▓▓▓▓▓▓█▀▀        φ╜          ▓                        ▀▀██╢╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓█`                                     ╙╨                        ,▄████╢▓▓▓▓▓▓▓█▀▀        #')
        print('# ▄███╢╢▓▓▓▓▓▓▓▓█▀          ,▓            ▐                  R▄       -▀▀████▓▓▓▓▓▓▓▓▓█                                                               ▄██▓▓▓▓▓▓▓▓▓▓▓▓█           #')
        print('# ▀█▓▓▓▓▓▓▓▓▓█▀             `                                  ▀▄,          `▀███▓╣▓▓█                                                               ▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌           #')
        print('#   ▀▀█╢▓▓▓▓█                                                                    ▀███▌                                                               ▐█╢╢▓▓▓▓▓▓▓▓▓▓▓█▌           #')
        print('#      ▀▀▀██                                                                                                                                           - ▀▀▀▀▀▀▀▀▀▀▀▀            #')
        print('#                                                                                                                                                                                #')
        print('#                                                            __     __     ____  _     _        _____  _____   _____                                                             #')
        print('#                                                            \ \   / /    / __ \| |   | |      |  __ \|  __ \ / ____|                                                            #')
        print('#                                                             \ \_/ /__  | |  | | | __| | ___  | |__) | |__) | |  __                                                             #')
        print('#                                                              \   / _ \ | |  | | |/ _` |/ _ \ |  _  /|  ___/| | |_ |                                                            #')
        print('#                                                               | |  __/ | |__| | | (_| |  __/ | | \ \| |    | |__| |                                                            #')
        print('#                                                               |_|\___|  \____/|_|\__,_|\___| |_|  \_\_|     \_____|                                                            #')
        print('#                                                                                                                                                                                #')
        print('#                                                                              Press Enter to begin!                                                                             #')
        print('#                                                                                                                                                                                #')
        print('#                                                                          Created by Tyler McKenna 2021                                                                         #')
        print('#                                                                                                                                                                                #')
        print('##################################################################################################################################################################################')
        start = input('')
        if '' in start:
            self.main_menu()
    
    def main_menu(self):

        Utility.clear() 
        TextSpeed.fast("\n################################")
        TextSpeed.fast("\n# Welcome to Ye Olde Text RPG! #")
        TextSpeed.fast("\n################################")
        TextSpeed.fast("\n         --(P)lay--")
        TextSpeed.fast("\n        --(O)ptions--")
        TextSpeed.fast("\n         --(Q)uit--")
        print('\n' * 5)
        main_menu_selection = input("\n>>> ")
        if "p" in main_menu_selection.lower():
            self.player_name()
        elif "o" in main_menu_selection.lower():
            self.options()
        elif "q" in main_menu_selection.lower():
            quit()
        else:
            TextSpeed.fast("\nYou must select Play or Quit.\n")
            self.main_menu()
    
    def options(self):
        
        Utility.clear()
        TextSpeed.fast("\n############################")
        TextSpeed.fast("\n#         Options          #")
        TextSpeed.fast("\n############################")
        TextSpeed.fast("\n    1.) Story Text Speed")
        TextSpeed.fast("\n      2.) Combat Speed")
        TextSpeed.fast("\n          (R)eturn")
        answer = input('\n\n>>> ')
        if str(1) in answer:
            self.story_text_speed()
        elif str(2) in answer:
            self.combat_text_speed()
        elif "r" in answer.lower():
            self.main_menu()
        else:
            TextSpeed.fast('\nYou need to make a valid selection.')
            self.options()
    
    def story_text_speed(self):

        Utility.clear()
        TextSpeed.fast("\n############################")
        TextSpeed.fast("\n#     Story Text Speed     #")
        TextSpeed.fast("\n############################")
        TextSpeed.fast("\n        1.) Normal")
        TextSpeed.fast("\n        2.) Fast")
        TextSpeed.fast("\n        3.) Instant")
        TextSpeed.fast("\n         (R)eturn")
        answer = input('\n\n>>> ')
        if str(1) in answer:
            Utility.story = TextSpeed.normal
            self.options()
        elif str(2) in answer:
            Utility.story = TextSpeed.fast
            self.options()
        elif str(3) in answer:
            Utility.story = TextSpeed.instant
            self.options()
        elif "r" in answer.lower():
            self.options()
        else:
            Utility.story('\nYou need to make a valid selection.')
            self.story_text_speed()
    
    def combat_text_speed(self):

        Utility.clear()
        Utility.story("\n############################")
        Utility.story("\n#       Combat Speed       #")
        Utility.story("\n############################")
        Utility.story("\n        1.) Normal")
        Utility.story("\n        2.) Fast")
        Utility.story("\n        3.) Instant")
        Utility.story("\n         (R)eturn")
        answer = input('\n\n>>> ')
        if str(1) in answer:
            Utility.combat = TextSpeed.normal
            self.options()
        elif str(2) in answer:
            Utility.combat = TextSpeed.fast
            self.options()
        elif str(3) in answer:
            Utility.combat = TextSpeed.instant
            self.options()
        elif "r" in answer.lower():
            self.options()
        else:
            Utility.story('\nYou need to make a valid selection.')
            self.story_text_speed()

    def player_name(self):

        Utility.clear()
        Utility.story("\nWhat is your name?")
        self.myPlayer.name = input("\n\n>>> ").title()
        self.player_setup()

    def player_setup(self):

        Utility.clear()
        Utility.story("\nAre you a (W)arrior, (M)age, (R)ogue, or (B)arbarian?")
        answer_2 = input("\n\n>>> ")
        if "w" in answer_2.lower():
            self.myPlayer = Warrior(self.myPlayer.name)
        elif "m" in answer_2.lower():
            self.myPlayer = Mage(self.myPlayer.name)
        elif "r" in answer_2.lower():
            self.myPlayer = Rogue(self.myPlayer.name)
        elif "b" in answer_2.lower():
            self.myPlayer = Barb(self.myPlayer.name)
        else:
            self.player_setup()
        while self.skillselection():
            if "w" in answer_2.lower():
                self.myPlayer = Warrior(self.myPlayer.name)
            elif "m" in answer_2.lower():
                self.myPlayer = Mage(self.myPlayer.name)
            elif "r" in answer_2.lower():
                self.myPlayer = Rogue(self.myPlayer.name)
            elif "b" in answer_2.lower():
                self.myPlayer = Barb(self.myPlayer.name)
            else:
                break
    
    
    def skillselection(self):

        Attacks = [ShieldBash, OverheadSlash, Flurry, TripWire, Backstab, Fireball, Lightning, IceWall, Kick]
        Buffs = [Rage, Anger, Barrier, Shadows]
        Recovery = [HealMinor, HealMajor, Bandage]

       
        Utility.clear()
        if self.myPlayer.skills == []:
            Utility.story('\n\nYou now must choose your starting skills.')
        elif self.myPlayer.skillpoints < 2:
            self.confirmation()
            return True
        else:
            Utility.story('\n\nChoose another skill.')
            Utility.story('\n\nSkills chosen so far:')
            Utility.story('\n#####################\n')
            for skill in self.myPlayer.skills:
                Utility.story(f"\n{skill.name}")
        Utility.story("\n\n#####################")
        Utility.story("\n1.) Attacks")
        Utility.story("\n2.) Buffs")
        Utility.story("\n3.) Restorative")
        Utility.story("\n4.) Continue")
        answer = input('\n\n>>> ')
        if str(1) in answer:
            SkillList = Attacks
        elif str(2) in answer:
            SkillList = Buffs
        elif str(3) in answer:
            SkillList = Recovery
            for skill in SkillList:
                skill.role = self.myPlayer.role
        elif str(4) in answer:
            self.confirmation()
            return True
        count = 1
        ListStore = []
        for skill in SkillList:
            if skill.role == self.myPlayer.role:
                ListStore.append(skill)
                Utility.story(f"\n{count}.) {skill.name} | Cost: {skill.skillcost}")
                count += 1
        Utility.story(f"\n{count}.) Return")
        Utility.story(f'\n\nYou have {self.myPlayer.skillpoints} points remaining.\n')
        selection = input('\n\n>>> ')
        if selection == '':
            Utility.story('\nPlease enter a valid selection. Try again.')
            Utility.continue_prompt()
            self.skillselection()
        elif (int(selection) <= len(ListStore)):
            choice = ListStore[int(selection) - 1]
            if self.myPlayer.skillpoints >= choice.skillcost and choice not in self.myPlayer.skills:
                self.myPlayer.skills.append(choice)
                self.myPlayer.skillpoints -= (choice.skillcost)
                self.skillselection()
            elif self.myPlayer.skillpoints < choice.skillcost:
                Utility.story('\nNot enough skill points.')
                Utility.continue_prompt()
                self.skillselection()
            else:
                Utility.story('\nSkill already selected. Choose a different skill.')
                Utility.continue_prompt()
                self.skillselection()
        elif (int(selection) == count):
            self.skillselection()
        elif (selection != int):
            Utility.story('\nPlease enter a valid selection. Try again.')
            Utility.continue_prompt()
            self.skillselection()



    def confirmation(self):

        Utility.clear()
        a = (f"{self.myPlayer.name} the {self.myPlayer.role}")
        Utility.story(f'{a:^24}')
        Utility.story("\n########################\n")
        Utility.story(f"\nHit Points: {self.myPlayer.hp}")
        Utility.story(f"\nMana Points: {self.myPlayer.mp}")
        Utility.story(f"\nDefence: {self.myPlayer.defense}")
        Utility.story(f"\nAttack Dice: {self.myPlayer.max_attack_str}")
        Utility.story("\n\n#######| Skills |#######\n")
        for skill in self.myPlayer.skills:
            Utility.story(f'\n{skill.name}')
        Utility.story("\n\n########################")
        Utility.story("\n\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n\n>>> ")
        if "n" in answer_3:
            self.skillselection == False
        elif "y" in answer_3:
            print('\n' * 10)
            self.player_setup()
            self.skillselection == True
        else:
            Utility.story("\n\nYou have to choose (Y)es or (N)o\n")
            self.confirmation()
    

    def chapter_one_begin(self):

        Utility.clear()
        Utility.story("\n                            #########################")
        Utility.story("\n                            #      Chapter One      #")
        Utility.story("\n                            #########################")
        Utility.story("\n\n\nAs night falls you enter a small tavern on the crossroads.")
        Utility.story("\n\nThere aren't many patrons in the tavern but the fireplace \nburns bright and the ale seems to be flowing.")
        Utility.continue_prompt()
        Utility.clear()
        print("##################################################################################")
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

        Utility.story("\n\nDo you (C)all the Ale Wench or do you (R)est a bit before ordering?")
        answer = input("\n\n>>> ")
        if "c" in answer.lower():
            Utility.story("\n\nThe Ale Wench is passing by when you raise your hand to order. \nYou order a large pint of cold ale and sit at the nearest empty table.")
            Utility.story("\nYou feel tense and tired from the harsh travel of the road. \nYou take a moment to reflect on where you're headed...")
            self.fame_or_escape()
        elif "r" in answer.lower():
            Utility.story("\n\nYou find the nearest table and put down your pack and weapon. The dust from the road fills the air as \nyou kick the toes of your boots on the table leg.")
            Utility.story("\n\nYou sit back in the wooden chair. A small creature approaches and hops into the vacant chair in front of you.")
            self.doge_convo()
        else:
            Utility.story('You must choose one of the two options.')
            self.table_answers()


    def fame_or_escape(self):

        Utility.story("\n\nAre you (L)ooking for fame and fortune or are you trying to (E)scape an evil ruler's imprisonment?")
        answer_2 = input("\n>>> ")
        if "l" in answer_2.lower():
            Utility.story("\n\nYou've heard that there's gold and fame to be gained in this region. \nMany travelers have come to this area seeking it, but few have survived.")
            Utility.story("\n\nAs you daydream of a better life filled with treasure and women, \nyou see a small creature hop into the empty seat across the table from you.")
            self.doge_convo()
        elif "e" in answer_2.lower():
            Utility.story("\n\nThe royal guard seems to be getting closer and closer to catching you. \nYou hear murmurs of Kingsman being spotted nearby in the last few days.")
            Utility.story("\n\nAs you anxiously sip the ale that was just set in front of you, a small creature hops into the empty chair at the table.")
            self.doge_convo()
        else:
            Utility.story('You must choose one of the two options.')
            self.fame_or_escape()
        
    
    def doge_convo(self):
        Utility.continue_prompt()
        Utility.clear()
        print("##################################################################################")
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

        Utility.story('\n\n"Hello there, traveler! What is your name?"')
        Utility.story("\n\nDo you (T)ell him or do you (R)emain silent?")
        answer = input("\n>>> ")
        if "t" in answer.lower():
            Utility.story(f"\nYou tell him your name is {self.myPlayer.name} and he wags his puffy tail happily.")
            Utility.story(f'\n\n"It is very nice to meet you, {self.myPlayer.name}! \nI can tell by looking at you that you must be a {self.myPlayer.role.lower()}."')
            self.cross_roads()
        elif "r" in answer.lower():
            print('\n')
            TextSpeed.slow('...')
            Utility.story('\n\n"The silent type, I see. Well then, I shall call you Booba!"')
            self.myPlayer.name = "Booba"
            Utility.story(f'\n\n"My name is Meelon Husk. It\'s a pleasure to meet you, {self.myPlayer.name}. \
            \nI can see by your outfit and your gear, \nthat you must be a {self.myPlayer.role.lower()}.')
            self.cross_roads()
        else:
            self.doge_convo()
        

    def cross_roads(self):

        Utility.story('\n\n"Listen, I have some information that you may find valuable. \n\nI know that we don\'t know one another,\nbut we should talk in private."')
        Utility.story('\n\n"Let\'s go outside and speak near the stables..."\n')
        Utility.story('\nDo you (F)ollow the doge or do you (R)emain seated?')
        answer = input("\n>>> ")
        if "f" in answer.lower():
            Utility.story('\nYou rise from your chair and follow the doge to the tavern door.')
            self.stables()
        elif "r" in answer.lower():
            Utility.story('\n\nYou hesitate to rise from your seat. You\'re having trouble trusting a doge you just met...')
            Utility.story('\nMeelon turns and notices that you have not gotten up from the table.')
            Utility.story(f'\n"Listen, {self.myPlayer.name}... You\'re just going to have to trust me. \nThis is imporant information."')
            self.stables()
        else:
            Utility.story('You must choose one of the two options.')
            self.cross_roads()
    
    def stables(self):

        Utility.continue_prompt()
        Utility.clear()                                                                                            
        print('##################################################################################')
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
                                                                                                                                                                                    
        Utility.story('\n\n\nThe two of you walk out of the tavern and into the cool, dark night. \nYou hear the sounds of sleeping horses in the stables as you approach.')
        Utility.story('\n\nThe small doge looks around before he begins to speak.')
        Utility.story('\n\n"There is a patch of woods nearby... It has been said that a very powerful foe lies in those woods..."')
        Utility.story('\n"He goes by the name of')
        TextSpeed.slow('...')
        Utility.story(' Shturman."')
        Utility.story('\n\n"We must make our way to the Woods and see if we can find him. \nHe poses a very real threat upon the Land of Olde."')
        Utility.story('\n\nBefore Meelon can finish explaining the situation you hear something behind a nearby tree.')
        Utility.story('\n\n\n"CHEEKIE BREEKIE!"')
        Utility.story('\n\nA wild Nick the Scav appears!')
        self.nick_fight()


    def nick_fight(self):

        Utility.continue_prompt()
        Utility.clear()
        print("#################################################################################################")
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
            Turn.turn_count(-1)
            Utility.player_combat_prompt(self.myPlayer, self.nick)
        else:
            Turn.turn_count(0)
            Utility.buff_check(self.nick, self.myPlayer)
        self.post_nick_fight()
            

    def post_nick_fight(self):
        
        Utility.continue_prompt()
        Utility.clear()
        Utility.story('\n\n"Wow!" says Meelon. "It looks like you can fight... \nLook, he dropped this after you got him."')
        get_loot = input('\n\n>>> Hit enter to loot the scav.')
        if '' in get_loot:
            Utility.clear()
            print('###########################################################################################################################')
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
            Utility.story('\n\nThe doge bends down and picks up a weapon off of the ground.')
            Utility.story('\nIt appears to be a TOZ-106! You pick it up. It adds (+ 1) to your damage roll.')
            self.myPlayer.additional_damage += 1
            Utility.story(f'\n\nYou now do {str(self.myPlayer.max_attack_str)} + {str(self.myPlayer.additional_damage)} points of damage.')
            Utility.continue_prompt()
            self.woods()


    def woods(self):
        Utility.clear()
        print('#####################################################################################')                                                                                
        print('#                                       ▐▄                                          #')
        print('#                                      ▄▀█                                          #')
        print('#                                     █▄▀        █▄                                 #')
        print('#                                      ▀          █▀▄                               #')
        print('#                                                  ▌ █                              #')
        print('#                                       ▄▄▌        ▌  ▀█,                           #')
        print('#                                    ▄▀▀▐▀       ,█     ▀▄                          #')
        print('#                                  ▄▀  ▄▀      ▄▀¬       ▐▄                         #')
        print('#                                 █     ▀▀▄▄▄▀▀           ▌                         #')
        print('#                                ¬▌                      █                          #')
        print('#                                 █                    ▄▀                           #')
        print('#                                 █             ,      █                            #')
        print('#                                █▀      ▄    ▄▀▀       █                           #')
        print('#                            ,▄▀▀     ,Æ█    ▄ ▐         █                          #')
        print('#                           █▀      ,▀   ▀∞∞▀   ▀▄       ▐▌                         #')
        print('#                           ▌       ▌             ▀▄      █                         #')
        print('#                          ,▌       ▌               ▄     ▐▌                        #')
        print('#                         █▀      ▄,▄              ▄▀     ▐▌                        #')
        print('#                          ▀▄      N             ▄▀      ▄▀      ▄██▄               #')
        print('#                             ▀▀▄    ▀▄        ,▀     ,█▀     ▄▄███ ▀█              #')
        print('#                          ,,,▄▄▄████▄ ▀     ,▀    ▄█▀▄▄▄███▀▀▀¢██   █▌             #')
        print('#          ██▀██████████▀▀█▀▀▀▀ÅΣΣÅ▒▒Å▀████████████▀▀▀▀▀╟▒▒▒▒▒▒▄█ █ ▐█              #')
        print('#        ▄█▀▀█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄█▀▀%▒▒▒▒▒██▒▒▒█Ñ▒▒▒▒▒▒▒▒▒▒▒⌠▀▀▀████  ▌ ▀█              #')
        print('#      ,█▀ █▄▀██▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▄██▀▀██¢▒▒▒▐█▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒█▌ █ ╓▄▀█▄            #')
        print('#     ╒█  ▄⌐██ ▀█▌▒▒▒▄▄██▀▀▒▒▒▒▒░▒▄███▀▒▒▒▒▒████████▀▀▀██▄▄▒▒▒██ ▀▄ █  █            #')
        print('#     █ ▄█▀ ██ ▄██▀▀▀≡▒▒▒▒▒██▌▒▄██▀██▒▒█▒▒▒█▒█▌    ▀▀█▀▀████▀▀▀██  █ ▄█`            #')
        print('#     ▀▌ ▄█▀ ▄█▀▒▒▒▄█▀▀▒▒▄▀▒▄█▀▀  ██▒▄█▒▒▒▒█▒██           -▀▀████ ,█▀▀              #')
        print('#      ▀█  ▄█▀▒█▀▀▄▄████▀████    █▀▒█▀▒▒▒▄▌▀▒▒█                ▀▀▀▀                 #')
        print('#       ╙███▄███▀▀▀¬      -    ▄█▀▒████▀██▌▒▒▒█                                     #')
        print('#          -                  ██▀▀▀▀▄▄▄   ▀██▐█                                     #')
        print('#                            █▀ ▄▄▄▀▀  ▀▀0▄ ▀██                                     #')
        print('#                           █▌█▀    █▀  ,  ▀▌ █▌                                    #')
        print('#                          █▀ ▌  █▀▀██▀▄█▀  ███                                     #')
        print('#                          ╙▀█▀  █⌐ ▀▀█▀ ▀████                                      #')
        print('#                             ▀█▄  ,▄███▀▀-                                         #')
        print('#                               ▀▀▀▀                                                #')
        print('#####################################################################################')
        regen = HealMajor.dice()
        Utility.story(f'\n\nYou both settle in for some rest. You regain {(str(regen))} hit points from sleeping.')
        self.myPlayer.hp += regen
        Utility.story('\nDaylight creeps over the hills and treetops. The two of you gather your gear and start towards the Woods.')
        Utility.story('\nAs you walk Meelon continues explaining about Shturman.')
        Utility.story('\n\n"Shturman is said to be in possession of the mighty Kappa container...\nIt has the ability to hold a vast amount of items in a very small space."')
        Utility.story('\n\n"If we could aquire the Kappa container AND remove Shturman\'s evil hold \non the Woods, I\'m sure that the King would be most grateful."')
        Utility.story(f'\n\n"Listen, {self.myPlayer.name}, we should head East. \nThat\'s where Shturman was last spotted... or so I\'ve heard..."')
        Utility.story('\n\n\nThe two of you head East to see if you can find any traces of Shturman. \nAs you try to locate any clues you hear the sound of twigs snapping\nand the unmistakable smell of sweat!')
        Utility.story('\n\nA wild Sweaty Steven appears!')
        Utility.continue_prompt()
        self.steven_fight()

    def steven_fight(self):
        Utility.clear()
        print('######################################################################################')
        print('#                          ▄▄▄█                         ▀▄▄▄▄▄╓                      #')
        print('#                     ╒▄█▀▀▀                             "▀█ ╙▀▀▀▀█▄╓                #')
        print('#                 ╔▄█▀▀-                                   ▀█      `▀█▄              #')
        print('#               ▄█▀  ,                                      ▀█        -▀█ç           #')
        print('#             ▄█T ,█▀▀▀▀▀█▀                                  ╙█▄         ▀█▄         #')
        print('#            ▄▀  ▄█-  ▄▄█7                              ,▄▄▄█▀▀█           ▀█        #')
        print('#           ▐█  ▄█  ▄▀█▀                            ▄█▀▀▀╙ ▄▄▀▀▀       ▄▄▄▄,▐█       #')
        print('#          J█  ▐█ ╥▀ █▌                            █▀  ▄▄▀▀╓▄▄▄▄▄█▀▀▀▀▀⌠  "▀██▌      #')
        print('#          █▌  █▌ █   ╚█C                          ▐█▀▀  ▄█▀╛╘ ▄¬H    ▌▐Ç    ▐▌      #')
        print('#          █▌  ▐▌ █    █        FAST MT            ▐█  ▄█▀ ,   █▐+, ▄▄▄█▄    ▐▌      #')
        print('#         ▐█          ;▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄╓            █▌     ██▀▀▀▀▀▀█¿   ▀█   ▐▌      #')
        print('#          █▌▄█▀▀█▀▀▀▀▀╙             ╛╙▀▀▀▀▀█▄▄▄     ▀P  ╓▄█▌██▌   ²█    ▐▌  ]█      #')
        print('#           ▀█▄▄█▀         ▄▄█▀▀▀▀▀           █▌▀▀▀██▄▄█▀▀▄█        └█▄  ▄█   █      #')
        print('#              █▀▄▄     ▄█▀▀▄▄▄▄▄▄¿ ▄≡▄       █    █▌    ╔█"          ╙▀▄     █      #')
        print('#              █▄▄█▀   ▀▀▄█▀ ██  █ █ █▀      ▐▌   ▐█     █C   ▄▄▄██▄    ▀█   j█      #')
        print('#              ██▌▐█    ▐█ç ▐████ █▀ ╙       █▌   █      █▄▄█▀▀    ▀█▄   ▐█µ ▐▌      #')
        print('#              ▀██▀"     ▀█▀█▄▄█▀▀          ▄█▄▄▄▄█    ▄█▀▀          ▀█▄  ▐█ ╙       #')
        print('#           ▄█▀██-       ▀▄▀N▄▄             █∞   \█   ▄█               █   █         #')
        print('#          █▀▄▄ ▀█▄╓ ▄µ   -▀   `           ▐█▄▄▄▄▐▌  ,█       ▄▄       █  █▀         #')
        print('#         █ █▀     ▀██▀█▄▄▄                 █▌╙╙▐█¬ ▄█╚         ▄     █▌ █▀          #')
        print('#        █▀▄█      ▄█    `╙▀▀▀█▄▄▄        ;▄█▄▄▄██▀▀▀                ▄█▀▀▀           #')
        print('#       █▀,▀     ;█▀             ╙▀▀▀▀▀▀▀▀▀▀╙╙                      █▀ █C            #')
        print('#      ███▀▀▄▄  █▀                                           ▄▄   ▄▀7  ▐█            #')
        print('#      █▌    █▌ ▀█µ                                       ╥▄█▀▄▄█▀╙     ▀█           #')
        print('#      ▐█    ▐█   █▄                                   ▄█▀▀▀▀▀▀          █▌          #')
        print('#       ▐█    ▀█   █▄                               ▄█▀╧                ▄▀ ▀▀▀█▌     #')
        print('#        ▀▌    ▀█   █¿                           ▄█▀╝               ╔▄█▀▀     ▀▀▀▀▀▀ #')
        print('#         ▀█    ▀█   █▄                     ;▄█▀▀═█▌          ;▄▄▄█▀▀▀               #')
        print('#          ▀█    █▌   ▀▄                ,▄█▀▀  ▀▀▀ ▀▀█▄▄██▀▀▀▀╛                      #')
        print('#           ▀█    █`   ▀█           ▄▄█▀▀╛                                           #')
        print('#            ▐█⌐  ▐█    ▀█     ╓▄▄█▀╝                                                #')
        print('#             └█▄▄ ╚█▄  ,██▄█▀▀▀`                                                    #')
        print('#                ▀▀█▄███▀-                                                           #')
        print('######################################################################################')
        result = Utility.initiative()
        if result:
            Turn.turn_count(-1)
            Utility.buff_check(self.myPlayer, self.steven)
        else:
            Turn.turn_count(0)
            Utility.buff_check(self.steven, self.myPlayer)
        


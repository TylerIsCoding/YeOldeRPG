##### Imports #####
from Player import *
from Enemy import *
from Utility import *
import shelve
###################

class Main:

    def save_game(self):

        shelfFile = shelve.open('save_game')
        shelfFile['playerData'] = self.myPlayer
        shelfFile['area'] = Main.area
        shelfFile.close()

    def load_game(self):

        shelfFile = shelve.open('save_game')
        Main.myPlayer = shelfFile['playerData']
        Main.area = shelfFile['area']
        shelfFile.close()
        area = Main.area

        Main.resume(self, area)

    def resume(self, area):

        if area == 'chapter_one_begin':
            Main.chapter_one_begin(self)
        elif area == 'doge_convo':
            Main.doge_convo(self)
        elif area == 'cross_roads':
            Main.cross_roads(self)
        elif area == 'stables':
            Main.stables(self)
        elif area == 'Nick':
            Main.nick_fight(self)
        elif area == 'postNick':
            Main.post_nick_fight(self)
        elif area == 'woods':
            Main.woods(self)
        elif area == 'Steven':
            Main.steven_fight(self)
        elif area == 'postSteven':
            Main.post_steven_fight(self)
        elif area == 'lumber':
            Main.lumber_mill(self)
        elif area == 'Shturman':
            Main.shturman_fight(self)
        elif area == 'postShturman':
            Main.post_shturman_fight(self)
        elif area == 'kingsmen':
            Main.kingsmen(self)
        elif area == 'knight':
            Main.knight(self)
        else:
            Main.player_name()

    myPlayer = Player("name")
    nick = Nick()
    nick.max_hp = nick.hp
    steven = Steven()
    steven.max_hp = steven.hp
    shturman = Shturman()
    shturman.max_hp = shturman.hp
    attack = Attack()
    buff = Buff()
    restore = Recovery()
    area = ''

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
        TextSpeed.line("################################")
        TextSpeed.line("# Welcome to Ye Olde Text RPG! #")
        TextSpeed.line("################################")
        TextSpeed.line("         --(P)lay--")
        TextSpeed.line("         --(L)oad--")
        TextSpeed.line("        --(O)ptions--")
        TextSpeed.line("         --(Q)uit--")
        print('\n' * 5)
        main_menu_selection = input("\n>>> ")
        if "p" in main_menu_selection.lower():
            self.player_name()
        elif "l" in main_menu_selection.lower():
            self.load_game()
        elif "o" in main_menu_selection.lower():
            self.options()
        elif "q" in main_menu_selection.lower():
            quit()
        else:
            TextSpeed.line("\nYou must select Play or Quit.\n")
            Utility.continue_prompt
            self.main_menu()
    
    def options(self):
        
        Utility.clear()
        TextSpeed.line("############################")
        TextSpeed.line("#         Options          #")
        TextSpeed.line("############################")
        TextSpeed.line("    1.) Story Text Speed")
        TextSpeed.line("      2.) Combat Speed")
        TextSpeed.line("          (R)eturn")
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
        TextSpeed.line("############################")
        TextSpeed.line("#     Story Text Speed     #")
        TextSpeed.line("############################")
        TextSpeed.line("        1.) Normal")
        TextSpeed.line("        2.) Fast")
        TextSpeed.line("        3.) Instant")
        TextSpeed.line("         (R)eturn")
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
        TextSpeed.line("############################")
        TextSpeed.line("#       Combat Speed       #")
        TextSpeed.line("############################")
        TextSpeed.line("        1.) Normal")
        TextSpeed.line("        2.) Fast Scroll")
        TextSpeed.line("        3.) Instant")
        TextSpeed.line("         (R)eturn")
        answer = input('\n\n>>> ')
        if str(1) in answer:
            Utility.combat = TextSpeed.line
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
        Buffs = [Rage, Anger, Barrier, Shadows, Pain]
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
        elif answer == str(answer):
            Utility.story('\nPlease enter a valid selection. Try again.')
            Utility.continue_prompt()
            self.skillselection()
        count = 1
        ListStore = []
        for skill in SkillList:
            if skill.role == self.myPlayer.role:
                ListStore.append(skill)
                Utility.story(f"\n{count}.) {skill.name} | Cost: {skill.skillcost}")
                count += 1
        Utility.story(f"\n{count}.) Return")
        Utility.story('\n\nPress (D) for skill descriptions.')
        Utility.story(f'\n\nYou have {self.myPlayer.skillpoints} points remaining.\n')
        selection = input('\n\n>>> ')
        if 'd' in selection.lower():
            for skill in ListStore:
                Utility.story(f'\n\n{skill.name}:{skill.skilldes}')
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
        elif 'd' in answer.lower():
            for skill in SkillList:
                Utility.story(f'\n\n{skill.name}:{skill.skilldes}')
            Utility.continue_prompt()
            self.skillselection()
        elif (int(selection) == count):
            self.skillselection()
        elif selection == str(selection):
            Utility.story('\nPlease enter a valid selection. Try again.')
            Utility.continue_prompt()
            self.skillselection()
        



    def confirmation(self):

        Utility.clear()
        self.myPlayer.max_hp = self.myPlayer.hp
        a = (f"+ {self.myPlayer.name} the {self.myPlayer.role} +")
        TextSpeed.line(f'{a:^46}')
        TextSpeed.line("##############################################")
        b = (f"| Hit Points: {self.myPlayer.hp}/{self.myPlayer.max_hp}")
        c = (f"| Mana Points: {self.myPlayer.mp}")
        d = (f"| Defense: {self.myPlayer.defense}")
        e = (f"| Attack Dice: {self.myPlayer.max_attack_str}")
        TextSpeed.line('|' + ' ' * 44 + '|')
        TextSpeed.line(f'{b:<44} |')
        TextSpeed.line(f'{c:<44} |')
        TextSpeed.line(f'{d:<44} |')
        TextSpeed.line(f'{e:<44} |')
        TextSpeed.line('|' + ' ' * 44 + '|')
        TextSpeed.line("##################| Skills |##################")
        TextSpeed.line('|' + ' ' * 44 + '|')
        for skill in self.myPlayer.skills:
            TextSpeed.line(f'| {skill.name:<42} |')
        TextSpeed.line('|' + ' ' * 44 + '|')
        TextSpeed.line("##############################################")
        TextSpeed.line("\n\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n\n>>> ")
        if "n" in answer_3:
            self.skillselection == False
        elif "y" in answer_3:
            Utility.clear()
            self.player_setup()
            self.skillselection == True
        else:
            TextSpeed.line("\n\nYou have to choose (Y)es or (N)o\n")
            self.confirmation()
    

    def chapter_one_begin(self):

        Utility.clear()
        Main.area = 'chapter_one_begin'
        Main.save_game(self)
        TextSpeed.line("                            #########################")
        TextSpeed.line("                            #      Chapter One      #")
        TextSpeed.line("                            #########################")
        Utility.story("\n\n\nAs night falls you enter a small tavern on the crossroads.")
        Utility.story("\n\nThere aren't many patrons in the tavern but the fireplace \nburns bright and the ale seems to be flowing.")
        Utility.continue_prompt()
        Utility.clear()
        TextSpeed.line("##################################################################################")
        TextSpeed.line("#                                                                                #")
        TextSpeed.line("#                                  ▄▄▄▄▄,                                        #")                     
        TextSpeed.line("#                      ▄█▀▀▀▀▀█▄██▀      ▀█,██▀▀▀█▄█▀▀▀██,                       #")                    
        TextSpeed.line("#                  ▄███                    `             ▀██,                    #")                    
        TextSpeed.line("#                 █▌                                        ▀█                   #")                 
        TextSpeed.line("#                ██  ▐█                                   ▐█▀                    #")                  
        TextSpeed.line("#               ██    ▀█▀                            ,,    ██                    #")                 
        TextSpeed.line("#              █▀                                  ,▄█  ▄,  ██                   #")                 
        TextSpeed.line("#              █▄   █████▀████▀▀██████r         ▄▄█▀  ,████▀▀                    #")               
        TextSpeed.line("#               █  █▌                 ▀██▄           █▌   █▌      ,▄█▄           #")        
        TextSpeed.line("#              ▐█ ██                     ██        ███▄▄█████████▀▀  ╙█          #")      
        TextSpeed.line("#               ███▀▀▀█████▄▄▄██████▀▀▀▀███▀▀█▌    ▀██ ,,  █          ╘█         #")      
        TextSpeed.line("#              ▄███            ,▄▄▄,         █     ▄█   ██ ██ ▄████    ▐█        #")     
        TextSpeed.line("#             ▐█ █▌           ▐█   ▀█        █   ▄█   ███▀,▄█▀    █▌    ▐█       #")     
        TextSpeed.line("#               ▀██▄           █▄,,▄█        ▀██▀   ,▄▄██▀▀█▌      █▄    █▌      #")    
        TextSpeed.line("#                █▌ ▀▀███▄▄▄▄▄▄▄▄▄▄▄,,,,,,,▄██▀▀▀▀▀▀▀      ▐█       █    ▐█      #")    
        TextSpeed.line("#                █                 ▀▀▀▀▀▀▀▀▀         ▐      █      █▌    j█      #")    
        TextSpeed.line("#                █▌     ▐U                ▐W         ▌      █▌      █▌   j█      #")     
        TextSpeed.line("#                █▌     ▐                  ▌         █       █      █▌   ▐█      #")    
        TextSpeed.line("#                █      █                  █         █      ▐█      █▌   █▌      #")    
        TextSpeed.line("#               ▐█      █                  █          ▌      █▄     █▌   ▐█      #")   
        TextSpeed.line("#               ██      █                  █          █       █    █▀    ▐█      #")   
        TextSpeed.line("#               █▌      ▌                  █          █       █,▄██      █       #")    
        TextSpeed.line("#               █       ▌                  ▐          ▐      ▄██      ,▄██       #")     
        TextSpeed.line("#              █▌      ▐                   ▐r            ,▄██▀ █▌  ▄█▀           #")       
        TextSpeed.line("#              ██      █                    ▌       ,▄██▀▀▀▄,  ▐█▀▀              #")          
        TextSpeed.line("#            ▄███▀█▄,,                       ,▄▄██▀▀▀     ▄ █r ██                #")           
        TextSpeed.line("#           ▐█ █▌    `▀▀▀▀▀▀▀▀▀▀█████████▀▀▀▀`            ███▄███▌               #")           
        TextSpeed.line("#            ▀██              ▄█▀▀▀█                    ,▄██▀    █               #")           
        TextSpeed.line("#              █▄             █,   █▌              ,▄██▀▀▌      ▐█               #")           
        TextSpeed.line("#              ████▄▄,         ▀▀▀▀`   ,,,▄▄▄▄███▀▀      █      █▌               #")          
        TextSpeed.line("#              █     `█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀`    ▐▌           █      █                #")          
        TextSpeed.line("#              █▌     █                     ▐             ▌   ▄█▀                #")           
        TextSpeed.line("#              ██     █                     ▐             █,█▀                   #")           
        TextSpeed.line("#                ▀█▄  █                     ▐  ,▄▄▄▄▄▄▄███▀▀                     #")          
        TextSpeed.line("#                  ▀▀██▄▄▄,       ,,▄▄▄▄▄▄▄██▀▀`                                 #")         
        TextSpeed.line("#                         ▀▀▀▀▀▀▀▀``                                             #")         
        TextSpeed.line("#                                                                                #")
        TextSpeed.line("##################################################################################")
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
            self.myPlayer.on_the_run = False
            Utility.story("\n\nYou've heard that there's gold and fame to be gained in this region. \nMany travelers have come to this area seeking it, but few have survived.")
            Utility.story("\n\nAs you daydream of a better life filled with treasure and women, \nyou see a small creature hop into the empty seat across the table from you.")
            self.doge_convo()
        elif "e" in answer_2.lower():
            self.myPlayer.on_the_run = True
            Utility.story("\n\nThe royal guard seems to be getting closer and closer to catching you. \nYou hear murmurs of Kingsman being spotted nearby in the last few days.")
            Utility.story("\n\nAs you anxiously sip the ale that was just set in front of you,\na small creature hops into the empty chair at the table.")
            self.doge_convo()
        else:
            Utility.story('You must choose one of the two options.')
            self.fame_or_escape()
        
    
    def doge_convo(self):

        Utility.continue_prompt()
        Main.area = 'doge_convo'
        Main.save_game(self)
        Utility.clear()
        TextSpeed.line("##################################################################################")
        TextSpeed.line("#                                                               ▄▀▀▀█            #")
        TextSpeed.line("#                                                           ,▄▀    █▌            #")
        TextSpeed.line("#                                                           ▄█      j█           #")
        TextSpeed.line("#                   ,▄▄                                    █▀ ▄      █           #")
        TextSpeed.line("#                   ▐▌ ▀█▄                               ▄█  █▀      █           #")
        TextSpeed.line("#                    █    ▀▄                           ,█▀  ▄▀       █           #")
        TextSpeed.line("#                    ▐▌     ▀█▄                     ▄▄█▀   ▄█  ▄▄███  █          #")
        TextSpeed.line("#                    ▐▌       ▀█▄           ,▄▄&▀▀▀▀`     █▌  █████▌  ▐▌         #")
        TextSpeed.line("#                    █       ▀▀▀▀▀▀▄▄  ▄▄▀▀▀▀        ▄ ,██▀   ,█████  ▐▌         #")
        TextSpeed.line("#                    █▄█▀           `▀▀-             `▀██▌   ▄████▀   ▐▌         #")
        TextSpeed.line("#                  ▄█▀                                  --  ███▀      █▌         #")
        TextSpeed.line("#               ▄█▀-                   ▄▄                            ,█          #")
        TextSpeed.line("#            ,█▀-     ▀▀█▄          ,▄▀▀▀▀▄                          █           #")
        TextSpeed.line("#           ▄█           █▌       ▄█▀      ▀█▄,                      █⌐          #")
        TextSpeed.line("#          ▐▌            ▀Γ                   ▀█▄                     █          #")
        TextSpeed.line("#          █▌    ▄███▀█▄               ▄██▀█▄▄  ▐█                    `█         #")
        TextSpeed.line("#          █   ▄█████▌ █▌            ▄███▄▄████▄                       `█,       #")
        TextSpeed.line("#         ▄█   █,▐██████        █ ▀██`▐█████████C                        █▄      #")
        TextSpeed.line("#        ╒█     ▀██████         ▐▌  ▀▀████████▀                      ▀█   █▌     #")
        TextSpeed.line("#        █          ▄█           ▀▌      ---                          ▐█   █⌐    #")
        TextSpeed.line("#       █▌        ▄▀              ▀        ▄▄██▌                     ▐▌    └█    #")
        TextSpeed.line("#      ▐█      ,█▀                    '▀▀▀▀▀`                       ██      ▐▌   #")
        TextSpeed.line("#      █     ▄█▀                                                 ,▄▄▀        █   #")
        TextSpeed.line("#     █▀   ▄█▀▄▄▄,▀█▄                                                        █   #")
        TextSpeed.line("#     █   ▐██████████`                                                       █   #")
        TextSpeed.line("#     █⌐  ▐▌███████▀  ▄ ,                                                   ▐█   #")
        TextSpeed.line("#      █ ╒█  ▀███▀  ▀  '─4                                                  ▐▌   #")
        TextSpeed.line("#      ▐█▐█ ∞,▀█▄     ` ª        ,▄█▀▀                                      ▐▌   #")
        TextSpeed.line("#     ▄█▀█ ▀█▄▄████▄          ▄▄▀▀                                       ,   █   #")
        TextSpeed.line("#   ,█▀  █  █████████████████▀                                      ,▄▐█▀▀   █-  #")
        TextSpeed.line("#   █-   █▌  ╙█ ▀▀▀          ,▄▄▄▄▄▄                             ▄█▄█▀       █▌  #")
        TextSpeed.line("#   █▄    ▀▄   ▀█▄  ,▄▄▄▄▄█▀▀▀                  ,█▀             ▀▀           ▐█  #")
        TextSpeed.line("#   ▄█      █▄   `▀▀`                         ,▄█                            █▀  #")
        TextSpeed.line("# ╒█▀        '▀█▄                          ,▄█▀                             ▄█,  #")
        TextSpeed.line("#▄█              ▀▀█▄                ▄▄▄▀▀▀▀                                  █▄ #")
        TextSpeed.line("#▀                  -▀▀▀▄▄▄▄▄,,,▄▄█▀▀                                          █▌#")
        TextSpeed.line("#                           --▀▀                                               ▐█#")
        TextSpeed.line("##################################################################################")
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

        Main.area = 'cross_roads'
        Main.save_game(self)
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
        Main.area = 'stables'
        Main.save_game(self)
        Utility.clear()                                                                                            
        TextSpeed.line('##################################################################################')
        TextSpeed.line('#               ~      ,,                                                        #')               
        TextSpeed.line('#              ▓       ╙▄>),                                                     #')               
        TextSpeed.line('#             ╒M]▀      ▓Ü┐"φ                                                    #')               
        TextSpeed.line('#             ▐ ▐ ▀,    ]╢ % ╬     .⌐=╖, ,,                                      #')               
        TextSpeed.line('#             ▐     █▄∞0$▓▌  ]]*▄,`"*      ╙▀╙╝  "W.                             #')               
        TextSpeed.line('#              ▌ ,▄▀`√"   ▓█╓] $   ▀▌```````""ⁿM∞╖╓` ╚╜[ ═,                      #')               
        TextSpeed.line('#              ╙█▀ / `     ∩╙█▌▐     L               `*w,  ▀Xw,                  #')               
        TextSpeed.line('#              ▓  `,`     NΓ  " .. ⌐                      "ª▄▌ ▀╚D═,             #')               
        TextSpeed.line('#             ▓* ▓╒`      Ü▌                                  ▀▄ ║  █            #')               
        TextSpeed.line('#             ▌,╣ ▌            Γ       ╘           ~            ╙N  ╟▌▄,         #')               
        TextSpeed.line('#            ╒▄ `█ ¿ ▐ ╒,▓              b             "~           ▀,╙ ▌▐▄,      #')               
        TextSpeed.line('#            ▓ j▐▒   ▐ ╢╢               ▐                 \.         ▀,▀  Ü█,    #')               
        TextSpeed.line('#           Æ  ]▌║   █ ▌        \        ▌                   \\        ▀,  ▓"▄   #')               
        TextSpeed.line('#         ▄▀   ▐ ▐ ┐ ▐ C        ▐  ░     ╘                     "┐        N   █,  #')               
        TextSpeed.line('#          █   ]  U" ² ░ ,     `  /┘      ▌                            `  ╙ ²▐▐▄ #')               
        TextSpeed.line('#          ╘µ     ▓L\╘` ╩█   ]   ,]       ▐                              \ ╚  ┘▐ #')               
        TextSpeed.line('#          ▌      ▓ \k  ▀▓m═`             C                                ╚  ║▀ #')            
        TextSpeed.line('#           ▌      `▌ ╙╕       ¿           ▌                             ╙   ╙,  #')           
        TextSpeed.line('#          ▐                  ^            ▌                                   N #')         
        TextSpeed.line('#          ▓                  U^           ▌ ]           `.                 «    #')         
        TextSpeed.line('#          ▌                 ▓ ~,         ▐ j               ~                    #')       
        TextSpeed.line('#         ]                               ▌ ╝r                                   #')      
        TextSpeed.line('#         ▐ j                            ▓                                       #')     
        TextSpeed.line('#         ▌ `       ┌    `         ╙╦  ▄▀                                        #')     
        TextSpeed.line('#               ┌   Γ  ╒         ┌  ▐▀    ^      ,                               #')      
        TextSpeed.line('#        ▐      `                  ╔`                                            #')          
        TextSpeed.line('#        ▓                   ─^   Æ         ▐     ]                              #')         
        TextSpeed.line('#        ▌                    ¡ ¿`           r                         ┘         #')         
        TextSpeed.line('#       ▐                ,,   ,┘             ▌     ├                             #')         
        TextSpeed.line('#       ▌      ▄██▄  L . ▄▐▌¿`               ▐                         ┌         #')               
        TextSpeed.line('#      ▐       █████   ,█  █                 ]      L                  v         #')              
        TextSpeed.line('#       ▀▄     ▌ ]█▀╛P,▀ ╓ ▓                  ▌     ╢                 ,[         #')       
        TextSpeed.line('#         ╙N▄, ▀▀▀    █ ╒╜"                   ▓     ▐                 ^          #')           
        TextSpeed.line('#              ▀N▄▄mÆ▌═²`                     ▐                                  #')            
        TextSpeed.line('#                                              ▌                              ¿" #')               
        TextSpeed.line('#                                              ▀     L                      ¿    #')               
        TextSpeed.line('#                                               L    |             -`,^          #')               
        TextSpeed.line("##################################################################################")                                                                                                                                                                                
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
        Main.area = "Nick"
        Main.save_game(self)
        Utility.clear()
        TextSpeed.line("#################################################################################################")
        TextSpeed.line("#                                                                                               #")
        TextSpeed.line("#                                  ▄▄▄▄▀▀▀▀▀▀▀▀▀▀█▄▄▄╓                                          #")
        TextSpeed.line("#                              ╔▄▀▀▀  ▄     ╨       -▀▀▀█▄▄                                     #")
        TextSpeed.line("#                            ▄█▀▄             Æ   ▀     ç ▀█▄                                   #")
        TextSpeed.line("#                          ▄█╚       ╚`                     ▀▄                                  #")
        TextSpeed.line("#                        ▄▀╚                 ▀   '        ╘¬ ▀█▄                                #")
        TextSpeed.line("#                      ╒█╚    ▀  ╙                       ▀     ▀█                               #")
        TextSpeed.line("#                      █`              ▀                        ▐█                              #")
        TextSpeed.line("#                     █▀  ▀      ▀                               ▐█                             #")
        TextSpeed.line("#                    ▄▌     ▀                                    ▐▌                             #")
        TextSpeed.line("#                   ╔█ 7ⁿ                               ▄        █-                             #")
        TextSpeed.line("#                   █C      Æ                  ▀▄.     ┌▌     ▄▀ █                              #")
        TextSpeed.line("#                  ▐▌                            ▀&ç   █   ╓█▀-  ▐▌                             #") 
        TextSpeed.line("#                   █   P            ╔▄▄▄▄▄╓      ╓╨▀    ,█▀,▄▄▄▄▄█▄              ▄█▀       ▄µ  #")
        TextSpeed.line("#                   █▌      :        ▀═   ╛▀▀▀█▄▄¿╔▀▄   ▐█-█▀═████▀█▄          ;▄▀═       ▄█▀   #")
        TextSpeed.line("#                ;▄▄█▌      -           ▄▄▄▄▄▄▄▄▄▄▀╝▌    ▀▄`██▀▀▀╔  █         ▄▀      ,▄█▀╙     #")
        TextSpeed.line("#              ▄▀▀▄▄,▀▀▄⌐            ╒█▀▐█▄▄██µ ▄█▌       ▐▌ '▀▀▀   █        █▌     ╔█▀         #")
        TextSpeed.line("#            ▄█═▄▀, ▀▀▄              ╘▀▄▄██████▀╝ ▌        █▄      ▄▀█▄      ╘█µ     ▀▄         #")
        TextSpeed.line("#            █▄▐-    ▄▌                 ╙▀▀╝╙   ▄▀        ╓▄█    ,▄▌ ▐▌        ▀▄.    ▀█▄       #")
        TextSpeed.line("#             ██   ▄▀ ▀▄                             ,▄█▀▀▀╚▀▀▀▀▀▀╚  ▐▌          ▀▄     ▀█⌐     #")
        TextSpeed.line("#             ███▄▄⌠▀M▄▀                 ç▄▄▄▄▄▄▄███▀▀¬      ,  ▄▄▄  █L           ▐█.     █     #")
        TextSpeed.line("#             ▐█  ▀▀▀▀██▄▄▄▄▄ççç▄▄▄▄▄▀▀▀▀╚╙-                 ▐█ ¬╙╛ `█           ▄▄▀-  ╓▄▀▀     #")
        TextSpeed.line("#              ▀█          ¬╙╙╙╙╚╘            ▄▄▄▀██          █ ▐▄   █⌐      ,▄█▀▀  ▄▄▀▀        #")
        TextSpeed.line("#              ▄█▀▄,                   ,▄▄▄█▀▀╩ ▄█▀    ¬▄▄▄▄▄▀▀  ▀   ▐▌     █▀- ▄▄▀▀¬           #")
        TextSpeed.line("#              █` `▀▌                  ▀╛       ╚  ╓▄▀    '`          █    ▐█▄ █▌               #")
        TextSpeed.line("#              ▀█                                ▄█▀                 █▀      ▀█∞▀               #")
        TextSpeed.line("#               ╙█ ▀█▄▄,                       ▄█▀            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                  #")
        TextSpeed.line("#          ▄▄▀÷  ▐▌   ╚▀▀▀█▄▄,                ▀╛             █   █▄          ███                #")
        TextSpeed.line("#      ╔▄█▀▀      ▀█▌       ╛▀▀▀▀                             ▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀╚                 #")
        TextSpeed.line("#   ╔▄▀▀           ▐█▌                                             -█  ╙▀▀▀▄▄▄▄                 #")
        TextSpeed.line("# ▄█▀                █▄              '▀▄▄▄                      ▄█ⁿ▐▌         ╙▀▀█µ             #")
        TextSpeed.line("# █                   ▀█▄                ╙▀▀▀█▄▄▄µ             ▀▌  █▌             █⌐            #")
        TextSpeed.line("#                       ▀▀█▄▄                   ▄█                ▐▌              ▐█            #")
        TextSpeed.line("#                           ╘▀█▄              4▀▀                 █r               █▌           #")
        TextSpeed.line("#                              ▀██▄▄                 ╓▄▄µ        █5                ▐▌           #")
        TextSpeed.line("#                                 └▀▀███▄▄µ    ,▄▄█▀▀▀╛└▀▀▀▀█▄▄▄▐▌                  ▀           #")
        TextSpeed.line("#                                      '  ▀▀▀▀▀▀╘              ╨▀                               #")
        TextSpeed.line("#################################################################################################")
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
        Main.area = "postNick"
        Main.save_game(self)
        Utility.clear()
        Utility.story('\n\n"Wow!" says Meelon. "It looks like you can fight... \nLook, he dropped this after you got him."')
        get_loot = input('\n\n>>> Hit enter to loot the scav.')
        if '' in get_loot:
            Utility.clear()
            TextSpeed.line('###########################################################################################################################')
            TextSpeed.line("#                                                           ▄▄,,,                                                         #")  
            TextSpeed.line("#                        █444444▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██╢╢▓╢██▄,,,,,,,,,,                                 ▄▄███▄     #") 
            TextSpeed.line("#                       █▀     ██╢██╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╢███╢▓▓▓▓█▓▓█▓▓▓▓▓▓▓▓▓████████████████████████████████████████▄   #")
            TextSpeed.line("#                     ▄█▀     ▐█╬██████████████████████████████████████████████████████████████████████████████████████   #") 
            TextSpeed.line("#                   ▄█▀       █╢▓█▌                      ,,,▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄█████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     #") 
            TextSpeed.line("#            ,▄▄▄█▀▀         █╣▓▓█                ▄▀             ,,,,▄▄▄▄▄▄▄▄▄▄Æ▀        ,^▄█                             #")
            TextSpeed.line("#         ▐▀▀ ▌     ╚       ▐█╢╢█▌                 `▀▀▀▀▀`                    ,,,,...⌐∞'▄▄█▀                              #") 
            TextSpeed.line("#         █   '     ▌       ▐█▓██           ,,,,..⌐¬∞∞═══^^''''``    ,,▄▄▄▄▄▄▄▄▄▄▄4▀▀▀▀▀                                  #") 
            TextSpeed.line("#         █,,...⌐⌐¬════^^''''7▀▀`              ,,,▄▄▄▄▄▄▄▄&4▀▀▀▀▀▀▀▀▀▀ `                                                  #") 
            TextSpeed.line("#         █            ,,,▄▄▄▄▄▄▄▄▄████████████▓▀                                                                         #") 
            TextSpeed.line("#        ▐█4▀▀▀▀▀▀▀▀▀▀█▀██▀   ▐█ ╢█▓▓▓▓▓▓▓█▓▓███                                                                          #")
            TextSpeed.line("#        ▐▌           █ ▀█  ,▄█╢ █╢▓▓▓▓▓▓╫█▓▓█╣▌                                                                          #")
            TextSpeed.line("#        ▐▌      ,,, ▐█████████ ▓██▓▓▓▓▓▓█╢▓███                                                                           #")
            TextSpeed.line("#       ,█     ,██▀-'   ▀▀   █ ▓▓▓██████╢▓▓▓█╣▌                                                                           #")
            TextSpeed.line("#      ▄▀     ▄██            █▓▓▓▓▓▓▓▓▓▓▓▓▓▓█╣█                                                                           #")
            TextSpeed.line("#    ╒█      ██▀            ██╢╢╢████████████▀                                                                            #")
            TextSpeed.line("#    █       ██▌                                                                                                          #")
            TextSpeed.line("#   █-       ▐██                                                                                                          #")  
            TextSpeed.line("#  ▐█,      ,▄██                                                                                                          #") 
            TextSpeed.line("#    `▀444████▀                                                                                                           #")
            TextSpeed.line('###########################################################################################################################')  
            Utility.story('\n\nThe doge bends down and picks up a weapon off of the ground.')
            Utility.story('\nIt appears to be a TOZ-106! You pick it up. It adds (+1) to your damage roll.')
            self.myPlayer.additional_damage += 1
            self.myPlayer.max_attack_str = (f'{self.myPlayer.max_attack_str} + 1')
            Utility.story(f'\n\nYou now do {str(self.myPlayer.max_attack_str)} points of damage.')
            Utility.continue_prompt()
            self.woods()


    def woods(self):

        Main.area = "woods"
        Main.save_game(self)
        Utility.clear()
        TextSpeed.line('#####################################################################################')                                                                                
        TextSpeed.line('#                                       ▐▄                                          #')
        TextSpeed.line('#                                      ▄▀█                                          #')
        TextSpeed.line('#                                     █▄▀        █▄                                 #')
        TextSpeed.line('#                                      ▀          █▀▄                               #')
        TextSpeed.line('#                                                  ▌ █                              #')
        TextSpeed.line('#                                       ▄▄▌        ▌  ▀█,                           #')
        TextSpeed.line('#                                    ▄▀▀▐▀       ,█     ▀▄                          #')
        TextSpeed.line('#                                  ▄▀  ▄▀      ▄▀¬       ▐▄                         #')
        TextSpeed.line('#                                 █     ▀▀▄▄▄▀▀           ▌                         #')
        TextSpeed.line('#                                ¬▌                      █                          #')
        TextSpeed.line('#                                 █                    ▄▀                           #')
        TextSpeed.line('#                                 █             ,      █                            #')
        TextSpeed.line('#                                █▀      ▄    ▄▀▀       █                           #')
        TextSpeed.line('#                            ,▄▀▀     ,Æ█    ▄ ▐         █                          #')
        TextSpeed.line('#                           █▀      ,▀   ▀∞∞▀   ▀▄       ▐▌                         #')
        TextSpeed.line('#                           ▌       ▌             ▀▄      █                         #')
        TextSpeed.line('#                          ,▌       ▌               ▄     ▐▌                        #')
        TextSpeed.line('#                         █▀      ▄,▄              ▄▀     ▐▌                        #')
        TextSpeed.line('#                          ▀▄      N             ▄▀      ▄▀      ▄██▄               #')
        TextSpeed.line('#                             ▀▀▄    ▀▄        ,▀     ,█▀     ▄▄███ ▀█              #')
        TextSpeed.line('#                          ,,,▄▄▄████▄ ▀     ,▀    ▄█▀▄▄▄███▀▀▀¢██   █▌             #')
        TextSpeed.line('#          ██▀██████████▀▀█▀▀▀▀ÅΣΣÅ▒▒Å▀████████████▀▀▀▀▀╟▒▒▒▒▒▒▄█ █ ▐█              #')
        TextSpeed.line('#        ▄█▀▀█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄█▀▀%▒▒▒▒▒██▒▒▒█Ñ▒▒▒▒▒▒▒▒▒▒▒⌠▀▀▀████  ▌ ▀█              #')
        TextSpeed.line('#      ,█▀ █▄▀██▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▄██▀▀██¢▒▒▒▐█▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒█▌ █ ╓▄▀█▄            #')
        TextSpeed.line('#     ╒█  ▄⌐██ ▀█▌▒▒▒▄▄██▀▀▒▒▒▒▒░▒▄███▀▒▒▒▒▒████████▀▀▀██▄▄▒▒▒██ ▀▄ █  █            #')
        TextSpeed.line('#     █ ▄█▀ ██ ▄██▀▀▀≡▒▒▒▒▒██▌▒▄██▀██▒▒█▒▒▒█▒█▌    ▀▀█▀▀████▀▀▀██  █ ▄█`            #')
        TextSpeed.line('#     ▀▌ ▄█▀ ▄█▀▒▒▒▄█▀▀▒▒▄▀▒▄█▀▀  ██▒▄█▒▒▒▒█▒██           -▀▀████ ,█▀▀              #')
        TextSpeed.line('#      ▀█  ▄█▀▒█▀▀▄▄████▀████    █▀▒█▀▒▒▒▄▌▀▒▒█                ▀▀▀▀                 #')
        TextSpeed.line('#       ╙███▄███▀▀▀¬      -    ▄█▀▒████▀██▌▒▒▒█                                     #')
        TextSpeed.line('#          -                  ██▀▀▀▀▄▄▄   ▀██▐█                                     #')
        TextSpeed.line('#                            █▀ ▄▄▄▀▀  ▀▀0▄ ▀██                                     #')
        TextSpeed.line('#                           █▌█▀    █▀  ,  ▀▌ █▌                                    #')
        TextSpeed.line('#                          █▀ ▌  █▀▀██▀▄█▀  ███                                     #')
        TextSpeed.line('#                          ╙▀█▀  █⌐ ▀▀█▀ ▀████                                      #')
        TextSpeed.line('#                             ▀█▄  ,▄███▀▀-                                         #')
        TextSpeed.line('#                               ▀▀▀▀                                                #')
        TextSpeed.line('#####################################################################################')
        regen = HealMajor.dice()
        Utility.story(f'\n\nYou both settle in for some rest. You regain {(str(regen))} hit points from sleeping.')
        self.myPlayer.hp += regen
        if self.myPlayer.hp > self.myPlayer.max_hp:
            self.myPlayer.hp = self.myPlayer.max_hp
        Utility.story('\nDaylight creeps over the hills and treetops. The two of you gather your gear and start towards the Woods.')
        Utility.story('\nAs you walk Meelon continues explaining about Shturman.')
        Utility.story('\n\n"Shturman is said to be in possession of the mighty Kappa container...\nIt has the ability to hold a vast amount of items in a very small space."')
        Utility.continue_prompt()
        Utility.clear()
        TextSpeed.line('#######################################################################################################')
        TextSpeed.line('#                                                   ,▄▄▄▄▄▄▄▄▄▄▄▄▄                                    #')
        TextSpeed.line('#                                                  ▄▀    ,   ,, , ▀▀█▄▄,                              #')
        TextSpeed.line('#                                                ▄█   ▄█▀▀▀▀▀▀▀▀▀▀▀█▄▄ ▀▀▀▄▄,                         #')
        TextSpeed.line('#                                           ,▄▄▀▀-,▄█▀-  ▐██████████▄▄▀▀█▄▄, ▀▀█▄▄                    #')
        TextSpeed.line('#                                      ,▄▄▀▀` ▄▄█▀▀        ▀▀██╢▓▓▓▓╢╢███▄▄▀▀▀▄▄▄ ▀▀█▄▄               #')
        TextSpeed.line('#                                 ,▄▄█▀▀ ▄▄█▀▀-                ▀▀███╢▓▓▓▓▓╢████▄▄▀▀█▄▄ ▀▀█▄▄          #')
        TextSpeed.line('#                             ▄▄█▀▀,▄▄█▀▀                           ▀▀██▓╢▓▓▓▓▓╢▓███▄ ▀▀    █         #')
        TextSpeed.line('#                  ▄▄&&▄▄▄▄█▀▀ ,▄█▀▀`                                    ▀▀████▀▀▀▀▄▄▄█▀▀    █        #')
        TextSpeed.line('#               ,▄▀▀      ,▄▄▀▀-                                             `,▄ ▀▀          ▐▌       #')
        TextSpeed.line('#            ,▄█▀  ,▄▄▄▀▀▀¬                                                ▄█▀▀   ▄▄▄▄▄▄,     █       #')
        TextSpeed.line('#           █▀▄▄█▀▀▀▄▄▄▄███▄▄                                          ▄▄▀▀       ▀█   -▄▄▄   ▐█      #')
        TextSpeed.line('#          █▀ █-████╢╢╢▓▓▓▓╢▓██▄,                                  ▄▄▀▀-           ▀⌐ ▄█▀ █▄  ▐█      #')
        TextSpeed.line('#         █▀ ▐█   ▀██╢▓▓▓▓▓▓▓▓▓╢▓██▄,                          ▄▄█▀                 ▄█ ▄▀▀▄█⌐ ██      #')
        TextSpeed.line('#        █▀   ▀▀▄,   ▀██╢▓▓▓▓▓▓▓▓▓▓╢▓██▄,                  ,▄█▀-                     █╘▌  ▀▄█¬██      #')
        TextSpeed.line('#       █▀       ▀█▄    ▀██╣▓▓▓▓▓▓▓▓▓▓▓╢███▄,          ,▄█▀`                     ▐█▄ ▀█▐   ▀▄█▌█⌐     #')
        TextSpeed.line('#      █▀           ▀█▄    ▀▀██╢▓▓▓▓▓▓▓▓▓▓╢███     ,▄█▀▀                     ▄▄▄▄▐███,█▌█ ,▄▀█ █▌     #')
        TextSpeed.line('#      ██▄,           `▀█▄     ▀██╢▓▓▓▓╢█▀▀     ╒█▀▀    ,██▄             ,▄▄▄▀██▀ █`   █⌐    █ ▐▌     #')
        TextSpeed.line('#       █ ▀█▄             ▀█▄     ▀██╢╢█▀    ▄        ,█▀  `▀▄         ▄  ██▀  █▄   ,▄▀▀▄█   █ █▀     #')
        TextSpeed.line('#       ▐█  `▀█▄             ▀▄▄     ▀▀    ,█▀       ▄▀      ,,     ▄⌐ █▀█,▀▄     ▄█▀ j█ `█  ██       #')
        TextSpeed.line('#        ▀█    ▀█▄             ▀█▄,       ▄█       ▄▀    ▄▄▀▀ ▀█ ▐▄▄█  ██`▀    ,▄▀`  ,▄█ ▄██▄█        #')
        TextSpeed.line('#         ▀▌      ▀█▄             ▀█▄    █▀       ▀-,▄▄▀▀,▄█▀█▄▐█ ▀█▀▀▀▀"    ▄█▀   ▄█▀,▄▀` ██         #')
        TextSpeed.line('#          █⌐        ▀▄,             ▀█▄█         ▄█▀,▄█▀▀    █▄▐█ ▀`     ▄█▀   ,▄▀`▄█▀   ▄█▀         #')
        TextSpeed.line('#          `█▄,        ▀█▄             ▄           █ █▄        █▄ █    ,▄▀▀   ▄█▀ ▄▀▀   ▄█▀           #')
        TextSpeed.line('#            █▀█▄         ▀█▄         ▐▌           `█ █▄        ▀█ █,▄█▀,, ▄█▀ ▄█▀   ,▄▀              #')
        TextSpeed.line('#            ▐█  ▀█▄        ▀█▄       ▐              █ ▀▄    ▄▄█ █ ▐█▄▄▀▀-▀ ,▄▀`   ▄█▀                #')
        TextSpeed.line('#             `▀▄,  ▀▄▄        ▀█▄    █              ▐█ ▀█ ▀▀`   █-█▌█▀▀▀█&█▀    ▄█▀                  #')
        TextSpeed.line('#                ▀█▄  ▀█▄         ▀▄  ▀         ,,▄▄▄▄██ █       █-█ █        ,▄▀-                    #')
        TextSpeed.line('#                   ▀█,  ▀█▄        ▀█▄&█▀▀▀▀▀▀▀  `   ▐▌ █       █ █ █▄▄▄▄▄▄▄█▀                       #')
        TextSpeed.line('#                     ▀█▄   ▀█▄     j█                ▐▌j█     ,▄█¬█ ▄█▀▀ ``                          #')
        TextSpeed.line('#                        ▀█,  ▀▀▄   ▐█                ▐▌▐▌ ,▄█▀▀▄▄▀▀▀                                 #')
        TextSpeed.line('#                          ▀█▄   ▀█▄▐█       ,▄▄▄▄▄█▀▀█▌▀█▀▀▄▄▀▀                                      #')
        TextSpeed.line('#                            -▀█▄  `▀██▀▀▀▀▀▀ -       ▐▌▄▄▀▀                                          #')
        TextSpeed.line('#                               ▀█▄            ,▄▄▄▄▄&▀▀-                                             #')
        TextSpeed.line('#                                  ▀█▄▄▄▄&▀▀▀▀▀`                                                      #')
        TextSpeed.line('#######################################################################################################')
        if self.myPlayer.on_the_run == True:
            Utility.story('\n\n"If we could aquire the Kappa container AND remove Shturman\'s evil hold \non the Woods, I\'m sure that the King would be most grateful."')
        else:
            Utility.story('\n\n"I know that you\'ve been seeking wealth in our fair land... The Kappa container is said to be worth a fortune."')
        Utility.story(f'\n\n"Listen, {self.myPlayer.name}, we should head East. \nThat\'s where Shturman was last spotted... or so I\'ve heard..."')
        Utility.story('\n\n\nThe two of you head East to see if you can find any traces of Shturman. \nAs you try to locate any clues you hear the sound of twigs snapping\nand the unmistakable smell of sweat!')
        Utility.story('\n\nA wild Sweaty Steven appears!')
        Utility.continue_prompt()
        self.steven_fight()


    def steven_fight(self):

        Main.area = "Steven"
        Main.save_game(self)
        Utility.clear()
        TextSpeed.line('######################################################################################')
        TextSpeed.line('#                          ▄▄▄█                         ▀▄▄▄▄▄╓                      #')
        TextSpeed.line('#                     ╒▄█▀▀▀                             "▀█ ╙▀▀▀▀█▄╓                #')
        TextSpeed.line('#                 ╔▄█▀▀-                                   ▀█      `▀█▄              #')
        TextSpeed.line('#               ▄█▀  ,                                      ▀█        -▀█ç           #')
        TextSpeed.line('#             ▄█T ,█▀▀▀▀▀█▀                                  ╙█▄         ▀█▄         #')
        TextSpeed.line('#            ▄▀  ▄█-  ▄▄█7                              ,▄▄▄█▀▀█           ▀█        #')
        TextSpeed.line('#           ▐█  ▄█  ▄▀█▀                            ▄█▀▀▀╙ ▄▄▀▀▀       ▄▄▄▄,▐█       #')
        TextSpeed.line('#          J█  ▐█ ╥▀ █▌                            █▀  ▄▄▀▀╓▄▄▄▄▄█▀▀▀▀▀⌠  "▀██▌      #')
        TextSpeed.line('#          █▌  █▌ █   ╚█C                          ▐█▀▀  ▄█▀╛╘ ▄¬H    ▌▐Ç    ▐▌      #')
        TextSpeed.line('#          █▌  ▐▌ █    █        FAST MT            ▐█  ▄█▀ ,   █▐+, ▄▄▄█▄    ▐▌      #')
        TextSpeed.line('#         ▐█          ;▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄╓            █▌     ██▀▀▀▀▀▀█¿   ▀█   ▐▌      #')
        TextSpeed.line('#          █▌▄█▀▀█▀▀▀▀▀╙             ╛╙▀▀▀▀▀█▄▄▄     ▀P  ╓▄█▌██▌   ²█    ▐▌  ]█      #')
        TextSpeed.line('#           ▀█▄▄█▀         ▄▄█▀▀▀▀▀           █▌▀▀▀██▄▄█▀▀▄█        └█▄  ▄█   █      #')
        TextSpeed.line('#              █▀▄▄     ▄█▀▀▄▄▄▄▄▄¿ ▄≡▄       █    █▌    ╔█"          ╙▀▄     █      #')
        TextSpeed.line('#              █▄▄█▀   ▀▀▄█▀ ██  █ █ █▀      ▐▌   ▐█     █C   ▄▄▄██▄    ▀█   j█      #')
        TextSpeed.line('#              ██▌▐█    ▐█ç ▐████ █▀ ╙       █▌   █      █▄▄█▀▀    ▀█▄   ▐█µ ▐▌      #')
        TextSpeed.line('#              ▀██▀"     ▀█▀█▄▄█▀▀          ▄█▄▄▄▄█    ▄█▀▀          ▀█▄  ▐█ ╙       #')
        TextSpeed.line('#           ▄█▀██-       ▀▄▀N▄▄             █∞   \█   ▄█               █   █         #')
        TextSpeed.line('#          █▀▄▄ ▀█▄╓ ▄µ   -▀   `           ▐█▄▄▄▄▐▌  ,█       ▄▄       █  █▀         #')
        TextSpeed.line('#         █ █▀     ▀██▀█▄▄▄                 █▌╙╙▐█¬ ▄█╚         ▄     █▌ █▀          #')
        TextSpeed.line('#        █▀▄█      ▄█    `╙▀▀▀█▄▄▄        ;▄█▄▄▄██▀▀▀                ▄█▀▀▀           #')
        TextSpeed.line('#       █▀,▀     ;█▀             ╙▀▀▀▀▀▀▀▀▀▀╙╙                      █▀ █C            #')
        TextSpeed.line('#      ███▀▀▄▄  █▀                                           ▄▄   ▄▀7  ▐█            #')
        TextSpeed.line('#      █▌    █▌ ▀█µ                                       ╥▄█▀▄▄█▀╙     ▀█           #')
        TextSpeed.line('#      ▐█    ▐█   █▄                                   ▄█▀▀▀▀▀▀          █▌          #')
        TextSpeed.line('#       ▐█    ▀█   █▄                               ▄█▀╧                ▄▀ ▀▀▀█▌     #')
        TextSpeed.line('#        ▀▌    ▀█   █¿                           ▄█▀╝               ╔▄█▀▀     ▀▀▀▀▀▀ #')
        TextSpeed.line('#         ▀█    ▀█   █▄                     ;▄█▀▀═█▌          ;▄▄▄█▀▀▀               #')
        TextSpeed.line('#          ▀█    █▌   ▀▄                ,▄█▀▀  ▀▀▀ ▀▀█▄▄██▀▀▀▀╛                      #')
        TextSpeed.line('#           ▀█    █`   ▀█           ▄▄█▀▀╛                                           #')
        TextSpeed.line('#            ▐█⌐  ▐█    ▀█     ╓▄▄█▀╝                                                #')
        TextSpeed.line('#             └█▄▄ ╚█▄  ,██▄█▀▀▀`                                                    #')
        TextSpeed.line('#                ▀▀█▄███▀-                                                           #')
        TextSpeed.line('######################################################################################')
        result = Utility.initiative()
        if result:
            Turn.turn_count(-1)
            Utility.buff_check(self.myPlayer, self.steven)
        else:
            Turn.turn_count(0)
            Utility.buff_check(self.steven, self.myPlayer)
        self.post_steven_fight()


    def post_steven_fight(self):

        Utility.continue_prompt()
        Utility.clear()
        Main.area = 'postSteven'
        Main.save_game(self)
        Utility.story('\nAs your final shot lands you see the sweaty boy hit the ground with a gasp.')
        Utility.story('\n"That was close!" says Meelon. "He came out of nowhere! Come; we need to find Shturman\
        \nbefore we lose any more daylight... He should be at the Lumber Mill nearby."')
        Utility.story('\n\nBefore the two of you leave, you bend down and remove the sweaty helmet off of the body.')
        get_loot = input('\n\n>>> Hit enter to loot the PMC.')
        if '' in get_loot:
            Utility.clear()
            TextSpeed.line('##################################################################################')
            TextSpeed.line('#                                                                                #')
            TextSpeed.line('#                           ,▄▄▄▄▄▄ANK4MNN4▄▄▄▄▄▄,                               #')
            TextSpeed.line('#                    ,▄▄▀▀▀.                     `▀▀▀4▄▄                         #')
            TextSpeed.line('#                 ,▄▐▀ `                                ▀█,                      #')
            TextSpeed.line('#             █▀▀▀    ─,                                   ▀█▄                   #')
            TextSpeed.line('#        ,ÆP▄Å▀▀`   ▀  █▀                                     ▀█▄                #')
            TextSpeed.line('#      ▄▄▌▄▀ ▄═  ▄M^  ▄█                                        `█▄              #')
            TextSpeed.line('#      █▀▀  █         █,▌  ,                                      ▀█,            #')
            TextSpeed.line('#     ▐██  █     ,   ▐▌█  ▄▀                                        ▀▌           #')
            TextSpeed.line('#      ▀  ▐`   ,⌐▀   ▄⌐m                                 B ═╒r¬ ▄  ▄ "█          #')
            TextSpeed.line('#     ▐▌       ▀⌐                                 ▄r   ▄`     ^*═─═-~ ╘█         #')
            TextSpeed.line('#    ▐▌       `                                        █  ▐▌  █  █  █  ╙█        #')
            TextSpeed.line('#    ▐`  ▀                                      ▄█`▄   `   `            ▀█▄      #')
            TextSpeed.line('#    █                                           █▄█      ▀ ` ▀  ▀  ▀     █      #')
            TextSpeed.line('#    ▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄,,,            ` -      ▄▄▄▄▄▄▄▄.▄     ▐▄ █▄     #')
            TextSpeed.line('#        ▀ █▐▌              ▐▌╖    --` "▀▀▀NA∞▄▄,,,▄▄▀▀-          ╙▄      ▐▌     #')
            TextSpeed.line('#          ▐█▌               █ █                 `               } █  ▐    ▌     #')
            TextSpeed.line('#           █▌                █ ▌ ,     , ╜     r                ▐ ▐▌ ▐ `  █     #')
            TextSpeed.line('#           ██                ▐▄█⌐▐▄   ▀ ▄Γ    ▐                  ⌐ █  ▌   █     #')
            TextSpeed.line('#           ██                 █ █w█ ⌐═  █     ▌                  \ █  ▌▀  █     #')
            TextSpeed.line('#         ╙▌▄█                  █       ▐▀ *═w▐▄                   █▀  █   ▐▌    #')
            TextSpeed.line('#          █ █▌                 ▐▌ █    █ *∞▄▄ █                   ▀▐  ▐]  █     #')
            TextSpeed.line('#           ▀██                  ▀▄▀,   ▌ ▄▄,,▐▌                   ∞▐µ ▐   █     #')
            TextSpeed.line('#            ▐█                    ▀█▄ ▐▌+∞∞▄▄▀                  ▄▀▀█▌  ,▄█`     #')
            TextSpeed.line('#             █▌                    ,█ █    █                  ,█▀    ██▀`       #')
            TextSpeed.line('#             ██               ▄▄&▀▀-,▄`   ╓█,               ,▄█                 #')
            TextSpeed.line('#             ╘█µ          ,▄▄▀` ▄▄▀▀`,▄  █  `▀▀▀4▄▄▄▄▄Æ4m,▄▀,▌                  #')
            TextSpeed.line('#              ██     ,▄▄▀▀▄  ╒█▀     █  ]▀            ,▄▀ ,█▀                   #')
            TextSpeed.line('#              ▐█▌ ▄█▀"  ▄▄r███      █` , ▀,       ▄Æ▀▐⌐ ▄█▀                     #')
            TextSpeed.line('#               █▄▀` ,▄▀▀           █`▄▄▄ ▀▄N ,▄▄▀▀█ ▌ ▌█                        #')
            TextSpeed.line('#               ██▄▄▀▀             ▄▀-,▄▀    `  ▄▄m▀▄▀▀                          #')
            TextSpeed.line('#               ╘▄ ¬▄▄▄▄▄▄▄▄▄▄▄▄ ⁿ`   - ,▄,▄Æ▀▀`                                 #')
            TextSpeed.line('#                ▐▄             ▀ ▀▄   █▀                                        #')
            TextSpeed.line('#                  █▄ ▀M∞∞∞N∞  "  ▄`█P▀                                          #')
            TextSpeed.line('#                   ▀█▄▄    ▄▀  ▄▀                                               #')
            TextSpeed.line('#                     ▀▀██▀▀▀▀▀                                                  #') 
            TextSpeed.line('#                                                                                #')
            TextSpeed.line('##################################################################################')
        Utility.story('\n\nYou receive the Fast MT! It adds (+1) to your defense roll!')
        self.myPlayer.additional_defense += 1
        self.myPlayer.defense = (f'{self.myPlayer.defense} + 1')
        Utility.continue_prompt()
        Utility.clear()
        Utility.story('After you finish taking the helmet off of the PMC, you and Meelon start down the path\
        \ntowards the Lumber Mill. Nightfall approaches and you make camp.')
        Utility.continue_prompt()
        Utility.clear()
        TextSpeed.line('#####################################################################################')                                                                                
        TextSpeed.line('#                                       ▐▄                                          #')
        TextSpeed.line('#                                      ▄▀█                                          #')
        TextSpeed.line('#                                     █▄▀        █▄                                 #')
        TextSpeed.line('#                                      ▀          █▀▄                               #')
        TextSpeed.line('#                                                  ▌ █                              #')
        TextSpeed.line('#                                       ▄▄▌        ▌  ▀█,                           #')
        TextSpeed.line('#                                    ▄▀▀▐▀       ,█     ▀▄                          #')
        TextSpeed.line('#                                  ▄▀  ▄▀      ▄▀¬       ▐▄                         #')
        TextSpeed.line('#                                 █     ▀▀▄▄▄▀▀           ▌                         #')
        TextSpeed.line('#                                ¬▌                      █                          #')
        TextSpeed.line('#                                 █                    ▄▀                           #')
        TextSpeed.line('#                                 █             ,      █                            #')
        TextSpeed.line('#                                █▀      ▄    ▄▀▀       █                           #')
        TextSpeed.line('#                            ,▄▀▀     ,Æ█    ▄ ▐         █                          #')
        TextSpeed.line('#                           █▀      ,▀   ▀∞∞▀   ▀▄       ▐▌                         #')
        TextSpeed.line('#                           ▌       ▌             ▀▄      █                         #')
        TextSpeed.line('#                          ,▌       ▌               ▄     ▐▌                        #')
        TextSpeed.line('#                         █▀      ▄,▄              ▄▀     ▐▌                        #')
        TextSpeed.line('#                          ▀▄      N             ▄▀      ▄▀      ▄██▄               #')
        TextSpeed.line('#                             ▀▀▄    ▀▄        ,▀     ,█▀     ▄▄███ ▀█              #')
        TextSpeed.line('#                          ,,,▄▄▄████▄ ▀     ,▀    ▄█▀▄▄▄███▀▀▀¢██   █▌             #')
        TextSpeed.line('#          ██▀██████████▀▀█▀▀▀▀ÅΣΣÅ▒▒Å▀████████████▀▀▀▀▀╟▒▒▒▒▒▒▄█ █ ▐█              #')
        TextSpeed.line('#        ▄█▀▀█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄█▀▀%▒▒▒▒▒██▒▒▒█Ñ▒▒▒▒▒▒▒▒▒▒▒⌠▀▀▀████  ▌ ▀█              #')
        TextSpeed.line('#      ,█▀ █▄▀██▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▄██▀▀██¢▒▒▒▐█▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒█▌ █ ╓▄▀█▄            #')
        TextSpeed.line('#     ╒█  ▄⌐██ ▀█▌▒▒▒▄▄██▀▀▒▒▒▒▒░▒▄███▀▒▒▒▒▒████████▀▀▀██▄▄▒▒▒██ ▀▄ █  █            #')
        TextSpeed.line('#     █ ▄█▀ ██ ▄██▀▀▀≡▒▒▒▒▒██▌▒▄██▀██▒▒█▒▒▒█▒█▌    ▀▀█▀▀████▀▀▀██  █ ▄█`            #')
        TextSpeed.line('#     ▀▌ ▄█▀ ▄█▀▒▒▒▄█▀▀▒▒▄▀▒▄█▀▀  ██▒▄█▒▒▒▒█▒██           -▀▀████ ,█▀▀              #')
        TextSpeed.line('#      ▀█  ▄█▀▒█▀▀▄▄████▀████    █▀▒█▀▒▒▒▄▌▀▒▒█                ▀▀▀▀                 #')
        TextSpeed.line('#       ╙███▄███▀▀▀¬      -    ▄█▀▒████▀██▌▒▒▒█                                     #')
        TextSpeed.line('#          -                  ██▀▀▀▀▄▄▄   ▀██▐█                                     #')
        TextSpeed.line('#                            █▀ ▄▄▄▀▀  ▀▀0▄ ▀██                                     #')
        TextSpeed.line('#                           █▌█▀    █▀  ,  ▀▌ █▌                                    #')
        TextSpeed.line('#                          █▀ ▌  █▀▀██▀▄█▀  ███                                     #')
        TextSpeed.line('#                          ╙▀█▀  █⌐ ▀▀█▀ ▀████                                      #')
        TextSpeed.line('#                             ▀█▄  ,▄███▀▀-                                         #')
        TextSpeed.line('#                               ▀▀▀▀                                                #')
        TextSpeed.line('#####################################################################################')
        regen = HealMajor.dice()
        Utility.story(f'\n\nYou both settle in for some rest. You regain {(str(regen))} hit points from sleeping.')
        self.myPlayer.hp += regen
        if self.myPlayer.hp > self.myPlayer.max_hp:
            self.myPlayer.hp = self.myPlayer.max_hp
        Utility.continue_prompt()
        Utility.clear()
        self.lumber_mill()

    
    def lumber_mill(self):

        Main.area = 'lumber'
        Main.save_game(self)
        Utility.story('The two of you wake up as the sun rises. A sense of anxiousness washes over you...\
        \nShturman will not be an easy foe. You can sense that you and Meelon are close.')
        Utility.story('\n\nAfter traveling for a few hours you come over the crest of a hill and see the Lumber Mill below.')
        Utility.story('\nThe entire forest becomes quiet... A sudden crack in the air as a bullet narrowly misses you!')
        self.shturman_fight()


    def shturman_fight(self):

        Main.area = 'Shturman'
        Main.save_game(self)
        Utility.story('\n\nA wild Shturman appears!')
        Utility.continue_prompt()
        Utility.clear()
        TextSpeed.line('#######################################################################################################')
        TextSpeed.line('#                                              ▄▄▄▄▄▄▄▄                                               #')
        TextSpeed.line('#                                       ,▄Æ▀▀ -         `▀▀∞▄▄▄▄                                      #')
        TextSpeed.line('#                                   ▄▄▀▀                         `▀▀4▄▄                               #')
        TextSpeed.line('#                                ,▄▀                                    ▀▀▄                           #')
        TextSpeed.line('#                              ▄▀"                                   ,▄▄▄  ▀▄,                        #')
        TextSpeed.line('#                             █`   ▀▀P▄                          ▄▄██▓▓▓▓▓█▄▄-▀▀N▄                    #')
        TextSpeed.line('#                           ▄▀              ▀▀▄               ▄Æ▀░░▀▀█▓▓▓▓▓▓▓▓▓▄, -▀▀▄▄               #')
        TextSpeed.line('#                          ▄▀                  `▀▄,        ,▄▀▒▒▒▒▒▒▒▒░▀██▓▓▓▓▓▓╣▓▓▄   ▀▄             #')
        TextSpeed.line('#                         █                        ▀`   ▄▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▀█▓▓▓▓▓▓▓▓▓▓▄▄ ▀▄           #')
        TextSpeed.line('#                    ▄▄  █                           ▄Æ▀░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▀█▓▓▓▓▓▓▓▓▓█, ▀▄         #')
        TextSpeed.line('#                ▄▄ ▄  -█                         ,█▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▀█▓▓▓▓▓▓▓▓╢█  ▀▄       #')
        TextSpeed.line('#              ,▄▌ -   ▐▌                       ,█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀█▓▓▓▓▓▓▓▓▓█   ▀▄     #')
        TextSpeed.line('#           ▀█,        ▐▄                      ▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐╣▓▓▓▓▓▓▓▓▓█▄  █     #')
        TextSpeed.line('#          ,▄▀`         ▀                    ▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓█  ▐`    #')
        TextSpeed.line('#       ▐█-             ▐                  ▄▀▒▒▒▒▒▒▒▒▄▄ÅÅ▀ÑÑ▄▄▄▄▄▄▄▄▄▄▄▄▄▄░▒▒▒▒▒▒▐▌▓▓▓▓▓▓▓▓▓▓█  █     #')
        TextSpeed.line('#      ▄P▀             █                 ▄▀▒▒▒▒▒▒▄▀▀  ,▄▄████▄▄⌐           ▀▀█░▒▒█▓▓▓▓▓▓▓▓▓▓▓█  █     #')
        TextSpeed.line('#    ▄▀               ▐`               ▄▀░▒▒▒▒▒▄▀    ▀      ▀▀▀▀∞      ███▀▀▀▀▀`▄▓▓▓▓▓▓▓▓▓▓▓╫▌  █     #')
        TextSpeed.line('#     ▄▀              █              ▄█▒▒▒▒▒▒▄▀      ,▄P▀███▀▀▄,        ,▄▄▄▄▄ ▐▌▓▓▓▓▓▓▓▓▓▓▓█   █     #')
        TextSpeed.line('#   ▄▀               ▐▌              ▌▒▒▒▒▒▒▒█      ▀▄   ███▄ ,█      █▐▄ ██▄▐▌█▓▓▓▓▓▓▓▓▓▓▓▓█  ,▌     #')
        TextSpeed.line('#    ▀█              ▐`             ▐▌▒▒▒▒▒▒▒░█       - ▀▀▀▀▀▀         █  ▀▀▀▀ █▓▓▓▓▓▓▓▓▓▓▓▓▌ ,▌      #')
        TextSpeed.line('#   ▄▀                ▌             ▐▒▒▒▒▒▒▒▒▒▒█,                       ▀▄     ▀╣▓▓▓▓▓▓▓▓▓▓▓▌ █       #')
        TextSpeed.line('#   ▀▀█               █             ▐▌▒▒▒▒▒▒▒▒▒▒▒▀▄,                ,,▄▄▄▄,    ╖▀╣▓▓▓▓▓▓▓▓▓█  █       #')
        TextSpeed.line('#    ▐                 ▌             ▐▌▒▒▒▒▒▒▒▒▒▒▒▒░▒▀▀B▄▄▄▄▄▄▄▄▀▀▀░░▒▒▒▒▒▒▀▀▀▀░▒█▓▓▓▓▓▓▓▓█   █       #')
        TextSpeed.line('#   ▄▀                 ▀▄             █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▄▄▄▒▒▒▒▒▒▒█▒▒▒▒▒░▌▓▓▓▓▓▓▓█  ,█        #')
        TextSpeed.line('#   ▀▀█                  ▀▄            █░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▀▒▒░▒░▀▒▄▒▒▒▒▀▀▒▒▒▒▒▒▐╢▓▓▓▓▓▓█  ╒▀         #')
        TextSpeed.line('#    ,▌                    ▀▄           █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒¥▒░█▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓█   █          #')
        TextSpeed.line('#   ▄▀ ,                     ▀&▄        ▀█░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐░▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓█-  █ █Æ█       #')
        TextSpeed.line('#       ▀                       ▀N▄       ▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▌  █    ▀█` ,   #')
        TextSpeed.line('#        █                          ▀▀▄▄    █▒▒▒▒▒▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓█  ▄`     ▀▀█▀   #')
        TextSpeed.line('#         ▀▀█                           `▀▄▄ ▀▀█▄▀ ╙▌▒▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓█▀ ▄▀       ▄▀     #')
        TextSpeed.line('#           █                               ▀▀▀▀    ▀▀` █▒▒▄▀█▒▒▒▒▒▒▒▒▒▒▒▒▄█╣▓▓▓██▀,▄▀        ▄▄▀Γ    #')
        TextSpeed.line('#           █▄█                                         `▀▀  ▀▀█▌▒▒▒▒▒▒░▄█╢▓╢███▀▀▀-       ▄▄▄▌       #')
        TextSpeed.line('#              █  ,▄µ                                         ▄▀-----▀▀▀▀▀▀"               ▐          #')
        TextSpeed.line('#               ▀▀  ▀▄▄▀█                                     ▀▌                     ,   █▀▀          #')
        TextSpeed.line('#                       █▄Aⁿ▀▀▀▄▄▀▌                          ▄4▀ ▄  ▄  ▄▄  ▄▄,    ,P▀`▀X▀             #')
        TextSpeed.line('#                                 █  ▄▄  ,▄▀▄  ,▄∞▀▄,▄▀▀N█▀▀▄▌    ▀▀ ▀▀   ▀   "▀4▀                    #')
        TextSpeed.line('#                                                                                                     #')
        TextSpeed.line('#######################################################################################################')
        result = Utility.initiative()
        if result:
            Turn.turn_count(-1)
            Utility.buff_check(self.myPlayer, self.shturman)
        else:
            Turn.turn_count(0)
            Utility.buff_check(self.shturman, self.myPlayer)
        self.post_shturman_fight()

    
    def post_shturman_fight(self):

        Main.area = 'postShturman'
        Main.save_game(self)
        Utility.continue_prompt()
        Utility.clear()
        Utility.story('Your final shot rings out across the vast wilderness and \nShturman crumples under his own weight, lifeless.')
        Utility.story('\n"We did it!", shouts Meelon. "He\'s finally dead... \nand look, he dropped the Kappa container!"')
        Utility.story('\nThe two of you approach Shturman\'s lifeless body and kneel to inspect the small black container.')
        Utility.story('\nAs your fingers graze the handle you hear a cacophony of horses and men crashing through the woodline.')
        Utility.continue_prompt()
        Utility.clear()
        self.kingsmen()

    def kingsmen(self):

        Main.area = 'kingsmen'
        Main.save_game(self)
        Utility.story('The sound of horns blare out as a crier enters the clearing.')
        Utility.story('\n\n"Make way for KING')
        TextSpeed.slow('...')
        Utility.story(' NIKITA!"')
        Utility.continue_prompt()
        Utility.clear()
        TextSpeed.line('####################################################################################')        
        TextSpeed.line('#                                                                                  #')
        TextSpeed.line('#                                       █`           ,▄                            #')
        TextSpeed.line('#                                     ▄▀█          ▄▀▀█                            #')
        TextSpeed.line('#                                   ▄▀  █▄▄▄▄⌂, ▄▀▀   █                            #')
        TextSpeed.line('#                               ,;,▀   ▐████████▄▄,   █                            #')
        TextSpeed.line('#                              █▀ ▐µ   ████████▀▀▀▀▀▀  ▀▀Wµ    ,▄A▀█               #')
        TextSpeed.line('#                             ▐▐█▀█    ▀████████ ;▄▀█▌  ▀▄▄▄▀▀▀   ▐                #')
        TextSpeed.line('#                            ,█▀▀¬      ▐█  ¬▀█▀▀   █      ▀██▄;  ▌                #')
        TextSpeed.line('#                        ▄&▀▀¬█           ▀▀▀      █ ,       ▄███▄└▄               #')
        TextSpeed.line('#                     ▄▀▀      ▀                   █  ╚▀██▄ ;▄█████▄▀µ   ,▄▄█"     #')
        TextSpeed.line('#                   ▄▀╔      ,█▀▀▄       ,▄▀ª▄     ▌   `▀▄████████▀██▄▀▀▄ ▄▀       #')
        TextSpeed.line('#                 ,█▄▀     ,╛ ▄═  ▀▄     ██   ▌     ▀▄▄  ▀▀▀██▀▀  ▐███████¬        #')
        TextSpeed.line('#                ▄█▀      ▄██▀     `▀▄   ▌ ▀ ▄         ╙▀RN▀╙     ████████  ╓▄█    #')
        TextSpeed.line('#               ▀█╓      ▐▀█          ▀▄  ╙"└                    ▐█████████▀ Z     #')
        TextSpeed.line('#              ,█▀        █             ▀▀▄                ▄▄ⁿN   ╙▀████▀   ╝      #')
        TextSpeed.line('#             ╓█└  ▄╛     ▌              ,▄██▄            █▀█µ █       ,▄▄▄└       #')
        TextSpeed.line('#            ╓█   █-     ▐  ▄█ ╔      ╔▀██▀   "T∞,        ╙∞,µ*       ▐▌█ ▀        #')
        TextSpeed.line('#            █  ▄█▀        ╓██▀       ,▀¬        ,██M▄g                ▐═"         #')
        TextSpeed.line('#           █∞ ▐▀█        .▀         ▄         ▄▀▀       ▀▀▀▀Nm▄▄▄▄▄▄∞▀═           #')
        TextSpeed.line('#          █▀  ╙▐▌                  Æ      C ▄▀                  ▐█▐▌              #')
        TextSpeed.line('#         ▄▀    █                         █▄▀ ▄A▀▀- ╘▀▄   █ █  ▄▄▄█▐▌              #')
        TextSpeed.line('#        ▄▀    ╒                         ██▄██▀▀▐██▀▀▄ ╙º▀█ ▀▐▀▄▄▀█ ▌              #')
        TextSpeed.line('#       ▄▀                            ▌ ▐▀▀" ,A██▀█▀███╙"▀   .███▌█▌▌              #')
        TextSpeed.line('#     ▄█▀                            █ ▄∞ .,▄P▀▀▄╓█▄██   ▀╗   ▀▄▀J.█▐              #')
        TextSpeed.line('#   ⌐▀▀   , .                       █▄▀█   `         █          █ ▌  ▌             #')
        TextSpeed.line('#  ╔▀  ;▄██▀             ▄Æ        ██▀ █             ▐           █▌ ▄▐▄            #')
        TextSpeed.line('# ▀▀▀▀▀▐▄▀,▄▄╙,▄╜     ▄█▀         ██   ▐µ ▄          ▀  █▀▀       █ⁿ▀└▀            #')
        TextSpeed.line('#     f▀▀╙▄▀▀█▀   µ═T▐▀   ,  ,  ,╩╙     ██▌          ,▄▄▄,▄█B    ▄█                #')
        TextSpeed.line('#           █       r,╓∞▐▀ ▄▀ ╔╛   ⌐`    ▀▐Ç     ▄▄███▀▀  "▀█▀ⁿ═▀█   ¬█       ,    #')
        TextSpeed.line('#          █      ▀▀▀¬ ▄█▀██&▀  ▄█¬        ╙▄█▄▀▀ ▐▄▀             ▀∞▄██       █▄   #')
        TextSpeed.line('#          █ ▌        ╙   `   ,▐▐∞         ▄█▀▄▀▀▀          ╖+,     ▄▀       ▐██   #')
        TextSpeed.line('#          ██▌                ▐█ ▌     ,▄▀▀⌐          ▄▀▄▄██████▄▄▄▀        ,▀▐▐   #')
        TextSpeed.line('#          ▐▌▌                █▀▄` ╙▀▀╙            ▄████████████           /   ¬⌐  #')
        TextSpeed.line('#            █ ▌              ▐▄               ▄▄▀▀▀▄  ▀█▄█▄█▄▀▀▀██  ,▄▄█Γ     ▐¬  #')
        TextSpeed.line('#            ▐▄█                ▀▄        ,▄▄▀▀¬    "═w▄   ,w4▄M`    ▀▀-       ██  #')
        TextSpeed.line('#             ▀█▌         ▐▌      `▀▀▀▀▀▀▀-              ▀¬ ▀▄¬               ╙▄   #')
        TextSpeed.line('#               ▀╗        J▀▄                                                ,█▌   #')
        TextSpeed.line('#                 ▀▄         ▀,▌                                             ▄▀    #')
        TextSpeed.line('#                   ▀▄         ▀█*w ▀█▄                   -,             ¿,▄▀      #')
        TextSpeed.line('#                     ▀▀▄           └▀▀ ╙ⁿ═∞Ç▄▄         ╙▀ⁿ╙└-       ,▄▄█▀╙        #')
        TextSpeed.line('#                        ▀▀N▄   ª▄ ▄                          ,▄▄═,▄▄▀▀-           #')
        TextSpeed.line('#                              "^▀█▀█▌"÷∞▄µ,▄▄▄▄▄▄▄-w▄▄▄▄▄&▀▀▀▀▀▀▀                 #')
        TextSpeed.line('#                                                                                  #')
        TextSpeed.line('####################################################################################')
        Utility.continue_prompt()
        Utility.clear()
        Utility.story('\nThe armored men on the horses bend over in respect\nas a portley bearded man endowed with a crown moves through the crowd.')
        Utility.story(f'\n\n"I am King Nikita... you must be {self.myPlayer.name}.\nMy royal spies have been keeping their distance and their eyes on you."')
        if self.myPlayer.on_the_run == True:
            Utility.story(f'\n\n"Your crimes have not been forgotten, {self.myPlayer.name}. But..."')
            Utility.story('\nHe eyes the Kappa container in front of you with wild eyes.')
            Utility.story('\n\n"You have done me quite a favor... Shturman has been giving my vassals the most difficult of times.\
            I will seperate you from this case and you will leave my Kingdom."')
        else:
            Utility.story(f'\n\nThey tell me that you\'ve come to my lands in order to search for wealth, {self.myPlayer.name}...\
            \nThis case would have certainly brought that wealth into your life if I had not been so close by..."')
            Utility.story('\n\n"It\'s a shame that I will have to seperate you from this... beautiful... case."')
        self.knight()


    def knight(self):

        Main.area = 'knight'
        Main.save_game(self)
        Utility.story('\n\nOne of the ploomed kingsmen slides off of his horse and approches you and Meelon.\
        \nHe gives the doge a swift kick and Meelon lets out a yelp.')
        Utility.story('\n"Move, you bloody mutt! Stand away from the King\'s property!"')
        Utility.continue_prompt()
        Utility.clear()
        TextSpeed.line('##################################################################################')
        TextSpeed.line('#                                                                                #')
        TextSpeed.line('#                        ,▄▄▄████████████▄▄▄,                                    #')
        TextSpeed.line('#                      ▄▄██▀▀`            `▀▀▀████▄▄                             #')  
        TextSpeed.line('#                ,▄▄███▀                         ▀▀███▄                          #')
        TextSpeed.line('#       ███████████▀             ,▄▄▄▄▄▄▄▄▄▄▄▄▄      ▀███▄                       #')
        TextSpeed.line('#        ██▀▀▀▀           ,▄▄P▀▀▀▀▀▀▀██████████████▄    ▀██,                     #')
        TextSpeed.line('#         ██▄▄    """""`           ,▄▄████▀▀▀▀▀███████▄   ██▄                    #')
        TextSpeed.line('#           ▀███▀             ,▄▄█▀███▀▀▀▀▀▀▀▀▀▀▀&▄▄█▀██   ▀██                   #')
        TextSpeed.line('#           ▄█▀          ,▄▄███▀▄▀▀▄▄█████████████▄▄,▀▀▄▄   ▐█▌                  #')
        TextSpeed.line('#          ██        ▄▄█████▀▄▀▄████████▀██████████████▄ ▀█▄██▌                  #')
        TextSpeed.line('#        ,██      ,▄██████▀▄▀▄██▀▀             ▀▀█████████▄ ▀█▄                  #')
        TextSpeed.line('#        ██     ,█████▀▀███▄█▀                     ▀████████▄ ▀█▄                #')
        TextSpeed.line('#       ██     ╒███▀   ██▀▄█                         ▀████████▄ ██               #')
        TextSpeed.line('#       █▌     ██     ██▌▄▀                            ▀████████ ▀█▄▄▄▄▄         #')
        TextSpeed.line('#      ▐█▌    ▐█     ▐▌█▐▀                              ▀███████▀ █████████████  #')
        TextSpeed.line('#      ▐█▌    █▌     ██▌▌     ,▄æmæ▄▄▄                   ██▀▀▄A▀▀      ,▄  ▄▄█▀  #')
        TextSpeed.line('#       ██    █      ██     ,█▄█▀▀▀█▄, ▀▀▀R▄▄▄,,   ,,    ,▄█▀    ▄▄▄█ ██████▀    #')
        TextSpeed.line('#       ██▌   ▐▌     ██U    █▐█▌    █ █         `▀▀ ▐█▄▄███▄▄███████▌▄▀▀██       #')
        TextSpeed.line('#       ▐██    ▌     ██▌    █▐██▄,,,█  ▀▄▄           ████████████▀▀`  ,, ██      #')
        TextSpeed.line('#        ██▌   █     █▌█▐    █▄▀▀▀▀▀       ▀▀ⁿ══════─ ▀▀▀▀▀`      ▄█ ███ ██      #')
        TextSpeed.line('#        ▐██    ▌    ███▄█▄   ▀█                         ,▄ █▌ █▌ ██ ▐██ ██      #')
        TextSpeed.line('#         ██▌   █    ▐█▌█ █▄     █,                    █ ██ ██ █▌ ██ ▐██ █▌      #')
        TextSpeed.line('#         ███   █    ██▀ █ ██,     ▀▄^,                █ ██ ██ █▌ ██ ██▌ █       #')
        TextSpeed.line('#         ▐██   ▌   ██    █ ███      ▀4▄¥▄            ▐█ █▌ █▌ █▌ ██ ██ ▐█       #')
        TextSpeed.line('#          ██  ╒ , ▐█   ,█▄▐████▄       ▀N█▀▄,             ▀█ ██ ██▌ ██ █▌       #')
        TextSpeed.line('#         ▐██   ▄  █   ▄████▄▀█████▄       ▀N█▀█▄▄               ▀█ ██ ▐█        #')
        TextSpeed.line('#         ██▄▄███ ▐   ████████▄▀█████▄,       ▀▀▄▀▀███▄▄,              █▌        #')
        TextSpeed.line('#        ▄██████▌ ▌  ███████████▄██▄▄█▀▀█▄        ▀▀▄█▀██████████████ ▐█         #')
        TextSpeed.line('#       ▀▀▀▀   █▌▐  ▐██████████▀      ▀▀█▄▄▀█▄,        ▀R▄▄▀▀▀██████▌ █▌         #')
        TextSpeed.line('#              █▌ƒ  █████████▀            ▀▀▄▄▀████▄▄▄,      ▀▀P∞▄▄▄,▐█          #')
        TextSpeed.line('#              █▌  █████████   "▀▀████▄▄     ▀▀▄▄▀█████▀▀█████████████▌          #')
        TextSpeed.line('#              ██  ██████▀            ▀████▄    ▀█▄▀███▄  ▀▌█████▀▀▀▀▀           #')
        TextSpeed.line('#              ▐█  ███████▀▀▀▀▀▀▀████▄▄  ▀▀███▄▄   ▀█▄▀██,  ▐██                  #')
        TextSpeed.line('#               ██ ███               ▀▀▀█▄▄  ▀████▄, ▀▀▄▀██,  ██,                #')
        TextSpeed.line('#                █▄███                    ▀▀██▄▄`▀████▄▄`▀▄▀▀▄ ▀██▄              #')
        TextSpeed.line('#                ▐████                         ▀▀██████████▄██═▄b▄███▄▄,         #')
        TextSpeed.line('#                 ▀███                                ▀▀▀▀▀████████▀▀▀▀▀         #')
        TextSpeed.line('#                   ▀██                                                          #')
        TextSpeed.line('#                     ▀█                                                         #')
        TextSpeed.line('#                                                                                #')
        TextSpeed.line('##################################################################################')
        Utility.continue_prompt()
        Utility.clear()
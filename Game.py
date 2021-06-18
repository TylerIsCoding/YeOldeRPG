from typing import Text
from Dice import *
from Enemy import Nick
from Enemy import Steven
from random import *
from Player import *
from Utility import *

class Game:

    myPlayer = Player("name")
    nick = Nick()
    steven = Steven()


    def main_menu(self):

        Utility.clear() 
        Utility.menu("\n############################")
        Utility.menu("\nWelcome to Ye Olde Text RPG!")
        Utility.menu("\n############################")
        Utility.menu("\n       --(P)lay--")
        Utility.menu("\n      --(O)ptions--")
        Utility.menu("\n       --(Q)uit--")
        print('\n' * 5)
        main_menu_selection = input("\n>>> ")
        if "p" in main_menu_selection.lower():
            Utility.story = TextSpeed.normal
            Utility.combat = TextSpeed.normal
            self.player_name()
        elif "o" in main_menu_selection.lower():
            self.options()
        elif "q" in main_menu_selection.lower():
            quit()
        else:
            Utility.menu("\nYou must select Play or Quit.\n")
            self.main_menu()
    
    def options(self):
        
        Utility.clear()
        Utility.menu("\n############################")
        Utility.menu("\n#         Options          #")
        Utility.menu("\n############################")
        Utility.menu("\n    1.) Story Text Speed    ")
        Utility.menu("\n      2.) Combat Speed      ")
        Utility.menu("\n          (R)eturn          ")
        answer = input('\n\n>>> ')
        if str(1) in answer:
            self.story_text_speed()
        elif str(2) in answer:
            self.combat_text_speed()
        elif "r" in answer.lower():
            self.main_menu()
        else:
            Utility.menu('\nYou need to make a valid selection.')
            self.options()
    
    def story_text_speed(self):

        Utility.clear()
        Utility.menu("\n############################")
        Utility.menu("\n#     Story Text Speed     #")
        Utility.menu("\n############################")
        Utility.menu("\n        1.) Normal          ")
        Utility.menu("\n        2.) Fast            ")
        Utility.menu("\n        3.) Instant         ")
        Utility.menu("\n          (R)eturn          ")
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
            Utility.menu('\nYou need to make a valid selection.')
            self.story_text_speed()
    
    def combat_text_speed(self):

        Utility.clear()
        Utility.menu("\n############################")
        Utility.menu("\n#       Combat Speed       #")
        Utility.menu("\n############################")
        Utility.menu("\n        1.) Normal          ")
        Utility.menu("\n        2.) Fast            ")
        Utility.menu("\n        3.) Instant         ")
        Utility.menu("\n          (R)eturn          ")
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
            Utility.menu('\nYou need to make a valid selection.')
            self.story_text_speed()

    def player_name(self):

        Utility.clear()
        Utility.story("\nWhat is your name?")
        self.myPlayer.name = input("\n>>> ").title()
        self.player_setup()

    def player_setup(self):

        Utility.clear()
        Utility.story("\nAre you a (W)arrior, (M)age, (R)ogue, or (B)arbarian?")
        answer_2 = input("\n>>> ")
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
        while self.skillselection1():
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

    def skillselection1(self):

            Utility.clear()
            Utility.story('\n\nYou now must choose two skills.')
            Utility.story('\n\nFor your first skill, do you want an (A)ttack Skill, a (B)uff Skill, or a (R)estorative Skill?')
            answer = input('\n\n>>>')
            if "a" in answer.lower():
                Utility.story('\n\nHere are the available Attack Skills:')
                TextSpeed.fast('\n#####################################')
                if self.myPlayer.role == "Warrior":
                    for key, value in AttackSkill.warrior_attack_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill1 = AttackSkill.warrior_attack_skill_list[int(answer1)]
                    self.skillselection2()
                elif self.myPlayer.role == "Mage":
                    for key, value in AttackSkill.mage_attack_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill1 = AttackSkill.mage_attack_skill_list[int(answer1)]
                    self.skillselection2()
                elif self.myPlayer.role == "Rogue":
                    for key, value in AttackSkill.rogue_attack_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill1 = AttackSkill.rogue_attack_skill_list[int(answer1)]
                    self.skillselection2()
                elif self.myPlayer.role == "Barbarian":
                    for key, value in AttackSkill.barb_attack_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill1 = AttackSkill.barb_attack_skill_list[int(answer1)]
                    self.skillselection2()
            elif "b" in answer.lower():
                Utility.story('\n\nHere are the available Buff Skills:')
                TextSpeed.fast('\n#####################################')
                for key, value in BuffSkill.buff_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                answer1 = input('\n>>> ')
                self.myPlayer.skill1 = BuffSkill.buff_skill_list[int(answer1)]
                self.skillselection2()
            elif "r" in answer.lower():
                Utility.story('\n\nHere are the available Restorative Skills:')
                TextSpeed.fast('\n##########################################')
                for key, value in RecoverySkill.recovery_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                answer1 = input('\n>>> ')
                self.myPlayer.skill1 = RecoverySkill.recovery_list[int(answer1)]
                self.skillselection2()
            else:
                self.skillselection1()

    def skillselection2(self):

            Utility.clear()
            Utility.story('\n\nYou now must choose the second skill.')
            Utility.story('\n\nFor your second skill, do you want an (A)ttack Skill, a (B)uff Skill, or a (R)estorative Skill?')
            answer = input('\n\n>>>')
            if "a" in answer.lower():
                Utility.story('\n\nHere are the available Attack Skills:')
                Utility.story('\n#####################################')
                if self.myPlayer.role == "Warrior":
                    for key, value in AttackSkill.warrior_attack_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill2 = AttackSkill.warrior_attack_skill_list[int(answer1)]
                    if self.myPlayer.skill1 == self.myPlayer.skill2:
                        Utility.story('\n\nThe second skill cannot be the same as the first. Try again.')
                        self.skillselection2()
                    else:
                        self.confirmation()
                elif self.myPlayer.role == "Mage":
                    for key, value in AttackSkill.mage_attack_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill2 = AttackSkill.mage_attack_skill_list[int(answer1)]
                    if self.myPlayer.skill1 == self.myPlayer.skill2:
                        Utility.story('\n\nThe second skill cannot be the same as the first. Try again.')
                        self.skillselection2()
                    else:
                        self.confirmation()
                elif self.myPlayer.role == "Rogue":
                    for key, value in AttackSkill.rogue_attack_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill2 = AttackSkill.rogue_attack_skill_list[int(answer1)]
                    if self.myPlayer.skill1 == self.myPlayer.skill2:
                        Utility.story('\n\nThe second skill cannot be the same as the first. Try again.')
                        self.skillselection2()
                    else:
                        self.confirmation()
                elif self.myPlayer.role == "Barbarian":
                    for key, value in AttackSkill.barb_attack_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill2 = AttackSkill.barb_attack_skill_list[int(answer1)]
                    if self.myPlayer.skill1 == self.myPlayer.skill2:
                        Utility.story('\n\nThe second skill cannot be the same as the first. Try again.')
                        self.skillselection2()
                    else:
                        self.confirmation()
            elif "b" in answer.lower():
                Utility.story('\n\nHere are the available Buff Skills:')
                TextSpeed.fast('\n#####################################')
                for key, value in BuffSkill.buff_skill_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                answer1 = input('\n>>> ')
                self.myPlayer.skill2 = BuffSkill.buff_skill_list[int(answer1)]
                if self.myPlayer.skill1 == self.myPlayer.skill2:
                    Utility.story('\n\nThe second skill cannot be the same as the first. Try again.')
                    self.skillselection2()
                else:
                    self.confirmation()
            elif "r" in answer.lower():
                Utility.story('\n\nHere are the available Restorative Skills:')
                TextSpeed.fast('\n##########################################')
                for key, value in RecoverySkill.recovery_list.items():
                        Utility.story(f"\n{str(key)}.) {value['name']}")
                answer1 = input('\n>>> ')
                self.myPlayer.skill2 = RecoverySkill.recovery_list[int(answer1)]
                if self.myPlayer.skill1 == self.myPlayer.skill2:
                    Utility.story('\n\nThe second skill cannot be the same as the first. Try again.')
                    self.skillselection2()
                else:
                    self.confirmation()
            else:
                self.skillselection2()
    


    def confirmation(self):

        Utility.clear()
        Utility.story(f"\n   {self.myPlayer.name} the {self.myPlayer.role}")
        Utility.story("\n########################")
        Utility.story(f"\nHit Points: {self.myPlayer.hp}")
        Utility.story(f"\nMana Points: {self.myPlayer.mp}")
        Utility.story(f"\nDefence: {self.myPlayer.defense}")
        Utility.story(f"\nAttack Dice: {self.myPlayer.max_attack_str}")
        skillset = "{0}, {1}".format(str(self.myPlayer.skill1['name']), str(self.myPlayer.skill2['name']))
        Utility.story(f'\nSkills: {str(skillset)}')
        Utility.story("\n\nRe-roll? (Y)es or (N)o")
        answer_3 = input("\n>>> ")
        if "n" in answer_3:
            return False
        elif "y" in answer_3:
            print('\n' * 10)
            self.player_setup()
            return True
        else:
            Utility.story("\n\nYou have to choose (Y)es or (N)o\n")
            self.confirmation()
    

    def chapter_one_begin(self):

        Utility.clear()
        Utility.menu("\n                            #########################")
        Utility.menu("\n                            #      Chapter One      #")
        Utility.menu("\n                            #########################")
        Utility.story("\n\n\nAs night falls you enter a small tavern on the crossroads.")
        Utility.story("\n\nThere aren't many patrons in the tavern but the fireplace \nburns bright and the ale seems to be flowing.")
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
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
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
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
                I can see by your outfit and your gear, \nthat you must be a {self.myPlayer.role.lower()}.')
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

        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
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

        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:

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
                Utility.enemy_attack(self.nick, self.myPlayer)
            self.post_nick_fight()
            
    def post_nick_fight(self):
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:

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
                
                continue_prompt_2 = input("\n\n>>> Hit enter to build camp.")
                if '' in continue_prompt_2:
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
        regen = RecoverySkill.heal_major['dice']()
        Utility.story(f'\n\nYou both settle in for some rest. You regain {(str(regen))} hit points back.')
        self.myPlayer.hp += regen
        Utility.story('\nDaylight creeps over the hills and treetops. The two of you gather your gear and start towards the Woods.')
        Utility.story('\nAs you walk Meelon continues explaining about Shturman.')
        Utility.story('\n\n"Shturman is said to be in possession of the mighty Kappa container...\nIt has the ability to hold a vast amount of items in a very small space."')
        Utility.story('\n\n"If we could aquire the Kappa container AND remove Shturman\'s evil hold \non the Woods, I\'m sure that the King would be most grateful."')
        Utility.story(f'\n\n"Listen, {self.myPlayer.name}, we should head East. \nThat\'s where Shturman was last spotted... or so I\'ve heard..."')
        Utility.story('\n\n\nThe two of you head East to see if you can find any traces of Shturman. \nAs you try to locate any clues you hear the sound of twigs snapping\nand the unmistakable smell of sweat!')
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
            self.steven_fight()

    def steven_fight(self):
        Utility.clear()
        Utility.story('\nA wild Sweaty Steven appears!')
        result = Utility.initiative()
        if result:
            Turn.turn_count(-1)
            Utility.player_combat_prompt(self.myPlayer, self.steven)
        else:
            Turn.turn_count(0)
            Utility.enemy_attack(self.steven, self.myPlayer)
        


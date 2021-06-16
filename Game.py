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

        print("\n" * 100) 
        Utility.typingPrint("\n############################")
        Utility.typingPrint("\nWelcome to Ye Olde Text RPG!")
        Utility.typingPrint("\n############################")
        Utility.typingPrint("\n       --(P)lay--")
        Utility.typingPrint("\n      --(O)ptions--")
        Utility.typingPrint("\n       --(Q)uit--")
        print('\n' * 10)
        main_menu_selection = input("\n>>> ")
        if "p" in main_menu_selection.lower():
            self.player_setup()
        elif "o" in main_menu_selection.lower():
            self.options()
        elif "q" in main_menu_selection.lower():
            quit()
        else:
            print("\n" * 100)
            Utility.typingPrint("\nYou must select Play or Quit.\n")
            self.main_menu()
    
    def options(self):

        Utility.typingPrint("\n############################")
        Utility.typingPrint("\n#         Options          #")
        Utility.typingPrint("\n############################")
        Utility.typingPrint("\n       --Text Speed--")
        Utility.typingPrint("\n         1.) Normal")
        Utility.typingPrint("\n         2.) Fast")
        Utility.typingPrint("\n         3.) Instant")
        Utility.typingPrint("\n          (R)eturn")
        answer = input('\n\n>>> ')
        if str(1) in answer:
            self.main_menu()
        elif str(2) in answer:
            self.main_menu()
        elif str(3) in answer:
            self.main_menu()
        elif "r" in answer.lower():
            self.main_menu()
        else:
            Utility.typingPrint('\nYou need to make a valid selection.')
            self.options()


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
            self.skillselection1()
        while self.skillselection1():
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

    def skillselection1(self):

            Utility.typingPrint('\n\nYou now must choose two skills.')
            Utility.typingPrint('\n\nFor your first skill, do you want an (A)ttack Skill, a (B)uff Skill, or a (R)estorative Skill?')
            answer = input('\n\n>>>')
            if "a" in answer.lower():
                Utility.typingPrint('\n\nHere are the available Attack Skills:')
                Utility.fastTypingPrint('\n#####################################')
                if self.myPlayer.role == "Warrior":
                    for key, value in AttackSkill.warrior_attack_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill1 = AttackSkill.warrior_attack_skill_list[int(answer1)]
                    self.skillselection2()
                elif self.myPlayer.role == "Mage":
                    for key, value in AttackSkill.mage_attack_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill1 = AttackSkill.mage_attack_skill_list[int(answer1)]
                    self.skillselection2()
                elif self.myPlayer.role == "Rogue":
                    for key, value in AttackSkill.rogue_attack_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill1 = AttackSkill.rogue_attack_skill_list[int(answer1)]
                    self.skillselection2()
                elif self.myPlayer.role == "Barbarian":
                    for key, value in AttackSkill.barb_attack_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill1 = AttackSkill.barb_attack_skill_list[int(answer1)]
                    self.skillselection2()
            elif "b" in answer.lower():
                Utility.typingPrint('\n\nHere are the available Buff Skills:')
                for key, value in BuffSkill.buff_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                answer1 = input('\n>>> ')
                self.myPlayer.skill1 = BuffSkill.buff_skill_list[int(answer1)]
                self.skillselection2()
            elif "r" in answer.lower():
                Utility.typingPrint('\n\nHere are the available Restorative Skills:')
                for key, value in RecoverySkill.recovery_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                answer1 = input('\n>>> ')
                self.myPlayer.skill1 = RecoverySkill.recovery_list[int(answer1)]
                self.skillselection2()
            else:
                self.skillselection1()

    def skillselection2(self):

            Utility.typingPrint('\n\nYou now must choose the second skill.')
            Utility.typingPrint('\n\nFor your second skill, do you want an (A)ttack Skill, a (B)uff Skill, or a (R)estorative Skill?')
            answer = input('\n\n>>>')
            if "a" in answer.lower():
                Utility.typingPrint('\n\nHere are the available Attack Skills:')
                Utility.fastTypingPrint('\n#####################################')
                if self.myPlayer.role == "Warrior":
                    for key, value in AttackSkill.warrior_attack_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill2 = AttackSkill.warrior_attack_skill_list[int(answer1)]
                    if self.myPlayer.skill1 == self.myPlayer.skill2:
                        Utility.typingPrint('\n\nThe second skill cannot be the same as the first. Try again.')
                        self.skillselection2()
                    else:
                        self.confirmation()
                elif self.myPlayer.role == "Mage":
                    for key, value in AttackSkill.mage_attack_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill2 = AttackSkill.mage_attack_skill_list[int(answer1)]
                    if self.myPlayer.skill1 == self.myPlayer.skill2:
                        Utility.typingPrint('\n\nThe second skill cannot be the same as the first. Try again.')
                        self.skillselection2()
                    else:
                        self.confirmation()
                elif self.myPlayer.role == "Rogue":
                    for key, value in AttackSkill.rogue_attack_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill2 = AttackSkill.rogue_attack_skill_list[int(answer1)]
                    if self.myPlayer.skill1 == self.myPlayer.skill2:
                        Utility.typingPrint('\n\nThe second skill cannot be the same as the first. Try again.')
                        self.skillselection2()
                    else:
                        self.confirmation()
                elif self.myPlayer.role == "Barbarian":
                    for key, value in AttackSkill.barb_attack_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                    answer1 = input('\n>>> ')
                    self.myPlayer.skill2 = AttackSkill.barb_attack_skill_list[int(answer1)]
                    if self.myPlayer.skill1 == self.myPlayer.skill2:
                        Utility.typingPrint('\n\nThe second skill cannot be the same as the first. Try again.')
                        self.skillselection2()
                    else:
                        self.confirmation()
            elif "b" in answer.lower():
                Utility.typingPrint('\n\nHere are the available Buff Skills:')
                for key, value in BuffSkill.buff_skill_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                answer1 = input('\n>>> ')
                self.myPlayer.skill2 = BuffSkill.buff_skill_list[int(answer1)]
                if self.myPlayer.skill1 == self.myPlayer.skill2:
                    Utility.typingPrint('\n\nThe second skill cannot be the same as the first. Try again.')
                    self.skillselection2()
                else:
                    self.confirmation()
            elif "r" in answer.lower():
                Utility.typingPrint('\n\nHere are the available Restorative Skills:')
                for key, value in RecoverySkill.recovery_list.items():
                        Utility.fastTypingPrint(f"\n{str(key)}.) {value['name']}")
                answer1 = input('\n>>> ')
                self.myPlayer.skill2 = RecoverySkill.recovery_list[int(answer1)]
                if self.myPlayer.skill1 == self.myPlayer.skill2:
                    Utility.typingPrint('\n\nThe second skill cannot be the same as the first. Try again.')
                    self.skillselection2()
                else:
                    self.confirmation()
            else:
                self.skillselection2()
    


    def confirmation(self):

        Utility.typingPrint(f"\n   {self.myPlayer.name} the {self.myPlayer.role}")
        Utility.typingPrint("\n########################")
        Utility.typingPrint(f"\nHit Points: {self.myPlayer.hp}")
        Utility.typingPrint(f"\nMana Points: {self.myPlayer.mp}")
        Utility.typingPrint(f"\nDefence: {self.myPlayer.defense}")
        Utility.typingPrint(f"\nAttack Dice: {self.myPlayer.max_attack_str}")
        skillset = "{0}, {1}".format(str(self.myPlayer.skill1['name']), str(self.myPlayer.skill2['name']))
        Utility.typingPrint(f'\nSkills: {str(skillset)}')
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
            print('\n' * 100)
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
            print('\n' * 100)                                                                                            
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

            print('\n' * 100)
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
                Utility.enemy_attack(self.nick, self.myPlayer)
            self.post_nick_fight()
            
    def post_nick_fight(self):
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:

            Utility.typingPrint('\n\n"Wow!" says Meelon. "It looks like you can fight... \nLook, he dropped this after you got him."')
            get_loot = input('\n\n>>> Hit enter to loot the scav.')
            if '' in get_loot:

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
                
                continue_prompt_2 = input("\n\n>>> Hit enter to build camp.")
                if '' in continue_prompt_2:
                    self.woods()


    def woods(self):
        print('\n' * 100)
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
        regen = randint(2, 4)
        Utility.typingPrint('\n\nYou both settle in for some rest. You regain {0} hit points back.'.format(str(regen)))
        self.myPlayer.hp += regen
        Utility.typingPrint('\nDaylight creeps over the hills and treetops. The two of you gather your gear and start towards the Woods.')
        Utility.typingPrint('\nAs you walk Meelon continues explaining about Shturman.')
        Utility.typingPrint('\n\n"Shturman is said to be in possession of the mighty Kappa container...\nIt has the ability to hold a vast amount of items in a very small space."')
        Utility.typingPrint('\n\n"If we could aquire the Kappa container AND remove Shturman\'s evil hold \non the Woods, I\'m sure that the King would be most grateful."')
        Utility.typingPrint('\n\n"Listen, {0}, we should head East. \nThat\'s where Shturman was last spotted... or so I\'ve heard..."'.format(self.myPlayer.name))
        Utility.typingPrint('\n\n\nThe two of you head East to see if you can find any traces of Shturman. \nAs you try to locate any clues you hear the sound of twigs snapping\nand the unmistakable smell of sweat!')
        continue_prompt = input("\n\n>>> Hit enter to continue")
        if '' in continue_prompt:
            self.steven_fight()

    def steven_fight(self):
        print('\n' * 100)
        Utility.typingPrint('\nA wild Sweaty Steven appears!')
        result = Utility.initiative()
        if result:
            Utility.player_combat_prompt(self.myPlayer, self.steven)
        else:
            Utility.enemy_attack(self.steven, self.myPlayer)
        


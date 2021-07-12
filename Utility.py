##### Imports #####
import time, sys
from typing import *
from Dice import *
from random import *
import random
###################

class TextSpeed:


  @staticmethod
  def normal(text):

    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)


  @staticmethod
  def fast(text):

    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.001)
  
  
  @staticmethod
  def instant(text):

    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0)


  @staticmethod
  def slow(text):

    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(1)

  @staticmethod
  def line(text):

    print(text)
    time.sleep(.1)

class Turn:

  current_turn = ''
  def_turns_passed = 1
  def_enemy_turns_passed = 1
  atk_turns_passed = 1
  atk_enemy_turns_passed = 1

  def turn_count(turn):

    turn += 1
    Turn.current_turn = turn
  
  def clear_turn():

      Turn.current_turn -= 1


class HealthBar:


  def Health(player):

    hp = player.hp
    maxhp = player.max_hp

    if int(hp) == int(maxhp):
      return (' ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰') 
    elif int(hp) >= int(maxhp) * 0.9:
      return (' ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▱') 
    elif int(hp) >= int(maxhp) * 0.8:
      return (' ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▱ ▱') 
    elif int(hp) >= int(maxhp) * 0.7:
      return (' ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▱ ▱ ▱') 
    elif int(hp) >= int(maxhp) * 0.6:
      return (' ▰ ▰ ▰ ▰ ▰ ▰ ▱ ▱ ▱ ▱') 
    elif int(hp) >= int(maxhp) * 0.5:
      return (' ▰ ▰ ▰ ▰ ▰ ▱ ▱ ▱ ▱ ▱') 
    elif int(hp) >= int(maxhp) * 0.4:
      return (' ▰ ▰ ▰ ▰ ▱ ▱ ▱ ▱ ▱ ▱') 
    elif int(hp) >= int(maxhp) * 0.3:
      return (' ▰ ▰ ▰ ▱ ▱ ▱ ▱ ▱ ▱ ▱') 
    elif int(hp) >= int(maxhp) * 0.2:
      return (' ▰ ▰ ▱ ▱ ▱ ▱ ▱ ▱ ▱ ▱') 
    elif int(hp) >= int(maxhp) * 0.1:
      return (' ▰ ▱ ▱ ▱ ▱ ▱ ▱ ▱ ▱ ▱') 
    elif int(hp) >= 0:
      return (' ▱ ▱ ▱ ▱ ▱ ▱ ▱ ▱ ▱ ▱')


  def HealthNum(player):

    hp = player.hp
    maxhp = player.max_hp

    return (f'HP: {hp}/{maxhp}')


  def Mana(player):

      pips = player.mp
      if pips > 0:
        return (f'⬤ ' * pips)
      else:
        return (f'◯')
  
  def ManaNum(player):

    return (f'MP: {player.mp}')


  def DisplayBars(player, enemy):

    a = (f' ' * 4 + f'{HealthBar.HealthNum(player)}')
    b = (f' ' * 4 + f'{HealthBar.ManaNum(player)}')
    c = (f'{HealthBar.Health(player)}' + ' ' * 8)
    d = HealthBar.Mana(player)
    e = (f' {player.name}')
    f = (f' ' * 4 + f'{HealthBar.HealthNum(enemy)}')
    g = (f' ' * 4 + f'{HealthBar.ManaNum(enemy)}')
    h = (f'{HealthBar.Health(enemy)}' + ' ' * 8)
    i = HealthBar.Mana(enemy)
    j = (f' {enemy.name}')

    result = (44 - (len(a) + len(c)))
    x = ' ' * result
    result2 = (len(a) + len(x) - len(b)) + 1
    y = ' ' * result2
    result3 = (44 - (len(b) + len(y) + len(d)))
    z = ' ' * result3
    result4 = (44 - (len(f) + len(h)))
    q = ' ' * result4
    result5 = (len(f) + len(q) - len(g)) + 1
    r = ' ' * result5
    result6 = (44 - (len(g) + len(r) + len(i)))
    s = ' ' * result6


    if player.type == "Player":
      Utility.combatline(f'|{e:<44}' + '|')
      Utility.combatline(f'|{a}' + f'{x}' + f'{c}' + '|')
      Utility.combatline(f'|{b}' + f'{y}' + f'{d}' + f'{z}' +'|')
      Utility.combatline('|' + '-' * 44 + '|')
      Utility.combatline(f'|{j:<44}' + '|')
      Utility.combatline(f'|{f}' + f'{q}' + f'{h}' + '|')
      Utility.combatline(f'|{g}' + f'{r}' + f'{i}' + f'{s}' +'|')
      Utility.combatline(f'+' + '=' * 44 + '+')
    else:
      Utility.combatline(f'|{j:<44}' + '|')
      Utility.combatline(f'|{f}' + f'{q}' + f'{h}' + '|')
      Utility.combatline(f'|{g}' + f'{r}' + f'{i}' + f'{s}' +'|')
      Utility.combatline('|' + '-' * 44 + '|')
      Utility.combatline(f'|{e:<44}' + '|')
      Utility.combatline(f'|{a}' + f'{x}' + f'{c}' + '|')
      Utility.combatline(f'|{b}' + f'{y}' + f'{d}' + f'{z}' +'|')
      Utility.combatline(f'+' + '=' * 44 + '+')



class Utility:


  def continue_prompt():
    continue_prompt = input("\n\n>>> Hit enter to continue")
    if '' in continue_prompt:
      None
  

  @staticmethod
  def story(text):

    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)


  @staticmethod
  def menu(text):

    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.02)
  

  @staticmethod
  def combat(text):

    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.001)
    
  

  @staticmethod
  def combatline(text):

    print(text)
    time.sleep(.2)


  @staticmethod
  def clear():

    print('\n' * 100)


  @staticmethod
  def gameOver():

    Utility.menu("\nGame over! Would you like to try again?")
    Utility.menu("\n(Y)es or (N)o")
    answer = input("\n>>> ")
    if "y" in answer.lower():
      Game.main_menu()
    elif "n" in answer.lower():
      quit()
    else:
      Utility.gameOver()


##### INITIATIVE #####


  def initiative():

    player_init = Dice.d_10()
    enemy_init = Dice.d_10()
    Utility.story('\nYou both roll for initiative!')
    Utility.story("\n\nYou rolled a " + str(player_init) + " and the enemy rolled a " + str(enemy_init) + ".")
    if player_init > enemy_init:
      Utility.story('\n\nYou rolled higher and get the first attack!\n')
      return True
    elif player_init == enemy_init:
      Utility.story('\n\nYou both tied. The enemy gets to attack first!')
      Utility.continue_prompt()
      Utility.clear()
      return False
    else:
      Utility.story('\n\nThe enemy rolled higher and gets the first attack!\n')
      Utility.continue_prompt()
      Utility.clear()
      return False


##### BUFF FUNCTIONS #####


  def buff_check(player, enemy):

    if player.type == "Player":
      if player.def_buff == Default and player.atk_buff == Default:
        Utility.player_combat_prompt(player, enemy)
      elif player.def_buff != Default and player.atk_buff == Default:
        if player.def_buff.duration == Turn.def_turns_passed:
          Utility.combat(f'{player.def_buff.name} has worn off!')
          player.def_buff = Default
          Utility.player_combat_prompt(player, enemy)
        else:
          Utility.player_combat_prompt(player, enemy)
      elif player.def_buff == Default and player.atk_buff != Default:
        if player.atk_buff.duration == Turn.atk_turns_passed:
          Utility.combat(f'{player.atk_buff.name} has worn off!')
          player.atk_buff = Default
          Utility.player_combat_prompt(player, enemy)
        else:
          Utility.player_combat_prompt(player, enemy)
    elif player.type == "Enemy":
      Utility.combat('\n\n#############################################')
      Utility.combat(f"\n\n{player.name}'s Turn!")
      Utility.continue_prompt()
      Utility.clear()
      if player.def_buff == Default and player.atk_buff == Default:
        SkillUse.enemy_skill(player, enemy)
      elif player.def_buff != Default and player.atk_buff == Default:
        if player.def_buff.duration == Turn.def_enemy_turns_passed:
          Utility.combat(f'{player.def_buff.name} has worn off!')
          player.def_buff = Default
          SkillUse.enemy_skill(player, enemy)
        else:
          SkillUse.enemy_skill(player, enemy)
      elif player.def_buff == Default and player.atk_buff != Default:
        if player.atk_buff.duration == Turn.atk_turns_passed:
          Utility.combat(f'{player.atk_buff.name} has worn off!')
          player.atk_buff = Default
          SkillUse.enemy_skill(player, enemy)
        else:
          SkillUse.enemy_skill(player, enemy)



      
  def buff_clear(player, enemy):

    player.atk_buff = Default
    player.def_buff = Default
    enemy.atk_buff = Default
    enemy.def_buff = Default


##### COMBAT FUNCTIONS #####


  def player_combat_prompt(player, enemy):

    Utility.combatline('\n\n##############################################')
    Utility.combatline('\n')
    Utility.combatline('Your turn!')
    Utility.continue_prompt()
    Utility.clear()
    this_turn = Turn.current_turn
    Turn.def_turns_passed += 1
    Turn.def_enemy_turns_passed += 1
    Turn.atk_turns_passed += 1
    Turn.atk_enemy_turns_passed += 1
    Turn.turn_count(this_turn)
    a = ('#############') 
    b = (f'#  Turn: {Turn.current_turn}  #')
    c = ('#############')
    Utility.combatline(f'\n{a:^46}')
    Utility.combatline(f'{b:^46}')
    Utility.combatline(f'{c:^46}')
    Utility.combatline("\n==============================================") 
    Utility.combatline("|  Do you (A)ttack or do you use a (S)kill?  |")
    Utility.combatline("==============================================\n")
    result1 = len(HealthBar.HealthNum(player)) + 2
    result2 = len(HealthBar.ManaNum(player))
    Utility.combatline(f'{HealthBar.HealthNum(player)} {HealthBar.Health(player)}')
    Utility.combatline(f'{HealthBar.ManaNum(player)}' + ' ' * (result1 - result2) + f'{HealthBar.Mana(player)}')
    if player.def_buff.name != "default":
      Utility.combatline(f"Buff: {player.def_buff.name} | Turns Remaining: {player.def_buff.duration - Turn.def_turns_passed + 1}")
      Utility.combatline(f"Defense: {player.defense} + {player.def_buff.maxbuff}")
    else:
      Utility.combatline(f"Defense: {player.defense}")
    if player.atk_buff.name != "default":
      Utility.combatline(f"Buff: {player.atk_buff.name} | Turns Remaining: {player.atk_buff.duration - Turn.atk_turns_passed + 1}")
      Utility.combatline(f"Attack: {player.max_attack_str} + {player.atk_buff.maxbuff}")
    else:
      Utility.combatline(f"Attack: {player.max_attack_str}")
    d = ('+------------------+')
    e = ('|      Skills      |')  
    f = ('+------------------+')  
    Utility.combatline(f'\n{d:^45}')
    Utility.combatline(f'{e:^45}')
    Utility.combatline(f'{f:^45}\n')
    for skill in player.skills:
      Utility.combatline(f'{skill.name} | MP: {skill.mpcost}')
    Utility.combatline('\nPress (D) for skill descriptions.')
    answer = input('\n\n>>> ')
    if 'a' in answer.lower():
      Utility.attack(player, enemy)
    elif 's' in answer.lower():
      SkillUse.player_skill(player, enemy)
    elif 'd' in answer.lower():
      for skill in player.skills:
        Utility.combatline(f'\n{skill.name}:{skill.skilldes}')
      Utility.continue_prompt()
      Utility.clear()
      Utility.player_combat_prompt(player, enemy)
    else:
      Utility.combat('You must make a valid selection.')
      Turn.clear_turn()
      Utility.player_combat_prompt(player, enemy)
     

  def attack(player, enemy):

    atkbuff = player.atk_buff.dice()
    defbuff = enemy.def_buff.dice()
    attack = player.atk() + player.additional_damage
    enemyblock = enemy.blk()
    damage = attack + atkbuff
    block = enemyblock + defbuff
    enemy.hp -= (damage - block) if (damage - block) > 0 else 0
    if enemy.hp < 0:
      enemy.hp = 0
    Utility.combat(f'\n\n{player.name} attacks!')
    print('\n')
    a = (f"| Attack Roll [ {player.max_attack_str} ] = {attack}")
    b = (f"| Defense Roll [ {enemy.defense} ] = {enemyblock}")
    c = (f'|  Total Damage = {(damage - block) if (damage - block) > 0 else 0}  |')
    d = (f'| {player.name}')
    e = (f"| Defense Buff [ {enemy.def_buff.maxbuff} ] = {defbuff}")
    f = (f"| Attack Buff [ {player.atk_buff.maxbuff} ] = {atkbuff}")
    g = (f'| {enemy.name}')
    length = len(c)
    h = ('=' * length)
    Utility.combatline(f'+' + '=' * 44 + '+')
    Utility.combatline(f"{d:<45}|")
    Utility.combatline('|' + '-' * 44 + '|')
    Utility.combatline('|' + ' ' * 44 + '|')
    Utility.combatline(f"{a:<45}|")
    if player.atk_buff != Default:
      Utility.combatline(f"{f:<45}|")
    Utility.combatline('|' + ' ' * 44 + '|')
    Utility.combatline('+' + '=' * 44 + '+\n')
    Utility.combatline('+' + '=' * 44 + '+')
    Utility.combatline(f"{g:<45}|")  
    Utility.combatline('|' + '-' * 44 + '|')
    Utility.combatline('|' + ' ' * 44 + '|')
    Utility.combatline(f"{b:<45}|")
    if enemy.def_buff != Default:
      Utility.combatline(f"{e:<45}|")
    Utility.combatline('|' + ' ' * 44 + '|')
    Utility.combatline('+' + '=' * 44 + '+\n')
    Utility.combatline(f'{h:^46}')
    Utility.combatline(f"{c:^46}")
    Utility.combatline(f'{h:^46}\n')
    Utility.combatline('+' + '=' * 44 + '+')
    HealthBar.DisplayBars(player, enemy)
    if enemy.hp == 0 and enemy.type == "Enemy":
      Recovery.mp_recovery(player)
      Utility.enemy_killed(enemy, player)
    elif enemy.hp == 0 and enemy.type == "Player":
      Utility.player_killed(enemy)
    else:
      Recovery.mp_recovery(player)
      Utility.buff_check(enemy, player)



##### DEATH FUNCTIONS #####


  def player_killed(player):

      Utility.combat('\nYou have been killed!\n')
      Utility.gameOver()


  def enemy_killed(enemy, player):

      a = (f'*   {enemy.name} has been killed!   *')
      b = ('*' * (len(a)))
      Utility.combatline(f'\n\n{b:^46}')
      Utility.combatline(f'{a:^46}')
      Utility.combatline(f'{b:^46}')
      Utility.buff_clear(player, enemy)


##### SKILL FUNCTIONS #####


class SkillUse:

    def player_skill(player, enemy):
      count = 1
      for skill in player.skills:
        Utility.combat(f'\n{count}.) {skill.name} | MP Cost: {skill.mpcost}')
        count += 1
      Utility.combat(f'\n{count}.) Return')
      selection = input('\n\n>>> ')
      if int(selection) <= len(player.skills):
        choice = player.skills[(int(selection) - 1)]
        if choice.type == 'attack' and choice.mpcost <= player.mp:
          choice.effect(choice, player, enemy)
        elif choice.type == 'atk_buff' and player.atk_buff == Default and choice.mpcost <= player.mp:
          choice.effect(choice, player, enemy)
        elif choice.type == 'atk_buff' and player.atk_buff != Default:
          Utility.combat('\nYou already have an attack buff. Please make a different selection.')
          Turn.clear_turn()
          Utility.player_combat_prompt(player, enemy)
        elif choice.type == 'def_buff' and player.def_buff == Default and choice.mpcost <= player.mp:
          choice.effect(choice, player, enemy)
        elif choice.type == 'def_buff' and player.def_buff != Default:
          Utility.combat('\nYou already have a defensive buff. Please make a different selection.')
          Turn.clear_turn()
          Utility.player_combat_prompt(player, enemy)
        elif choice.type == 'heal' and choice.mpcost <= player.mp:
          choice.effect(choice, player, enemy)
        elif choice.mpcost > player.mp:
          Utility.combat('\nYou do not have enough mana.')
          Turn.clear_turn()
          Utility.player_combat_prompt(player, enemy)
      elif int(selection) == count:
        Turn.clear_turn()
        Utility.player_combat_prompt(player, enemy)
      else:
        Utility.combat('\nPlease make a valid selection.')
        Turn.clear_turn()
        Utility.player_combat_prompt(player, enemy)

  
    def enemy_skill(enemy, player):

      temp = []
      if enemy.def_buff and enemy.atk_buff == Default:
        for skill in enemy.skills:
          if skill.type == "def_buff" or "atk_buff":
            temp.append(skill)
        selection = random.choice(temp)
        if enemy.mp >= selection.mpcost:
          selection.effect(selection, enemy, player)
        else:
          Utility.attack(enemy, player)
      elif enemy.def_buff == Default and enemy.atk_buff != Default:
        for skill in enemy.skills:
          if skill.type != "atk_buff":
            temp.append(skill)
        selection = random.choice(temp)
        if enemy.mp >= selection.mpcost:
          selection.effect(selection, enemy, player)
        else:
          Utility.attack(enemy, player)
      elif enemy.def_buff != Default and enemy.atk_buff == Default:
        for skill in enemy.skills:
          if skill.type != "def_buff":
            temp.append(skill)
        selection = random.choice(temp)
        if enemy.mp >= selection.mpcost:
          selection.effect(selection, enemy, player)
        else:
          Utility.attack(enemy, player)
      elif enemy.def_buff != Default and enemy.atk_buff != Default:
        for skill in enemy.skills:
          if skill.type != "def_buff" or "atk_buff":
            temp.append(skill)
        selection = random.choice(temp)
        if enemy.mp >= selection.mpcost:
          selection.effect(selection, enemy, player)
        else:
          Utility.attack(enemy, player)
      
     
##### Default #####


class Default:

    name = "default"
    type = "none"
    skillcost = 0
    element = "none"
    mpcost = 0
    duration = 0
    dice = Dice.d_0
    maxbuff = "none"
    effect = "none"
    skilldes = "\nERROR"
    effectdes = "\nERROR"


class Attack:

  def physical_damage(skill, player, enemy):

    player.mp -= skill.mpcost
    buff = enemy.def_buff.dice()
    defense = enemy.blk()
    block = buff + defense
    attackdice = skill.dice() + skill.additionaldamage()
    damage =  attackdice - block
    if damage < 0:
      damage = 0
    Utility.combat(f"\n\n{skill.effectdes}")
    Utility.combat(f'\n\n{player.name} attempts "{skill.name}".')
    enemy.hp -= damage
    if enemy.hp < 0:
        enemy.hp = 0
    Utility.combatline('\n\n'+ '+' + '=' * 44 + '+')
    a = (f"| Skill Roll [ {skill.skilldice} ] = {attackdice}")
    b = (f"| Defense Roll [ {enemy.defense} ] = {defense}")
    c = (f'| Total Damage = {damage}')
    d = (f'| {player.name}')
    e = (f"| Defense Buff [ {enemy.def_buff.maxbuff} ] = {buff}")
    f = (f'| {enemy.name}')
    Utility.combatline(f"{d:<45}|")
    Utility.combatline('|' + '-' * 44 + '|')
    Utility.combatline('|' + ' ' * 44 + '|')
    Utility.combatline(f"{a:<45}|")
    Utility.combatline('|' + ' ' * 44 + '|')
    Utility.combatline('|' + '=' * 44 + '|')
    Utility.combatline(f"{f:<45}|")
    Utility.combatline('|' + '-' * 44 + '|')
    Utility.combatline('|' + ' ' * 44 + '|')
    Utility.combatline(f"{b:<45}|")
    if enemy.def_buff != Default:
      Utility.combatline(f"{e:<45}|")
      Utility.combatline('|' + ' ' * 44 + '|')
    Utility.combatline('|' + '=' * 44 + '|')
    Utility.combatline(f"{c:<45}|")
    Utility.combatline('|' + '=' * 44 + '|')
    HealthBar.DisplayBars(player, enemy)
    if enemy.hp == 0 and enemy.type == "Enemy":
      Utility.enemy_killed(enemy, player)
    elif enemy.hp == 0 and enemy.type == "Player":
      Utility.player_killed(enemy)
    else:
      Utility.buff_check(enemy, player)


  type = "attack"
  effect = physical_damage


class Buff:
  
  def def_buff(skill, player, enemy):

    player.mp -= skill.mpcost
    player.def_buff = skill
    if player.type == "Player":
        Turn.def_turns_passed = 0
    else:
        Turn.def_enemy_turns_passed = 0
    Utility.combat(f"\n{skill.effectdes}")
    Utility.combat(f"\n\n{player.name} raised their {skill.element} by {skill.maxbuff} for {skill.duration} turns.")
    Utility.buff_check(enemy, player)
    

  def atk_buff(skill, player, enemy):

    player.mp -= skill.mpcost
    player.atk_buff = skill
    if player.type == "Player":
        Turn.atk_turns_passed = 0
    else:
        Turn.atk_enemy_turns_passed = 0
    Utility.combat(f"\n{skill.effectdes}")
    Utility.combat(f"\n\n{player.name} raised their {skill.element} by {skill.maxbuff} for {skill.duration} turns.")
    Utility.buff_check(enemy, player)


##### Warrior Abilities #####


class ShieldBash(Attack):

  name = "Shield Bash"
  role = "Warrior"
  skillcost = 5
  element = "bashing"
  mpcost = 4
  dice = Dice.d_8
  skilldice = "1d8"
  additionaldamage = Dice.d_0
  skilldes = "\nAttacks with the player's shield. Does 1d8 damage."
  effectdes = "\nYou throw the weight of your shield into the enemy!\n"


class OverheadSlash(Attack):

  name = "Overhead Slash"
  role = "Warrior"
  skillcost = 6
  element = "slashing"
  mpcost = 5
  dice = Dice.d_10
  skilldice = "1d10"
  additionaldamage = Dice.d_0
  skilldes = "\nA powerful overhead slash. Does 1d10 damage."
  effectdes = "\nYou swing your weapon from overhead!\n"


class Rage(Buff):

  name = "Blinding Rage"
  role = "Warrior"
  type = 'atk_buff'
  skillcost = 4
  element = 'attack'
  mpcost = 4
  duration = 2
  dice = Dice.d_8
  maxbuff = "1d8"
  effect = Buff.atk_buff
  skilldes = "\nYour attack is raised by 1d8 for two turns!"
  effectdes =  "\nYou are filled with rage!"

class Pain(Buff):

  name = "Ignore Pain"
  role = "Warrior"
  type = 'def_buff'
  skillcost = 4
  element = 'defense'
  mpcost = 4
  duration = 2
  dice = Dice.d_6
  maxbuff = "1d6"
  effect = Buff.def_buff
  skilldes = "\nIncreases your defense by 1d6 for two turns."
  effectdes =  "\nYou shrug off the pain!"


##### Barbarian Abilities #####


class Kick(Attack):

  name = "Fierce Kick"
  role = "Barbarian"
  skillcost = 5
  element = "kicking"
  mpcost = 5
  dice = Dice.d_8
  skilldice = "1d8 + 1d2"
  additionaldamage = Dice.d_2
  skilldes = "\nA powerful kick. 1d8 + 1d2 kicking damage."
  effectdes = "\nYou kick with all of your might!\n"


class Flurry(Attack):

  name = "Flurry of Blows"
  role = "Barbarian"
  type = 'attack'
  skillcost = 8
  element = "striking"
  mpcost = 4
  dice = Dice.d_8
  skilldice = "1d8 + 1d2"
  additionaldamage = Dice.d_2
  skilldes = "\nUnleash a flurry of blows for 1d8 + 1d2 damage."
  effectdes = "\nYou unleash a barrage of attacks!\n"


class Anger(Buff):

  name = 'Anger'
  role = "Barbarian"
  type = 'atk_buff'
  skillcost = 4
  element = 'attack'
  mpcost = 4
  duration = 2
  dice = Dice.d_8
  maxbuff = "1d8"
  effect = Buff.atk_buff
  skilldes = "\nYou get angry! Your attack is raised by 1d8 for two turns!"
  effectdes = "\nYou're furious!"


##### Mage Abilities #####


class Fireball(Attack):

  name = "Fireball"
  role = 'Mage'
  type = 'attack'
  skillcost = 6
  element = "fire"
  mpcost = 4
  dice = Dice.d_8
  skilldice = "1d8"
  additionaldamage = Dice.d_0
  skilldes = "\nAttacks with a fireball. Does 1d8 damage."
  effectdes = "\nYou cast a mighty fireball!\n"


class IceWall(Attack):

  name = "Ice Wall"
  role = 'Mage'
  type = 'attack'
  skillcost = 4
  element = "ice"
  mpcost = 3
  dice = Dice.d_6
  skilldice = "1d6 + 1d2"
  additionaldamage = Dice.d_2
  skilldes = "\nAttacks with a sheet of ice. Does 1d6 damage."
  effectdes = "\nA sheet of ice emerges from the staff into the enemy!\n"


class Lightning(Attack):

  name = "Lightning Strike"
  role = 'Mage'
  type = 'attack'
  skillcost = 4
  element = "lightning"
  mpcost = 3
  dice = Dice.d_6
  skilldice = "1d6 + 1d2"
  additionaldamage = Dice.d_2
  skilldes = "\nA lightning strike! Does 1d6 + 1d4 of lightning damage."
  effectdes = "\nA bolt of lightning comes from the heavens!\n"


class Barrier(Buff):

  name = "Magical Barrier"
  role = 'Mage'
  type = 'def_buff'
  skillcost = 6
  element = 'defense'
  mpcost = 6
  duration = 3
  dice = Dice.d_6
  maxbuff = "1d6"
  effect = Buff.def_buff
  skilldes = "\nRaises defense by 1d6 for 3 turns."
  effectdes = "\nYou form a magical barrier around yourself!\n"


##### Rogue Abilities #####


class Backstab(Attack):

  name = "Backstab"
  role = "Rogue"
  type = 'attack'
  skillcost = 8
  element = "critical"
  mpcost = 4
  dice = Dice.d_8
  skilldice = "1d8 + 1d2"
  additionaldamage = Dice.d_2
  skilldes = "\nSneak around to the back of the enemy for 1d8 + 1d2 damage."
  effectdes = "\nYou backstab the enemy!\n"


class TripWire(Attack):

  name = "Trip Wire"
  role = "Rogue"
  type = 'attack'
  skillcost = 4
  element = "critical"
  mpcost = 4
  dice = Dice.d_6
  skilldice = "1d6 + 1d4"
  additionaldamage = Dice.d_4
  skilldes = "\nSet up a trip wire for the enemy. Does 1d6 + 1d4 damage."
  effectdes = "\nThe enemy hits the trip wire!\n"


class Shadows(Buff):

  name = "Hide in Shadows"
  role = "Rogue"
  type = 'def_buff'
  skillcost = 6
  element = 'defense'
  mpcost = 4
  duration = 3
  dice = Dice.d_4
  maxbuff = "1d4"
  effect = Buff.def_buff
  skilldes = "\nRaises defense by 1d4 for 3 turns."
  effectdes = "\nYou hide in shadows!\n"


##### Enemy Abilities #####


class Legshot(Attack):

  name = "Leg Shot"
  role = "Enemy"
  type = 'attack'
  skillcost = 3
  element = "leg"
  mpcost = 4
  dice = Dice.d_8
  skilldice = "1d8"
  additionaldamage = Dice.d_0
  skilldes = "\nA shot to the legs for 1d8 damage."
  effectdes = "\nAim for the legs!\n"


class Aim(Attack):

  name = "Aim for the Head"
  role = "Enemy"
  type = 'attack'
  skillcost = 6
  element = "head"
  mpcost = 6
  dice = Dice.d_10
  skilldice = "1d10"
  additionaldamage = Dice.d_0
  skilldes = "\nA headshot for 1d10 damage."
  effectdes = "\nSteben aims for the head!\n"


class ExitCamp(Buff):

  name = "Exit Camp"
  role = "Enemy"
  type = 'atk_buff'
  skillcost = 6
  element = 'attack'
  mpcost = 4
  duration = 2
  dice = Dice.d_8
  maxbuff = '1d8'
  effect = Buff.atk_buff
  skilldes = "\nExit camps for 1d8 for two turns."
  effectdes = "\nSteven exit camps for an attack buff of 1d8 for two turns!\n"


class Bush(Buff):

  name = "Hide in Bush"
  role = "Enemy"
  type = 'def_buff'
  skillcost = 6
  element = 'defense'
  mpcost = 4
  duration = 2
  dice = Dice.d_8
  maxbuff = '1d8'
  effect = Buff.def_buff
  skilldes = "\nHide in a bush for two turns."
  effectdes = "\nNick hides in a bush!\n"


##### Recovery Skills #####


class Recovery:

  def hp_recovery(skill, player, enemy):
    recovery = skill.dice()
    player.hp += recovery
    if player.hp > player.max_hp:
      player.hp = player.max_hp
    Utility.combat(f"\n\n{skill.effectdes}")
    Utility.combat(f"\n{player.name} recovered {recovery} HP from {skill.name}.\n")
    Utility.buff_check(enemy, player)


  def mp_recovery(player):
    recovery = player.mprecover()
    player.mp += recovery
    b = (f'|  {player.name} recovers {recovery} MP.  |')
    length = len(b)
    a = ('+' * length)
    Utility.combatline(f'\n{a:^46}')
    Utility.combatline(f'{b:^46}')
    Utility.combatline(f'{a:^46}\n')


class HealMinor(Recovery):

    name = "Heal Minor Wounds"
    role = ''
    type = 'heal'
    skillcost = 4
    element = 'healing'
    mpcost = 5
    dice = Dice.d_4
    effect = Recovery.hp_recovery
    skilldes = "\nA minor healing spell. Recovers 1d4 HP on casting."
    effectdes = "\nYou cast heal minor wounds!\n"


class HealMajor(Recovery):

    name = "Heal Major Wounds"
    role = ''
    type = 'heal'
    skillcost = 6
    element = 'healing'
    mpcost = 8
    dice = Dice.d_6
    effect = Recovery.hp_recovery
    skilldes = "\nA major healing spell. Recovers 1d6 HP on casting."
    effectdes = "\nYou cast heal major wounds!\n"


class Bandage(Recovery):

    name = "Bandage Wounds"
    role = ''
    type = 'heal'
    skillcost = 3
    element = 'healing'
    mpcost = 3
    dice = Dice.d_2
    effect = Recovery.hp_recovery
    skilldes = "\nAn attempt to bandage wounds. Recovers 1d2 HP."
    effectdes = "\nYou attempt to bandage your wounds.\n"
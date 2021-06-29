##### Imports #####
import time, sys
from Dice import *
from random import *
from Skills import *
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
      Turn.atk_turns_passed -= 1
      Turn.def_turns_passed -= 1
      Turn.def_enemy_turns_passed -= 1
      Turn.atk_enemy_turns_passed -= 1
      Turn.current_turn -= 1


class Utility:


  def continue_prompt(self):
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
      time.sleep(0.02)
  

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
  

  def def_buff_check(player, enemy):
    
    TextSpeed.instant('\n' * 5)
    if player.type == "Player":
      if player.def_buff.duration != Turn.def_turns_passed and player.def_buff != Default:
        Utility.combat(f"{player.name} has {player.def_buff.duration - Turn.def_turns_passed} turns of \"{player.def_buff.name}\" remaining.")
        Utility.atk_buff_check(player, enemy)
      elif player.def_buff == Default:
        Utility.atk_buff_check(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.def_buff.name}\" has worn off!")
        player.def_buff = Default
        Turn.def_turns_passed = 0
        Utility.atk_buff_check(player, enemy)
    else:
      if player.def_buff.duration != Turn.def_enemy_turns_passed and player.def_buff != Default:
        Utility.combat(f"{player.name} has {player.def_buff.duration - Turn.def_enemy_turns_passed} turns of \"{player.def_buff.name}\" remaining.")
        Utility.enemy_skill_use(player, enemy)
      elif player.def_buff == Default:
        Utility.enemy_skill_use(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.def_buff.name}\" has worn off!")
        player.def_buff = Default
        Turn.def_enemy_turns_passed = 1
        Utility.enemy_skill_use(player, enemy)
  

  def atk_buff_check(player, enemy):

    TextSpeed.instant('\n' * 5)
    if player.type == "Player":
      if player.atk_buff.duration != Turn.atk_turns_passed and player.atk_buff != Default:
        Utility.combat(f"{player.name} has {player.atk_buff.duration - Turn.atk_turns_passed} turns of \"{player.atk_buff.name}\" remaining.")
        Utility.player_combat_prompt(player, enemy)
      elif player.atk_buff == Default:
        Utility.player_combat_prompt(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.atk_buff.name}\" has worn off!")
        player.atk_buff = Default
        Turn.atk_turns_passed = 0
        Utility.player_combat_prompt(player, enemy)
    else:
      if player.atk_buff.duration != Turn.atk_enemy_turns_passed and player.atk_buff != Default:
        Utility.combat(f"{player.name} has {player.atk_buff.duration - Turn.atk_enemy_turns_passed} turns of \"{player.atk_buff.name}\" remaining.")
        Utility.enemy_skill_use(player, enemy)
      elif player.atk_buff == Default:
        Utility.enemy_skill_use(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.atk_buff.name}\" has worn off!")
        player.atk_buff = Default
        Turn.atk_enemy_turns_passed = 1
        Utility.enemy_skill_use(player, enemy)


  def player_combat_prompt(player, enemy):

    this_turn = Turn.current_turn
    Turn.def_turns_passed += 1
    Turn.def_enemy_turns_passed += 1
    Turn.atk_turns_passed += 1
    Turn.atk_enemy_turns_passed += 1
    Turn.turn_count(this_turn)
    Utility.combat(f'\nTurn: {Turn.current_turn}')
    Utility.combat("\n\nDo you (A)ttack or do you use a (S)kill?")
    TextSpeed.fast("\n########################################")
    Utility.combat("\nHP: " + str(player.hp))
    Utility.combat("\nMP: " + str(player.mp))
    if player.def_buff != Default:
      Utility.combat(f"\nBuff: {player.def_buff.name}")
      Utility.combat(f"\nDefense: {player.defense} + {player.def_buff.maxbuff}")
    else:
      Utility.combat(f"\nDefense: {player.defense}")
    if player.atk_buff != Default:
      Utility.combat(f"\nBuff: {player.atk_buff.name}")
      Utility.combat(f"\nAttack: {player.max_attack_str} + {player.atk_buff.maxbuff}")
    else:
      Utility.combat(f"\nAttack: {player.max_attack_str}")
    for skill in player.skills:
      Utility.combat("\nSkill: " + str(skill.name))
    answer = input('\n>>> ')
    if 'a' in answer.lower():
      Utility.attack(player, enemy)
    elif 's' in answer.lower():
      SkillUse.player_skill(player, enemy)
     


  def attack(player, enemy):

    Utility.combat('\n\nYou have chosen to attack!')
    attack = player.atk()
    attackbuff = player.atk_buff.dice()
    if enemy.def_buff != Default:
      enemybuff = enemy.def_buff.dice()
    else:
      enemybuff = 0
    enemyblock = enemy.blk()
    damage = (attack + player.additional_damage + attackbuff) - (enemyblock + enemybuff) if (attack + player.additional_damage + attackbuff) - (enemyblock + enemybuff) > 0 else 0
    enemy.hp -= damage
    if (enemyblock + enemybuff) >= attack:
        finalblock = "all"
    else:
        finalblock = enemyblock + enemybuff
    Utility.combat(f"\n\nYou rolled a {attack + attackbuff} on your damage dice and {enemy.name} blocked {finalblock} of it.\
    \nYou have dealt {damage} points of damage. The enemy has {enemy.hp} hit points remaining.") if enemy.hp > 0 else 0
    if enemy.hp <= 0:
      Utility.combat(f"\n\nYou rolled a {attack + attackbuff} on your damage dice and {enemy.name} blocked {finalblock} of it.\
      \nYou have dealt {damage} points of damage. The enemy has 0 hit points remaining.")
      player.def_buff == Default
      Recovery.mp_recovery(player)
      Utility.enemy_killed(enemy, player)
    else:
      Recovery.mp_recovery(player)
      Utility.def_buff_check(enemy, player)


  def enemy_attack(enemy, player):
    
      Utility.combat(f'\n\n{enemy.name} attacks!')
      enemyattack = enemy.atk()
      enemyattackbuff = enemy.atk_buff.dice()
      playerbuff = player.def_buff.dice()
      playerblock = player.blk()
      damage = (enemyattack + enemy.additional_damage + enemyattackbuff) - (playerblock + playerbuff) if (enemyattack + enemy.additional_damage + enemyattackbuff) - (playerblock + playerbuff) > 0 else 0
      player.hp -= damage
      if (playerblock + playerbuff) >= enemyattack:
        finalblock = "all"
      else:
          finalblock = playerblock + playerbuff
      Utility.combat(f'\n\n{enemy.name} rolled a {enemyattack + enemyattackbuff} on their damage dice and you blocked {finalblock} of it.\
      \nThey have dealt {damage} points of damage. You have {player.hp} hit points remaining.') if player.hp > 0 else 0
      if player.hp <= 0:
        Utility.combat(f'\n\n{enemy.name} rolled a {enemyattack} on their damage dice and you blocked {finalblock} of it.\
        \nThey have dealt {damage} points of damage. You have 0 hit points remaining.')
        Utility.player_killed(player)
      elif player.hp > 0:
        Recovery.mp_recovery(enemy)
        Utility.def_buff_check(player, enemy)


  def enemy_skill_use(enemy, player):

      for skill in enemy.skills:
        if enemy.atk_buff == Default and enemy.def_buff == Default:
          choice = random.choice(enemy.skills)
          choice.effect()

         
 
  def player_killed(player):

    if player.hp <= 0:
      Utility.combat('\n\nYou have been killed!\n')
      Utility.gameOver()
  

  def buff_clear(player, enemy):

    if player.def_buff != Default and player.atk_buff != Default:
      Turn.def_turns_passed = player.def_buff.duration
      Turn.atk_turns_passed = player.atk_buff.duration
      player.def_buff = Default
      player.atk_buff = Default
      enemy.def_buff = Default
      enemy.atk_buff = Default
      Turn.def_turns_passed = 0
      Turn.def_enemy_turns_passed = 0
      Turn.atk_turns_passed = 0
      Turn.atk_enemy_turns_passed = 0
    elif player.def_buff != Default:
      Turn.def_turns_passed = player.def_buff.duration
      player.def_buff = Default
      enemy.def_buff = Default
      Turn.def_turns_passed = 0
      Turn.def_enemy_turns_passed = 0
    elif player.atk_buff != Default:
      Turn.atk_turns_passed = player.atk_buff.duration
      player.atk_buff = Default
      enemy.atk_buff = Default
      Turn.atk_turns_passed = 0
      Turn.atk_enemy_turns_passed = 0
    else:
      None


  def enemy_killed(enemy, player):

    if enemy.hp <= 0:
      Utility.combat(f'\n\n{enemy.name} has been killed!\n')
      Utility.buff_clear(player, enemy)


  def initiative():

    player_init = Dice.d_10()
    enemy_init = Dice.d_10()
    Utility.combat('\nYou both roll for initiative!')
    Utility.combat("\n\nYou rolled a " + str(player_init) + " and the enemy rolled a " + str(enemy_init) + ".")
    if player_init > enemy_init:
      Utility.combat('\n\nYou rolled higher and get the first attack!\n')
      continue_prompt = input("\n\n>>> Hit enter to continue")
      if '' in continue_prompt:
        return True
    if player_init == enemy_init:
      Utility.combat('\n\nYou both tied. The enemy gets to attack first!')
      continue_prompt = input("\n\n>>> Hit enter to continue")
      if '' in continue_prompt:
        return False
    else:
      Utility.combat('\n\nThe enemy rolled higher and gets the first attack!\n')
      continue_prompt = input("\n\n>>> Hit enter to continue")
      if '' in continue_prompt:
        return False
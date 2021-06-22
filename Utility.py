import time, sys
from Dice import *
from random import *
from Player import *

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
      if player.def_buff['duration'] != Turn.def_turns_passed and player.def_buff['name'] != "default":
        Utility.combat(f"{player.name} has {player.def_buff['duration'] - Turn.def_turns_passed} turns of \"{player.def_buff['name']}\" remaining.")
        Utility.atk_buff_check(player, enemy)
      elif player.def_buff == BuffSkill.default:
        Utility.atk_buff_check(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.def_buff['name']}\" has worn off!")
        player.def_buff = BuffSkill.default
        Turn.def_turns_passed = 0
        Utility.atk_buff_check(player, enemy)
    else:
      if player.def_buff['duration'] != Turn.def_enemy_turns_passed and player.def_buff['name'] != "default":
        Utility.combat(f"{player.name} has {player.def_buff['duration'] - Turn.def_enemy_turns_passed} turns of \"{player.def_buff['name']}\" remaining.")
        Utility.enemy_skill_use(player, enemy)
      elif player.def_buff == BuffSkill.default:
        Utility.enemy_skill_use(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.def_buff['name']}\" has worn off!")
        player.def_buff = BuffSkill.default
        Turn.def_enemy_turns_passed = 1
        Utility.enemy_skill_use(player, enemy)
  

  def atk_buff_check(player, enemy):

    TextSpeed.instant('\n' * 5)
    if player.type == "Player":
      if player.atk_buff['duration'] != Turn.atk_turns_passed and player.atk_buff['name'] != "default":
        Utility.combat(f"{player.name} has {player.atk_buff['duration'] - Turn.atk_turns_passed} turns of \"{player.atk_buff['name']}\" remaining.")
        Utility.player_combat_prompt(player, enemy)
      elif player.atk_buff == BuffSkill.default:
        Utility.player_combat_prompt(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.atk_buff['name']}\" has worn off!")
        player.atk_buff = BuffSkill.default
        Turn.atk_turns_passed = 0
        Utility.player_combat_prompt(player, enemy)
    else:
      if player.atk_buff['duration'] != Turn.atk_enemy_turns_passed and player.atk_buff['name'] != "default":
        Utility.combat(f"{player.name} has {player.atk_buff['duration'] - Turn.atk_enemy_turns_passed} turns of \"{player.atk_buff['name']}\" remaining.")
        Utility.enemy_skill_use(player, enemy)
      elif player.atk_buff == BuffSkill.default:
        Utility.enemy_skill_use(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.atk_buff['name']}\" has worn off!")
        player.atk_buff = BuffSkill.default
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
    if player.def_buff['name'] != 'default':
      Utility.combat(f"\nBuff: {player.def_buff['name']}")
      Utility.combat(f"\nDefense: {player.defense} + {player.def_buff['maxbuff']}")
    else:
      Utility.combat(f"\nDefense: {player.defense}")
    if player.atk_buff['name'] != 'default':
      Utility.combat(f"\nBuff: {player.atk_buff['name']}")
      Utility.combat(f"\nAttack: {player.max_attack_str} + {player.atk_buff['maxbuff']}")
    else:
      Utility.combat(f"\nAttack: {player.max_attack_str}")
    skillset = "{0}, {1}".format(player.skill1['name'], player.skill2['name'])
    Utility.combat("\nSkills: " + str(skillset))
    answer = input('\n>>> ')
    if 'a' in answer.lower():
      Utility.attack(player, enemy)
    elif 's' in answer.lower():
      Utility.combat('\n(1) {0} or (2) {1}?'.format(player.skill1['name'], player.skill2['name']))
      Utility.combat('\n\nSkill: %s' % player.skill1['name'])
      Utility.combat('\nMana Cost: %s' % player.skill1['mpcost'])
      Utility.combat('\nEffect: %s' % player.skill1['skilldes'])
      Utility.combat('\n\nSkill: %s' % player.skill2['name'])
      Utility.combat('\nMana Cost: %s' % player.skill2['mpcost'])
      Utility.combat('\nEffect: %s' % player.skill2['skilldes'])
      answer = input("\n\n>>> ")
      if str(1) in answer:
        if player.mp >= player.skill1['mpcost'] and player.atk_buff['element'] == 'none' and player.def_buff['element'] == 'none':
          SkillUse.skill1(player, enemy)
        elif player.mp >= player.skill1['mpcost'] and player.atk_buff['element'] != 'none' and player.skill1['type'] != 'atk_buff':
          SkillUse.skill1(player, enemy)
        elif player.mp >= player.skill1['mpcost'] and player.def_buff['element'] != 'none' and player.skill1['type'] != 'def_buff':
          SkillUse.skill1(player, enemy)
        elif player.mp >= player.skill1['mpcost'] and player.def_buff['element'] == 'none' and player.skill1['type'] == 'def_buff':
          SkillUse.skill1(player, enemy)
        elif player.mp >= player.skill1['mpcost'] and player.atk_buff['element'] == 'none' and player.skill1['type'] == 'atk_buff':
          SkillUse.skill1(player, enemy)
        elif player.mp >= player.skill1['mpcost'] and player.atk_buff['element'] != 'none' and player.skill1['type'] == 'def_buff':
          SkillUse.skill1(player, enemy)
        else:
          if player.mp < player.skill1['mpcost']:
            Utility.combat(f"\nYou do not have enough mana.")
          elif player.skill1['element'] != 'none' and player.skill1['type'] == 'def_buff':
            Utility.combat(f"\nYou are already using {player.skill1['name']}.")
          elif player.skill1['element'] != 'none' and player.skill1['type'] == 'atk_buff':
            Utility.combat(f"\nYou are already using {player.skill1['name']}.")
          Turn.clear_turn()
          Utility.player_combat_prompt(player, enemy)
      elif str(2) in answer:
        if player.mp >= player.skill2['mpcost'] and player.atk_buff['element'] == 'none' and player.def_buff['element'] == 'none':
          SkillUse.skill2(player, enemy)
        elif player.mp >= player.skill2['mpcost'] and player.atk_buff['element'] != 'none' and player.skill2['type'] != 'atk_buff':
          SkillUse.skill2(player, enemy)
        elif player.mp >= player.skill2['mpcost'] and player.def_buff['element'] != 'none' and player.skill2['type'] != 'def_buff':
          SkillUse.skill2(player, enemy)
        elif player.mp >= player.skill2['mpcost'] and player.def_buff['element'] == 'none' and player.skill2['type'] == 'def_buff':
          SkillUse.skill2(player, enemy)
        elif player.mp >= player.skill2['mpcost'] and player.atk_buff['element'] == 'none' and player.skill2['type'] == 'atk_buff':
          SkillUse.skill2(player, enemy)
        elif player.mp >= player.skill2['mpcost'] and player.atk_buff['element'] != 'none' and player.skill2['type'] == 'def_buff':
          SkillUse.skill2(player, enemy)
        else:
          if player.mp < player.skill2['mpcost']:
            Utility.combat(f"\nYou do not have enough mana.")
          elif player.skill2['element'] != 'none' and player.skill2['type'] == 'def_buff':
            Utility.combat(f"\nYou are already using {player.skill2['name']}.")
          elif player.skill2['element'] != 'none' and player.skill2['type'] == 'atk_buff':
            Utility.combat(f"\nYou are already using {player.skill2['name']}.")
          Turn.clear_turn()
          Utility.player_combat_prompt(player, enemy)
      else:
        Turn.clear_turn()
        Utility.combat('\nYou must choose a skill.')
        Utility.player_combat_prompt(player, enemy)


  def attack(player, enemy):

    Utility.combat('\n\nYou have chosen to attack!')
    attack = player.atk()
    attackbuff = player.atk_buff['dice']()
    if enemy.def_buff['element'] == "defense":
      enemybuff = enemy.def_buff['dice']()
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
      player.def_buff == BuffSkill.default
      RecoverySkill.mp_recovery(player)
      Utility.enemy_killed(enemy, player)
    else:
      RecoverySkill.mp_recovery(player)
      Utility.def_buff_check(enemy, player)


  def enemy_attack(enemy, player):
    
      Utility.combat(f'\n\n{enemy.name} attacks!')
      enemyattack = enemy.atk()
      enemyattackbuff = enemy.atk_buff['dice']()
      playerbuff = player.def_buff['dice']()
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
        RecoverySkill.mp_recovery(enemy)
        Utility.def_buff_check(player, enemy)


  def enemy_skill_use(enemy, player):

      if enemy.mp >= enemy.skill1['mpcost'] and enemy.mp >= enemy.skill2['mpcost'] and enemy.def_buff['element'] == 'none' and enemy.atk_buff['element'] == 'none':
        RandSkill1 = SkillUse.enemy_skill1
        RandSkill2 = SkillUse.enemy_skill2
        selection = random.choice((RandSkill1, RandSkill2))
        if selection == RandSkill1 and enemy.skill1['type'] == 'def_buff' or 'atk_buff':
          SkillUse.enemy_skill1(enemy, player)
        elif selection == RandSkill1 and enemy.skill2['type'] == 'def_buff' or 'atk_buff':
          SkillUse.enemy_skill2(enemy, player)
        elif selection == RandSkill2 and enemy.skill1['type'] == 'def_buff' or 'atk_buff':
          SkillUse.enemy_skill1(enemy, player)
        elif selection == RandSkill2 and enemy.skill2['type'] == 'def_buff' or 'atk_buff':
          SkillUse.enemy_skill2(enemy, player)
        elif selection == RandSkill1 and enemy.skill1['type'] != 'def_buff' or 'atk_buff':
          SkillUse.enemy_skill1(enemy, player)
        elif selection == RandSkill2 and enemy.skill2['type'] != 'def_buff' or 'atk_buff':
          SkillUse.enemy_skill2(enemy, player)
        else:
          Utility.enemy_attack(enemy, player)
      elif enemy.mp >= enemy.skill1['mpcost'] and enemy.def_buff['element'] == 'none' and enemy.atk_buff['element'] == 'none':
            SkillUse.enemy_skill1(enemy, player)
      elif enemy.mp >= enemy.skill2['mpcost'] and enemy.def_buff['element'] == 'none' and enemy.atk_buff['element'] == 'none':
            SkillUse.enemy_skill2(enemy, player)
      elif enemy.mp >= enemy.skill1['mpcost'] and enemy.def_buff['element'] != 'none' and enemy.atk_buff['element'] != 'none':
            SkillUse.enemy_skill1(enemy, player)
      elif enemy.mp >= enemy.skill2['mpcost'] and enemy.def_buff['element'] != 'none' and enemy.atk_buff['element'] != 'none':
            SkillUse.enemy_skill2(enemy, player)
      elif enemy.mp >= enemy.skill1['mpcost'] and enemy.def_buff['element'] == 'none' and enemy.atk_buff['element'] != 'none':
            SkillUse.enemy_skill1(enemy, player)
      elif enemy.mp >= enemy.skill2['mpcost'] and enemy.def_buff['element'] == 'none' and enemy.atk_buff['element'] != 'none':
            SkillUse.enemy_skill2(enemy, player)
      else:
            Utility.enemy_attack(enemy, player)

 
  def player_killed(player):

    if player.hp <= 0:
      Utility.combat('\n\nYou have been killed!\n')
      Utility.gameOver()
  

  def buff_clear(player, enemy):

    if player.def_buff['element'] != 'none' and player.atk_buff['element'] != 'none':
      Turn.def_turns_passed = player.def_buff['duration']
      Turn.atk_turns_passed = player.atk_buff['duration']
      player.def_buff = BuffSkill.default
      player.atk_buff = BuffSkill.default
      enemy.def_buff = BuffSkill.default
      enemy.atk_buff = BuffSkill.default
      Turn.def_turns_passed = 0
      Turn.def_enemy_turns_passed = 0
      Turn.atk_turns_passed = 0
      Turn.atk_enemy_turns_passed = 0
    elif player.def_buff['element'] != 'none':
      Turn.def_turns_passed = player.def_buff['duration']
      player.def_buff = BuffSkill.default
      enemy.def_buff = BuffSkill.default
      Turn.def_turns_passed = 0
      Turn.def_enemy_turns_passed = 0
    elif player.atk_buff['element'] != 'none':
      Turn.atk_turns_passed = player.atk_buff['duration']
      player.atk_buff = BuffSkill.default
      enemy.atk_buff = BuffSkill.default
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


class SkillUse:


    def skill1(player, enemy):

        skill = player.skill1
        player.skill1['effectdes']
        print('\n')
        player.skill1['effect'](skill, player, enemy)
        Utility.combat(f"\nThis action cost {player.name} {player.skill1['mpcost']} mana.")
        player.mp -= player.skill1['mpcost']
        Utility.combat(f"\n{player.name} has {player.mp} MP remaining.")
        if enemy.hp <= 0:
          Utility.enemy_killed(enemy, player)
        else:
          Utility.def_buff_check(enemy, player)


    def skill2(player, enemy):

        skill = player.skill2
        player.skill2['effectdes']
        player.skill2['effect'](skill, player, enemy)
        Utility.combat(f"\nThis action cost {player.name} {player.skill2['mpcost']} mana.")
        player.mp -= player.skill2['mpcost']
        Utility.combat(f"\n{player.name} has {player.mp} MP remaining.")
        if enemy.hp <= 0:
          Utility.enemy_killed(enemy, player)
        else:
          Utility.def_buff_check(enemy, player)


    def enemy_skill1(enemy, player):

        skill = enemy.skill1
        enemy.skill1['effectdes']
        enemy.skill1['effect'](skill, enemy, player)
        Utility.combat(f"\nThis action cost {enemy.name} {enemy.skill1['mpcost']} mana.")
        enemy.mp -= enemy.skill1['mpcost']
        Utility.combat(f"\n{enemy.name} has {enemy.mp} MP remaining.")
        if player.hp <= 0:
          Utility.player_killed(player)
        else:
          Utility.def_buff_check(player, enemy)
    

    def enemy_skill2(enemy, player):

        skill = enemy.skill2
        enemy.skill2['effectdes']
        enemy.skill2['effect'](skill, enemy, player)
        Utility.combat(f"\nThis action cost {enemy.name} {enemy.skill2['mpcost']} mana.")
        enemy.mp -= enemy.skill2['mpcost']
        Utility.combat(f"\n{enemy.name} has {enemy.mp} MP remaining.")
        if player.hp <= 0:
          player.def_buff == BuffSkill.default
          Utility.player_killed(player)
        else:
          Utility.def_buff_check(player, enemy)


class RecoverySkill:


  def mp_recovery(player):
        recovery = player.mprecover()
        player.mp += recovery
        Utility.combat(f'\n{player.name} naturally recovered {recovery} MP this turn.\n\n')

    
  def hp_recovery(skill, player, enemy):
        recovery = skill['dice']()
        player.hp += recovery
        Utility.combat(f"\n\n{skill['effectdes']}")
        Utility.combat(f"\n{player.name} recovered {recovery} HP from {skill['name']}.")
        enemy == False

  
  heal_minor = {
    'name': 'Heal Minor Wounds',
    'type': 'heal',
    'skillcost': 4,
    'element': 'healing',
    'mpcost': 5,
    'dice': Dice.d_4,
    'effect': hp_recovery,
    'skilldes': "\nA minor healing spell. Recovers 1d4 HP on casting.",
    'effectdes': "\nYou cast heal minor wounds!\n"
  }

  heal_major = {
    'name': 'Heal Major Wounds',
    'type': 'heal',
    'skillcost': 6,
    'element': 'healing',
    'mpcost': 8,
    'dice': Dice.d_6,
    'effect': hp_recovery,
    'skilldes': "\nA major healing spell. Recovers 1d6 HP on casting.",
    'effectdes': "\nYou cast heal major wounds!\n"
  }

  bandage = {
    'name': 'Bandage Wounds',
    'type': 'heal',
    'skillcost': 3,
    'element': 'healing',
    'mpcost': 3,
    'dice': Dice.d_2,
    'effect': hp_recovery,
    'skilldes': "\nAn attempt to bandage wounds. Recovers 1d2 HP.",
    'effectdes': "\nYou attempt to bandage your wounds.\n"
  }

  recovery_list = {
    1: heal_minor,
    2: heal_major,
    3: bandage
  }


class AttackSkill:

    
    def physical_damage(skill, player, enemy):

      block = enemy.blk() + enemy.def_buff['dice']()
      damage = (skill['dice']() + skill['additionaldamage']()) - block
      if damage > 0:
        enemy.hp -= damage
        Utility.combat(f"\n\n{skill['effectdes']}")
        Utility.combat(f"\n\n{player.name} has done {damage} points of {skill['element']} damage to {enemy.name}.")
      else:
        damage = 0
        Utility.combat(f"\n\n{skill['effectdes']}")
        Utility.combat(f"\n{player.name} has done {damage} points of {skill['element']} damage to {enemy.name}.")

  ### Warrior Skills ###

    shield_bash = {
      'name': "Shield Bash",
      'type': 'attack',
      'skillcost': 5,
      'element': "bashing",
      'mpcost': 4,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nAttacks with the player's shield. Does 1d8 damage.",
      'effectdes': "\nYou throw the weight of your shield into the enemy!\n"
    }


    overhead_slash = {
      'name': "Overhead Slash",
      'type': 'attack',
      'skillcost': 6,
      'element': "slashing",
      'mpcost': 5,
      'dice': Dice.d_10,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nA powerful overhead slash. Does 1d10 damage.",
      'effectdes': "\nYou swing your weapon from overhead!\n"
    }
    
    ### Barbarian Skills ###

    kick = {
      'name': "Fierce Kick",
      'type': 'attack',
      'skillcost': 5,
      'element': "kicking",
      'mpcost': 5,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_2,
      'effect': physical_damage,
      'skilldes': "\nA powerful kick. 1d8 + 1d2 kicking damage.",
      'effectdes': "\nYou kick with all of your might!\n"
    }

    flurry = {
      'name': "Flurry of Blows",
      'type': 'attack',
      'skillcost': 8,
      'element': "striking",
      'mpcost': 4,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_2,
      'effect': physical_damage,
      'skilldes': "\nUnleash a flurry of blows for 1d8 + 1d2 damage.",
      'effectdes': "\nYou unleash a barrage of attacks!\n"
    }

  ### Mage Skills ###

    fireball = {
      'name': "Fireball",
      'type': 'magic',
      'skillcost': 6,
      'element': "fire",
      'mpcost': 3,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nAttacks with a fireball. Does 1d8 damage.",
      'effectdes': "\nYou cast a mighty fireball!\n"
    }


    icewall = {
      'name': "Ice Wall",
      'type': 'magic',
      'skillcost': 4,
      'element': "ice",
      'mpcost': 2,
      'dice': Dice.d_6,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nAttacks with a sheet of ice. Does 1d6 damage.",
      'effectdes': "\nA sheet of ice emerges from the staff into the enemy!\n"
    }


    lightning = {
      'name': "Lightning Strike",
      'type': 'magic',
      'skillcost': 4,
      'element': "lightning",
      'mpcost': 3,
      'dice': Dice.d_6,
      'additionaldamage': Dice.d_4,
      'effect': physical_damage,
      'skilldes': "\nA lightning strike! Does 1d6 + 1d4 of lightning damage.",
      'effectdes': "\nA bolt of lightning comes from the heavens!\n"
    }

  ### Rogue Skills ###

    backstab = {
      'name': "Backstab",
      'type': 'attack',
      'skillcost': 8,
      'element': "critical",
      'mpcost': 5,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_2,
      'effect': physical_damage,
      'skilldes': "\nSneak around to the back of the enemy for 1d8 + 1d2 damage.",
      'effectdes': "\nYou backstab the enemy!\n"
    }


    tripwire = {
      'name': "Trip Wire",
      'type': 'attack',
      'skillcost': 4,
      'element': "critical",
      'mpcost': 4,
      'dice': Dice.d_6,
      'additionaldamage': Dice.d_4,
      'effect': physical_damage,
      'skilldes': "\nSet up a trip wire for the enemy. Does 1d6 + 1d4 damage.",
      'effectdes': "\nThe enemy hits the trip wire!\n"
    }

  ### Enemy Skills ##
  
    legshot = {
      'name': "Leg Shot",
      'type': 'attack',
      'skillcost': 3,
      'element': "leg",
      'mpcost': 3,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nA shot to the legs for 1d8 damage.",
      'effectdes': "\nAim for the legs!\n"
    }


    aim = {
      'name': "Aim for the Head",
      'type': 'attack',
      'skillcost': 6,
      'element': "head",
      'mpcost': 6,
      'dice': Dice.d_10,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nA shot to the legs for 1d8 damage.",
      'effectdes': "\nSteben aims for the head!\n"
    }



    warrior_attack_skill_list = {
      1: overhead_slash,
      2: shield_bash,
    }


    rogue_attack_skill_list = {
      1: backstab,
      3: tripwire
    }


    mage_attack_skill_list = {
      1: fireball,
      2: icewall,
      3: lightning
    }


    barb_attack_skill_list = {
      1: flurry,
      3: kick
    }


class BuffSkill:


  def def_buff(skill, player, enemy):

    player.def_buff = skill
    if player.type == "Player":
      Turn.def_turns_passed = 1
    else:
      Turn.def_enemy_turns_passed = 1
    Utility.combat(f"\n{player.def_buff['effectdes']}")
    Utility.combat(f"\n{player.name} raised their {player.def_buff['element']} by {player.def_buff['maxbuff']}.")
    enemy == False
  

  def atk_buff(skill, player, enemy):

    player.atk_buff = skill
    if player.type == "Player":
      Turn.atk_turns_passed = 1
    else:
      Turn.atk_enemy_turns_passed = 1
    Utility.combat(f"\n{player.atk_buff['effectdes']}")
    Utility.combat(f"\n{player.name} raised their {player.atk_buff['element']} by {player.atk_buff['maxbuff']}.")
    enemy == False
  

  default = {
    'name': "default",
    'type': 'none',
    'skillcost': 0,
    'element': 'none',
    'mpcost': 0,
    'duration': 0,
    'dice': Dice.d_0,
    'maxbuff': 'none',
    'effect': 'none',
    'skilldes': "\nERROR",
    'effectdes': "\nERROR"
  }


  shadows = {
      'name': "Hide in Shadows",
      'type': 'def_buff',
      'skillcost': 6,
      'element': 'defense',
      'mpcost': 5,
      'duration': 3,
      'dice': Dice.d_4,
      'maxbuff': "1d4",
      'effect': def_buff,
      'skilldes': "\nRaises defense by 1d4 for 3 turns.",
      'effectdes': "\nYou hide in shadows!\n"
    }

  barrier = {
      'name': "Magical Barrier",
      'type': 'def_buff',
      'skillcost': 6,
      'element': 'defense',
      'mpcost': 6,
      'duration': 3,
      'dice': Dice.d_6,
      'maxbuff': "1d6",
      'effect': def_buff,
      'skilldes': "\nRaises defense by 1d6 for 3 turns.",
      'effectdes': "\nYou hide in shadows!\n"
  }

  bush = {
      'name': "Hide in a Bush",
      'type': 'def_buff',
      'skillcost': 4,
      'element': 'defense',
      'mpcost': 4,
      'duration': 3,
      'dice': Dice.d_4,
      'maxbuff': "1d4",
      'effect': def_buff,
      'skilldes': "\nHide in a bush! Defense raises by 1d4 for two turns.",
      'effectdes': "\nThe enemy hides in a bush!\n"
  }


  rage = {
    'name': "Blinding Rage",
    'type': 'atk_buff',
    'skillcost': 4,
    'element': 'attack',
    'mpcost': 4,
    'duration': 3,
    'dice': Dice.d_8,
    'maxbuff': "1d8",
    'effect': atk_buff,
    'skilldes': "\nYou rage out! Your attack is raised by 1d8 for two turns!",
    'effectdes': "\nYou rage out!"
  }

  exit_camp = {
      'name': "Exit Camp",
      'type': 'atk_buff',
      'skillcost': 6,
      'element': 'attack',
      'mpcost': 4,
      'duration': 2,
      'dice': Dice.d_8,
      'maxbuff': '1d8',
      'effect': atk_buff,
      'skilldes': "\nExit camps for 1d8 for two turns.",
      'effectdes': "\nSteven exit camps for an attack buff of 1d8 for two turns!\n"
    }

  buff_skill_list = {
    1: shadows,
    2: rage,
    3: barrier
  }
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
      time.sleep(0.04)

  @staticmethod
  def fast(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.0000000000000000000000000000000001)
  
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

  def turn_count(turn):
    turn += 1
    Turn.current_turn = turn

class Utility:
  
  @staticmethod
  def story(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.04)

  @staticmethod
  def menu(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.0000000000000000000000000000000001)
  
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
  

  def player_combat_prompt(player, enemy):

    print('\n' * 5)
    this_turn = Turn.current_turn
    Turn.turn_count(this_turn)
    Utility.combat(f'\nTurn: {Turn.current_turn}')
    Utility.combat("\n\nDo you (A)ttack or do you use a (S)kill?")
    TextSpeed.fast("\n########################################")
    Utility.combat("\n\nYou have:")
    Utility.combat("\nHP: " + str(player.hp))
    Utility.combat("\nMP: " + str(player.mp))
    skillset = "{0}, {1}".format(player.skill1['name'], player.skill2['name'])
    Utility.combat("\nSkills: " + str(skillset))
    answer = input('\n>>> ')
    if 'a' in answer.lower():
      Utility.attack(player, enemy)
    elif 's' in answer.lower():
      Utility.combat('\nDo you want to use (1) {0} or (2) {1}?'.format(player.skill1['name'], player.skill2['name']))
      Utility.combat('\n\nSkill: %s' % player.skill1['name'])
      Utility.combat('\nMana Cost: %s' % player.skill1['mpcost'])
      Utility.combat('\nEffect: %s' % player.skill1['skilldes'])
      Utility.combat('\n\nSkill: %s' % player.skill2['name'])
      Utility.combat('\nMana Cost: %s' % player.skill2['mpcost'])
      Utility.combat('\nEffect: %s' % player.skill2['skilldes'])
      answer = input("\n\n>>> ")
      if str(1) in answer:
        if player.mp >= player.skill1['mpcost']:
          SkillUse.skill1(player, enemy)
        else:
          Utility.combat('\nYou do not have enough mana.')
          Utility.player_combat_prompt(player, enemy)
      elif str(2) in answer:
        if player.mp >= player.skill2['mpcost']:
          SkillUse.skill2(player, enemy)
        else:
          Utility.combat('\nYou do not have enough mana.')
          Utility.player_combat_prompt(player, enemy)
      else:
        Utility.combat('\nYou must select a skill.')
        Utility.player_combat_prompt(player, enemy)
    else:
      Utility.player_combat_prompt(player, enemy)

  def attack(player, enemy):
    Utility.combat('\n\nYou have chosen to attack!')
    attack = player.atk()
    enemyblock = enemy.blk()
    damage = (attack + player.additional_damage) - enemyblock if (attack + player.additional_damage) - enemyblock > 0 else 0
    enemy.hp -= damage
    Utility.combat(f"\n\nYou rolled a {attack} on your damage dice and {enemy.name} blocked {enemyblock} of it.\
    \nYou have dealt {damage} points of damage. The enemy has {enemy.hp} hit points remaining.") if enemy.hp > 0 else 0
    if enemy.hp <= 0:
      Utility.combat(f"\n\nYou rolled a {attack} on your damage dice and {enemy.name} blocked {enemyblock} of it.\
      \nYou have dealt {damage} points of damage. The enemy has 0 hit points remaining.")
      RecoverySkill.mp_recovery(player)
      Utility.enemy_killed(enemy)
    elif enemy.hp > 0:
      RecoverySkill.mp_recovery(player)
      Utility.enemy_attack(enemy, player)

  def enemy_attack(enemy, player):
    if enemy.mp >= enemy.skill1['mpcost'] and enemy.mp >= enemy.skill2['mpcost']:
      RandSkill1 = SkillUse.enemy_skill1
      RandSkill2 = SkillUse.enemy_skill2
      selection = random.choice((RandSkill1, RandSkill2))
      if selection == RandSkill1:
        SkillUse.enemy_skill1(enemy, player)
      elif selection == RandSkill2:
        SkillUse.enemy_skill2(enemy, player)
    elif enemy.mp >= enemy.skill1['mpcost']:
      SkillUse.enemy_skill1(enemy, player)
    elif enemy.mp >= enemy.skill2['mpcost']:
      SkillUse.enemy_skill2(enemy, player)
    else:
      Utility.combat(f'\n\n{enemy.name} attacks!')
      enemyattack = enemy.atk()
      playerblock = player.blk()
      damage = (enemyattack + enemy.additional_damage) - playerblock if (enemyattack + enemy.additional_damage) - playerblock > 0 else 0
      player.hp -= damage
      Utility.combat(f'\n\n{enemy.name} rolled a {enemyattack} on their damage dice and you blocked {playerblock} of it.\
      \nThey have dealt {damage} points of damage. You have {player.hp} hit points remaining.') if player.hp > 0 else 0
      if player.hp <= 0:
        Utility.combat(f'\n\n{enemy.name} rolled a {enemyattack} on their damage dice and you blocked {playerblock} of it.\
        \nThey have dealt {damage} points of damage. You have 0 hit points remaining.')
        Utility.player_killed(player)
      elif player.hp > 0:
        RecoverySkill.mp_recovery(enemy)
        Utility.player_combat_prompt(player, enemy)

  def player_killed(player):
    if player.hp <= 0:
      Utility.combat('\nYou have been killed!')
      Utility.gameOver()

  def enemy_killed(enemy):
    if enemy.hp <= 0:
      Utility.combat(f'\n{enemy.name} has been killed!')

  def initiative():
    player_init = Dice.d_10()
    enemy_init = Dice.d_10()
    Utility.combat('\nYou both roll for initiative!')
    Utility.combat("\n\nYou rolled a " + str(player_init) + " and the enemy rolled a " + str(enemy_init) + ".")
    if player_init > enemy_init:
      Utility.combat('\n\nYou rolled higher and get the first attack!\n')
      return True
    if player_init == enemy_init:
      Utility.combat('\n\nYou both tied. The enemy gets to attack first!')
    else:
      Utility.combat('\n\nThe enemy rolled higher and gets the first attack!\n')
      return False


class SkillUse:

    def skill1(player, enemy):
        skill = player.skill1
        player.skill1['effectdes']
        player.skill1['effect'](skill, player, enemy)
        Utility.combat(f"\nThis action cost {player.name} {player.skill1['mpcost']} mana.")
        player.mp -= player.skill1['mpcost']
        Utility.combat(f"\n{player.name} has {player.mp} MP remaining.")
        if enemy.hp <= 0:
          Utility.enemy_killed(enemy)
        else:
          Utility.enemy_attack(enemy, player)

    def skill2(player, enemy):
        skill = player.skill2
        player.skill2['effectdes']
        player.skill2['effect'](skill, player, enemy)
        Utility.combat(f"\nThis action cost {player.name} {player.skill2['mpcost']} mana.")
        player.mp -= player.skill2['mpcost']
        Utility.combat(f"\n{player.name} has {player.mp} MP remaining.")
        if enemy.hp <= 0:
          Utility.enemy_killed(enemy)
        else:
          Utility.enemy_attack(enemy, player)

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
          Utility.player_combat_prompt(player, enemy)
    
    def enemy_skill2(enemy, player):
        skill = enemy.skill2
        enemy.skill2['effectdes']
        enemy.skill2['effect'](skill, enemy, player)
        Utility.combat(f"\nThis action cost {enemy.name} {enemy.skill2['mpcost']} mana.")
        enemy.mp -= enemy.skill2['mpcost']
        Utility.combat(f"\n{enemy.name} has {enemy.mp} MP remaining.")
        if player.hp <= 0:
          Utility.player_killed(player)
        else:
          Utility.player_combat_prompt(player, enemy)


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
    'element': 'healing',
    'mpcost': 5,
    'dice': Dice.d_4,
    'effect': hp_recovery,
    'skilldes': "\nA minor healing spell. Recovers 1d4 HP on casting.",
    'effectdes': "\nYou cast heal minor wounds!"
  }

  heal_major = {
    'name': 'Heal Major Wounds',
    'element': 'healing',
    'mpcost': 8,
    'dice': Dice.d_6,
    'effect': hp_recovery,
    'skilldes': "\nA major healing spell. Recovers 1d6 HP on casting.",
    'effectdes': "\nYou cast heal major wounds!"
  }

  recovery_list = {
    1: heal_minor,
    2: heal_major
  }
    

class AttackSkill:

    
    def physical_damage(skill, player, enemy):
      block = enemy.blk()
      damage = (skill['dice']() + skill['additionaldamage']()) - block if (skill['dice']() + skill['additionaldamage']()) - block > 0 else 0
      enemy.hp -= damage
      Utility.combat(f"\n\n{skill['effectdes']}")
      Utility.combat(f"\n{player.name} has done {damage} points of {skill['element']} damage to {enemy.name}.")
        

    overhead_slash = {
      'name': "Overhead Slash",
      'element': "slashing",
      'mpcost': 5,
      'dice': Dice.d_10,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nA powerful overhead slash. Does 1d10 damage.",
      'effectdes': "\nYou swing your weapon from overhead!"
    }
    
    shield_bash = {
      'name': "Shield Bash",
      'element': "bashing",
      'mpcost': 4,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nAttacks with the player's shield. Does 1d8 damage.",
      'effectdes': "\nYou throw the weight of your shield into the enemy!"
    }

    fireball = {
      'name': "Fireball",
      'element': "fire",
      'mpcost': 3,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nAttacks with a fireball. Does 1d8 damage.",
      'effectdes': "\nYou cast a mighty fireball from your staff!"
    }

    icewall = {
      'name': "Ice Wall",
      'element': "ice",
      'mpcost': 2,
      'dice': Dice.d_6,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nAttacks with a sheet of ice. Does 1d6 damage.",
      'effectdes': "\nA sheet of ice emerges from your staff into the enemy!!"
    }

    backstab = {
      'name': "Backstab",
      'element': "critical",
      'mpcost': 3,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nYou sneak around to the back of the enemy for 1d8 damage.",
      'effectdes': "\nYou backstab the enemy!"
    }

    flurry = {
      'name': "Flurry of Blows",
      'element': "striking",
      'mpcost': 4,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_2,
      'effect': physical_damage,
      'skilldes': "\nYou unleash a flurry of blows for 1d8 + 1d2 damage.",
      'effectdes': "\nYou unleash a barrage of attacks!"
    }

    legshot = {
      'name': "Leg Shot",
      'element': "leg",
      'mpcost': 4,
      'dice': Dice.d_6,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nA shot to the legs for 1d6 damage.",
      'effectdes': "\nAim for the legs!"
    }

    warrior_attack_skill_list = {
      1: overhead_slash,
      2: shield_bash,
      3: flurry,
      4: legshot
    }

    rogue_attack_skill_list = {
      1: backstab,
      2: flurry,
      3: legshot
    }

    mage_attack_skill_list = {
      1: fireball,
      2: icewall,
    }

    barb_attack_skill_list = {
      1: flurry,
      2: overhead_slash,
    }

class BuffSkill:

  def blk_buff(skill, player, enemy):
      current_turn = Turn.current_turn
      while current_turn != skill['turns']:
        characterbuff = skill['dice']()
        Utility.menu(f"\n\n{skill['effectdes']}")
        Utility.menu(f"\n{player.name} has used {skill['name']} \nand raised their {skill['element']} by {characterbuff}.")
        enemy == False

  def combat_end(player, enemy):
    while enemy.hp <= 0:
      return True
    else:
      return False
  
  shadows = {
      'name': "Hide in Shadows",
      'element': 'defence',
      'mpcost': 4,
      'turns': combat_end,
      'dice': Dice.d_4,
      'effect': blk_buff,
      'skilldes': "\nYou attempt to hide in shadows! Raises defence by 1d4 until the end of the battle.",
      'effectdes': "\nYou hide in shadows!"
    }

  bush = {
      'name': "Hide in a Bush",
      'element': 'defence',
      'mpcost': 4,
      'turns': 2,
      'dice': Dice.d_4,
      'effect': blk_buff,
      'skilldes': "\nThe enemy hides in a bush!",
      'effectdes': "\nThe enemy hides in a bush. Their defense raises by 1d4 for two turns."
  }

  buff_skill_list = {
    1: shadows,
    2: bush
  }
import time, sys
from Dice import *
from Game import *
from random import *
from Player import *

class Utility:

  @staticmethod
  def typingPrint(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.04)

  @staticmethod
  def fastTypingPrint(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.0000000000000000000000000000000001)

  @staticmethod
  def slowTypingPrint(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(1)

  @staticmethod
  def gameOver(self):
    Utility.typingPrint("\nGame over! Would you like to try again?")
    Utility.typingPrint("\n(Y)es or (N)o")
    answer = input("\n>>> ")
    if "y" in answer.lower():
      Game.main_menu()
    elif "n" in answer.lower():
      quit()
    else:
      self.gameOver()

  def player_combat_prompt(player, enemy):

    Utility.typingPrint("\n\nDo you (A)ttack or do you use a (S)kill?")
    Utility.fastTypingPrint("\n########################################")
    Utility.fastTypingPrint("\n\nYou have:")
    Utility.fastTypingPrint("\nHP: " + str(player.hp))
    Utility.fastTypingPrint("\nMP: " + str(player.mp))
    skillset = "{0}, {1}".format(player.skill1['name'], player.skill2['name'])
    Utility.fastTypingPrint("\nSkills: " + str(skillset))
    answer = input('\n>>> ')
    if 'a' in answer.lower():
      Utility.attack(player, enemy)
    elif 's' in answer.lower():
      Utility.typingPrint('\nDo you want to use (1) {0} or (2) {1}?'.format(player.skill1['name'], player.skill2['name']))
      Utility.fastTypingPrint('\n\nSkill: %s' % player.skill1['name'])
      Utility.fastTypingPrint('\nMana Cost: %s' % player.skill1['mpcost'])
      Utility.fastTypingPrint('\nEffect: %s' % player.skill1['skilldes'])
      Utility.fastTypingPrint('\n\nSkill: %s' % player.skill2['name'])
      Utility.fastTypingPrint('\nMana Cost: %s' % player.skill2['mpcost'])
      Utility.fastTypingPrint('\nEffect: %s' % player.skill2['skilldes'])
      answer = input("\n\n>>> ")
      if str(1) in answer:
        if player.mp >= player.skill1['mpcost']:
          SkillUse.skill1(player, enemy)
        else:
          Utility.typingPrint('\nYou do not have enough mana.')
          Utility.player_combat_prompt(player, enemy)
      elif str(2) in answer:
        if player.mp >= player.skill2['mpcost']:
          SkillUse.skill2(player, enemy)
        else:
          Utility.typingPrint('\nYou do not have enough mana.')
          Utility.player_combat_prompt(player, enemy)
      else:
        Utility.typingPrint('\nYou must select a skill.')
        Utility.player_combat_prompt(player, enemy)
    else:
      Utility.player_combat_prompt(player, enemy)

  def attack(player, enemy):
    Utility.typingPrint('\n\nYou have chosen to attack!')
    damage = (player.atk + player.additional_damage) - enemy.blk if (player.atk + player.additional_damage) - enemy.blk > 0 else 0
    enemy.hp -= damage
    Utility.typingPrint(f"\n\nYou rolled a {player.atk} on your damage dice and {enemy.name} blocked {enemy.blk} of it.\
    \nYou have dealt {damage} points of damage. The enemy has {enemy.hp} hit points remaining.") if enemy.hp > 0 else 0
    if enemy.hp <= 0:
      Utility.typingPrint(f"\n\nYou rolled a {player.atk} on your damage dice and {enemy.name} blocked {enemy.blk} of it.\
      \nYou have dealt {damage} points of damage. The enemy has {enemy.hp} hit points remaining.") if enemy.hp > 0 else 0
      RecoverySkill.mp_recovery(player)
      Utility.enemy_killed(enemy)
    elif enemy.hp > 0:
      RecoverySkill.mp_recovery(player)
      Utility.enemy_attack(enemy, player)

  def enemy_attack(enemy, player):
    if enemy.mp >= enemy.skill1['mpcost']:
      SkillUse.enemy_skill1(enemy, player)
    elif enemy.mp >= enemy.skill2['mpcost']:
      SkillUse.enemy_skill2(enemy, player)
    else:
      Utility.typingPrint(f'\n\n{enemy.name} attacks!')
      damage = (enemy.atk + enemy.additional_damage) - player.blk if (enemy.atk + enemy.additional_damage) - player.blk > 0 else 0
      player.hp -= damage
      Utility.typingPrint(f'\n\n{enemy.name} rolled a {enemy.atk} on their damage dice and you blocked {player.blk} of it.\
      \nThey have dealt {damage} points of damage. You have {player.hp} hit points remaining.') if player.hp > 0 else 0
      if player.hp <= 0:
        Utility.typingPrint(f'\n\n{enemy.name} rolled a {enemy.atk} on their damage dice and you blocked {player.blk} of it.\
        \nThey have dealt {damage} points of damage. You have {player.hp} hit points remaining.') if player.hp > 0 else 0
        Utility.player_killed(player)
      elif player.hp > 0:
        RecoverySkill.mp_recovery(enemy)
        Utility.player_combat_prompt(player, enemy)

  def player_killed(player, self):
    if player.hp <= 0:
      Utility.typingPrint('\nYou have been killed!')
      Utility.gameOver(self)

  def enemy_killed(enemy):
    if enemy.hp <= 0:
      Utility.typingPrint(f'\n{enemy.name} has been killed!')

  def initiative():

    player_init = Dice.d_10()
    enemy_init = Dice.d_10()
    Utility.typingPrint('\nYou both roll for initiative!')
    Utility.typingPrint("\n\nYou rolled a " + str(player_init) + " and the enemy rolled a " + str(enemy_init) + ".")
    if player_init > enemy_init:
      Utility.typingPrint('\n\nYou rolled higher and get the first attack!\n')
      return True
    if player_init == enemy_init:
      Utility.typingPrint('\n\nYou both tied. The enemy gets to attack first!')
    else:
      Utility.typingPrint('\n\nThe enemy rolled higher and gets the first attack!\n')
      return False


class SkillUse:

    def skill1(player, enemy):
        skill = player.skill1
        player.skill1['effectdes']
        player.skill1['effect'](skill, player, enemy)
        Utility.typingPrint(f"\nThis action cost {player.name} {player.skill1['mpcost']} mana.")
        player.mp -= player.skill1['mpcost']
        Utility.typingPrint(f"\n{player.name} has {player.mp} MP remaining.")
        if enemy.hp <= 0:
          Utility.enemy_killed(enemy)
        else:
          Utility.enemy_attack(enemy, player)

    def skill2(player, enemy):
        skill = player.skill2
        player.skill2['effectdes']
        player.skill2['effect'](skill, player, enemy)
        Utility.typingPrint(f"\nThis action cost {player.name} {player.skill2['mpcost']} mana.")
        player.mp -= player.skill2['mpcost']
        Utility.typingPrint(f"\n{player.name} has {player.mp} MP remaining.")
        if enemy.hp <= 0:
          Utility.enemy_killed(enemy)
        else:
          Utility.enemy_attack(enemy, player)

    def enemy_skill1(enemy, player):
        skill = enemy.skill1
        enemy.skill1['effectdes']
        enemy.skill1['effect'](skill, enemy, player)
        Utility.typingPrint(f"\nThis action cost {enemy.name} {enemy.skill1['mpcost']} mana.")
        enemy.mp -= enemy.skill1['mpcost']
        Utility.typingPrint(f"\n{enemy.name} has {enemy.mp} MP remaining.")
        if player.hp <= 0:
          Utility.player_killed(player)
        else:
          Utility.player_combat_prompt(player, enemy)
    
    def enemy_skill2(enemy, player):
        skill = enemy.skill2
        enemy.skill2['effectdes']
        enemy.skill2['effect'](skill, enemy, player)
        Utility.typingPrint(f"\nThis action cost {enemy.name} {enemy.skill2['mpcost']} mana.")
        enemy.mp -= enemy.skill2['mpcost']
        Utility.typingPrint(f"\n{enemy.name} has {enemy.mp} MP remaining.")
        if player.hp <= 0:
          Utility.player_killed(player)
        else:
          Utility.player_combat_prompt(player, enemy)


class RecoverySkill:

  def mp_recovery(player):
        recovery = player.mprecover
        player.mp += recovery
        Utility.typingPrint(f'\n{player.name} naturally recovered {recovery} MP this turn.')

    
  def hp_recovery(skill, player, enemy):
        recovery = skill['dice']()
        player.hp += recovery
        Utility.typingPrint(f"\n\n{skill['effectdes']}")
        Utility.typingPrint(f"\n{player.name} recovered {recovery} HP from {skill['name']}.")
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
    

class AttackSkill:

    
    def physical_damage(skill, player, enemy):
      damage = (skill['dice']() + skill['additionaldamage']()) - (enemy.blk // 2) if (skill['dice']() + skill['additionaldamage']()) - (enemy.blk // 2) > 0 else 0
      enemy.hp -= damage
      Utility.typingPrint(f"\n\n{skill['effectdes']}")
      Utility.typingPrint(f"\n{player.name} has done {damage} points of {skill['element']} damage to {enemy.name}.")
        

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
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nA shot to the legs for 1d8 damage.",
      'effectdes': "\nAim for the legs!"
    }

class BuffSkill:

  def blk_buff(skill, player, enemy):
      characterbuff = skill['dice']()
      player.blk += characterbuff
      Utility.typingPrint(f"\n\n{skill['effectdes']}")
      Utility.typingPrint(f"\n{player.name} has used {skill['name']} \nand raised their {skill['element']} by {characterbuff}.")
      enemy == False

  
  shadows = {
      'name': "Hide in Shadows",
      'element': 'defence',
      'mpcost': 4,
      'turns': 2,
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
import time,os,sys
from Dice import *
from Player import *
from Game import *
from random import *

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
      self.main_menu()
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
      mprecovery = randint(1, 2)
      player.mp += mprecovery
      Utility.typingPrint('\nYou recovered {0} MP this turn.'.format(mprecovery))
      player.attack(enemy)
    elif 's' in answer.lower():
      Utility.typingPrint('\nDo you want to use (1) {0} or (2) {1}?'.format(player.skill1['name'], player.skill2['name']))
      Utility.fastTypingPrint('\n\nSkill: %s' % player.skill1['name'])
      Utility.fastTypingPrint('\nMana Cost: %s' % player.skill1['mpcost'])
      Utility.fastTypingPrint('\nDamage: %s' % player.skill1['damagedice'])
      Utility.fastTypingPrint('\n\nSkill: %s' % player.skill2['name'])
      Utility.fastTypingPrint('\nMana Cost: %s' % player.skill2['mpcost'])
      Utility.fastTypingPrint('\nDamage: %s' % player.skill2['damagedice'])
      answer = input("\n\n>>> ")
      if str(1) in answer.lower():
        if player.mp >= player.skill1['mpcost']:
          damage = (player.skill1['damage'] - enemy.blk) if (player.skill1['damage'] - enemy.blk) >= 0 else 0
          Utility.typingPrint('\n\n{0}'.format(player.skill1['des']))
          Utility.typingPrint('\nYou use {0} on {1} for {2} damage!'.format(player.skill1['name'], enemy.name, damage))
          player.mp -= player.skill1['mpcost']
          enemy.hp -= damage
          mprecovery = randint(1, 2)
          player.mp += mprecovery
          Utility.typingPrint('\nYou recovered {0} MP this turn.'.format(mprecovery))
          if enemy.hp > 0:
            Utility.typingPrint('\n\n{0} has {1} hit points remaining.'.format(enemy.name, enemy.hp))
            enemy.attack(player)
          elif enemy.hp <= 0:
            Utility.typingPrint('\n{0} has been killed!'.format(enemy.name))
        elif player.mp < player.skill1['mpcost']:
          Utility.typingPrint('\nYou do not have enough mana. You only have {0} MP remaining.'.format(player.mp))
          Utility.player_combat_prompt(player, enemy)
      elif str(2) in answer.lower():
        if player.mp >= player.skill2['mpcost']:
          damage = (player.skill2['damage'] - enemy.blk) if (player.skill2['damage'] - enemy.blk) >= 0 else 0
          Utility.typingPrint('\n\n{0}'.format(player.skill2['des']))
          Utility.typingPrint('\nYou use {0} on {1} for {2} damage!'.format(player.skill2['name'], enemy.name, damage))
          player.mp -= player.skill2['mpcost']
          enemy.hp -= damage
          mprecovery = randint(1, 2)
          player.mp += mprecovery
          Utility.typingPrint('\nYou recovered {0} MP this turn.'.format(mprecovery))
          if enemy.hp > 0:
            Utility.typingPrint('\n\n{0} has {1} hit points remaining.'.format(enemy.name, enemy.hp))
            enemy.attack(player)
          elif enemy.hp <= 0:
            Utility.typingPrint('\n{0} has been killed!'.format(enemy.name))
        elif player.mp < player.skill2['mpcost']:
          Utility.typingPrint('\nYou do not have enough mana. You only have {0} MP remaining.'.format(player.mp))
          Utility.player_combat_prompt(player, enemy)
      else:
        Utility.player_combat_prompt(player, enemy)



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

 
    


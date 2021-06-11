import time, sys
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
      Player.attack(player, enemy)
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
        Player.skill1(player, enemy)
      elif str(2) in answer:
        Player.skill2(player, enemy)
    else:
      Utility.player_combat_prompt(player, enemy)

  def player_killed(player):
    if player.hp < 0:
      Utility.typingPrint('\nYou have been killed!')
      Utility.gameOver()



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

 
    


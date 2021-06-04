import time,os,sys
from Dice import *
from Player import *
from Game import *

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
    self.typingPrint("\nGame over! Would you like to try again?")
    self.typingPrint("\n(Y)es or (N)o")
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
    Utility.typingPrint("\n\nYou have:")
    Utility.typingPrint("\nHP: " + str(player.hp))
    Utility.typingPrint("\nMP: " + str(player.mp))
    Utility.typingPrint("\nSkills: " + str(player.skills[1, 1]))
    answer = input('\n>>> ')
    if 'a' in answer.lower():
      player.attack(enemy)
    elif 's' in answer.lower():
      pass

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

 
    


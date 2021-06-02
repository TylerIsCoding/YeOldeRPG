import time,os,sys
import typing
from Dice import *
from Player import *

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)


def fastTypingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.0000000000000000000000000000000001)


def slowTypingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(1)


def gameOver(self):
  typingPrint("\nGame over! Would you like to try again?")
  typingPrint("\n(Y)es or (N)o")
  answer = input("\n>>> ")
  if "y" in answer.lower():
    self.Game.main_menu()
  elif "n" in answer.lower():
    quit()
  else:
    self.gameOver()


def initiative(self):
  player_init = Dice.d_10()
  enemy_init = Dice.d_10()
  typingPrint('\nYou both roll for initiative!')
  typingPrint("\n\nYou rolled a " + str(player_init) + " and the enemy rolled a " + str(enemy_init) + ".")
  if player_init > enemy_init:
    typingPrint('\n\nYou rolled higher and get the first attack!')
    player_init_win = True
    return player_init_win
  else:
    typingPrint('\n\nThe enemy rolled higher and gets the first attack!')
    player_init_win = False
    return player_init_win


def player_combat_prompt(self):
  typingPrint("\nDo you (A)ttack or do you use a (S)kill?")
  fastTypingPrint("\n########################################")
  typingPrint("\nYou have:")
  typingPrint("\nHP:" + str(self.myPlayer.hp))
  typingPrint("\nMP:" + str(self.myPlayer.mp))
  answer = input('\n>>> ')
  if 'a' in answer.lower():
    self.myPlayer.attack()
  elif 's' in answer.lower():
    self.myPlayer.skill_list()


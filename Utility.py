import time,os,sys
import typing
from Dice import *

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
    self.game.main_menu()
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
    typingPrint('\nYou rolled higher and get the first attack!')
    """Code for player combat turn here"""
  else:
    typingPrint('\nThe enemy rolled higher and gets the first attack!')
    """Code for enemy combat turn here"""


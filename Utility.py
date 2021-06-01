import time,os,sys
import typing

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
##### Imports #####
import time, sys
from typing import *
from Dice import *
from random import *
import random
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

      Turn.current_turn -= 1


class Utility:


  def continue_prompt():
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


##### INITIATIVE #####


  def initiative():

    player_init = Dice.d_10()
    enemy_init = Dice.d_10()
    Utility.combat('\nYou both roll for initiative!')
    Utility.combat("\n\nYou rolled a " + str(player_init) + " and the enemy rolled a " + str(enemy_init) + ".")
    if player_init > enemy_init:
      Utility.combat('\n\nYou rolled higher and get the first attack!\n')
      return True
    elif player_init == enemy_init:
      Utility.combat('\n\nYou both tied. The enemy gets to attack first!')
      Utility.continue_prompt()
      return False
    else:
      Utility.combat('\n\nThe enemy rolled higher and gets the first attack!\n')
      Utility.continue_prompt()
      return False


##### BUFF FUNCTIONS #####


  def buff_check(player, enemy):

    if player.type == "Player":
      if player.atk_buff.type != 'none' and player.atk_buff.duration == Turn.atk_turns_passed:
        Turn.atk_turns_passed = 0
        Utility.combat(f'\n\n"{player.atk_buff.name}" has worn off.')
        player.atk_buff = Default
      if player.def_buff.type != 'none' and player.def_buff.duration == Turn.def_turns_passed:
        Turn.def_turns_passed = 0
        Utility.combat(f'\n\n"{player.def_buff.name}" has worn off.')
        player.def_buff = Default
      if enemy.hp > 0:  
        Utility.player_combat_prompt(player, enemy)
      else:
        Utility.buff_clear(player, enemy)
    else:
      Utility.combat('\n\n##############################################')
      if player.atk_buff.type != 'none' and player.atk_buff.duration == Turn.atk_enemy_turns_passed:
        Turn.atk_enemy_turns_passed = 0
        Utility.combat(f'\n\n"{player.atk_buff.name}" has worn off.')
        player.atk_buff = Default
      if player.def_buff.type != 'none' and player.def_buff.duration == Turn.def_enemy_turns_passed:
        Turn.def_enemy_turns_passed = 0
        Utility.combat(f'\n\n"{player.def_buff.name}" has worn off.')
        player.def_buff = Default
      if player.hp > 0:
        SkillUse.enemy_skill(player, enemy)
      else:
        Utility.buff_clear(enemy, player)

      
  def buff_clear(player, enemy):

    player.atk_buff = Default
    player.def_buff = Default
    enemy.atk_buff = Default
    enemy.def_buff = Default


##### COMBAT FUNCTIONS #####


  def player_combat_prompt(player, enemy):

    Utility.combat('\n\n##############################################')
    Utility.combat('\n' * 5)
    Utility.combat('\nYour turn!')
    Utility.continue_prompt()
    this_turn = Turn.current_turn
    Turn.def_turns_passed += 1
    Turn.def_enemy_turns_passed += 1
    Turn.atk_turns_passed += 1
    Turn.atk_enemy_turns_passed += 1
    Turn.turn_count(this_turn)
    TextSpeed.instant('\n\n#############') 
    TextSpeed.instant(f'\n#  Turn: {Turn.current_turn}  #')
    TextSpeed.instant('\n#############\n')
    TextSpeed.instant("\n\n##############################################") 
    TextSpeed.instant("\n#  Do you (A)ttack or do you use a (S)kill?  #")
    TextSpeed.instant("\n##############################################\n")
    TextSpeed.instant("\nHP: " + str(player.hp))
    TextSpeed.instant("\nMP: " + str(player.mp))
    if player.def_buff.name != "default":
      TextSpeed.instant(f"\nBuff: {player.def_buff.name} | Turns Remaining: {player.def_buff.duration - Turn.def_turns_passed}")
      TextSpeed.instant(f"\nDefense: {player.defense} + {player.def_buff.maxbuff}")
    else:
      TextSpeed.instant(f"\nDefense: {player.defense}")
    if player.atk_buff.name != "default":
      TextSpeed.instant(f"\nBuff: {player.atk_buff.name} | Turns Remaining: {player.atk_buff.duration - Turn.atk_turns_passed}")
      TextSpeed.instant(f"\nAttack: {player.max_attack_str} + {player.atk_buff.maxbuff}")
    else:
      TextSpeed.instant(f"\nAttack: {player.max_attack_str}")
    TextSpeed.instant('\n\n--------------------')
    TextSpeed.instant('\n|      Skills      |')  
    TextSpeed.instant('\n--------------------\n')  
    for skill in player.skills:
      TextSpeed.instant(f'\n{skill.name} | MP: {skill.mpcost}')
    answer = input('\n\n>>> ')
    if 'a' in answer.lower():
      Utility.attack(player, enemy)
      Recovery.mp_recovery(player)
    elif 's' in answer.lower():
      SkillUse.player_skill(player, enemy)
    else:
      Utility.combat('\nYou must make a valid selection.')
      Turn.clear_turn()
      Utility.player_combat_prompt(player, enemy)
     

  def attack(player, enemy):

    attackbuff = player.atk_buff.dice()
    attack = player.atk() + player.additional_damage
    defbuff = enemy.def_buff.dice()
    defense = enemy.blk()
    damage = (attack + attackbuff) - (defense + defbuff) if (attack + attackbuff) - (defense + defbuff) > 0 else 0
    enemy.hp -= damage
    defense_roll = defbuff + defense
    if defense_roll > attackbuff + attack:
      defense_roll = "all"
    Utility.combat(f'\n\n{player.name} attacks!')
    Utility.combat(f'\n\n{player.name} has rolled {attackbuff + attack} on their damage dice and {enemy.name} blocked {defense_roll} of it.')
    Utility.remainder(player, enemy)

  def remainder(player, enemy):

    if enemy.type == "Player":
      if enemy.hp <= 0:
        Utility.combat(f'\n\n{enemy.name} has {enemy.hp} HP remaining.') if enemy.hp > 0 else 0
        Utility.player_killed(enemy)
      else:
        Utility.combat(f'\n\n{enemy.name} has {enemy.hp} HP remaining.') if enemy.hp > 0 else 0
        Utility.buff_check(enemy, player)
    else:
      if enemy.hp <= 0:
        Utility.combat(f'\n\n{enemy.name} has {enemy.hp} HP remaining.') if enemy.hp > 0 else 0
        Utility.enemy_killed(enemy, player)
      else:
        Utility.combat(f'\n\n{enemy.name} has {enemy.hp} HP remaining.') if enemy.hp > 0 else 0
        Utility.buff_check(enemy, player)

##### DEATH FUNCTIONS #####


  def player_killed(player):

      Utility.combat('\n\nYou have been killed!\n')
      Utility.gameOver()

  def enemy_killed(enemy, player):

      Utility.combat(f'\n\n{enemy.name} has been killed!\n')
      Utility.buff_clear(player, enemy)


##### SKILL FUNCTIONS #####


class SkillUse:

    def player_skill(player, enemy):
      count = 1
      for skill in player.skills:
        Utility.combat(f'\n{count}.) {skill.name} | MP Cost: {skill.mpcost}')
        count += 1
      Utility.combat(f'\n{count}.) Return')
      selection = input('\n\n>>> ')
      if int(selection) <= len(player.skills):
        choice = player.skills[(int(selection) - 1)]
        if choice.type == 'attack' and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
        elif choice.type == 'atk_buff' and player.atk_buff.type == 'none' and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.buff_check(enemy, player)
        elif choice.type == 'atk_buff' and player.atk_buff.type != 'none':
          Utility.combat('\nYou already have an attack buff. Please make a different selection.')
          Turn.clear_turn()
          Utility.player_combat_prompt(player, enemy)
        elif choice.type == 'def_buff' and player.def_buff.type == 'none' and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.buff_check(enemy, player)
        elif choice.type == 'def_buff' and player.def_buff.type != 'none':
          Utility.combat('\nYou already have a defensive buff. Please make a different selection.')
          Turn.clear_turn()
          Utility.player_combat_prompt(player, enemy)
        elif choice.type == 'heal' and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.buff_check(enemy, player)
        elif choice.mpcost > player.mp:
          Utility.combat('\nYou do not have enough mana.')
          Turn.clear_turn()
          Utility.player_combat_prompt(player, enemy)
      elif int(selection) == count:
        Turn.clear_turn()
        Utility.player_combat_prompt(player, enemy)
      else:
        Utility.combat('\nPlease make a valid selection.')
        Turn.clear_turn()
        Utility.player_combat_prompt(player, enemy)

  
    def enemy_skill(enemy, player):

      temp = []
      if enemy.hp > 0:
        if enemy.atk_buff.name == 'default' and enemy.def_buff.name == 'default':
          for skill in enemy.skills:
            if skill.type == "atk_buff" or "def_buff":
              temp.append(skill)
            else:
              Utility.attack(enemy, player)
          selection = random.choice(temp)
          if enemy.mp >= selection.mpcost:
            selection.effect(selection, enemy, player)
            enemy.mp -= skill.mpcost
            Utility.buff_check(player, enemy)
          else:
            Utility.attack(enemy, player)
        elif enemy.atk_buff.name == 'default' and enemy.def_buff.name != 'default':
          for skill in enemy.skills:
            if skill.type == "atk_buff":
              temp.append(skill)
            else:
              Utility.attack(enemy, player)
          selection = random.choice(temp)
          if enemy.mp >= selection.mpcost:
            selection.effect(selection, enemy, player)
            enemy.mp -= skill.mpcost
            Utility.buff_check(player, enemy)
          else:
            Utility.attack(enemy, player)
        elif enemy.atk_buff.name != 'default' and enemy.def_buff.name == 'default':
          for skill in enemy.skills:
            if skill.type == "def_buff":
              temp.append(skill)
            else:
              Utility.attack(enemy, player)
          selection = random.choice(temp)
          if enemy.mp >= selection.mpcost:
            selection.effect(selection, enemy, player)
            enemy.mp -= skill.mpcost
            Utility.buff_check(player, enemy)
          else:
            Utility.attack(enemy, player)
        elif enemy.atk_buff.name != 'default' and enemy.def_buff.name != 'default':
          for skill in enemy.skills:
            if skill.type != "atk_buff" or "def_buff" and skill.mpcost <= enemy.mp:
              skill.effect(skill, enemy, player)
              enemy.mp -= skill.mpcost
        else:
          Utility.attack(enemy, player)
      else:
        None
     
##### Default #####


class Default:

    name = "default"
    type = "none"
    skillcost = 0
    element = "none"
    mpcost = 0
    duration = 0
    dice = Dice.d_0
    maxbuff = "none"
    effect = "none"
    skilldes = "\nERROR"
    effectdes = "\nERROR"


class Attack:

  def physical_damage(skill, player, enemy):

    block = enemy.blk() + enemy.def_buff.dice()
    attackdice = skill.dice() + skill.additionaldamage()
    damage =  attackdice - block
    if damage > 0 if damage > 0 else 0:
      enemy.hp -= damage
    Utility.combat(f"\n\n{skill.effectdes}")
    Utility.combat(f'\n\n{player.name} attempts "{skill.name}" and rolled a {attackdice} on their attack dice.\
    \n{enemy.name} rolled a {block} on their defensive dice.')
    if damage > 0 if damage > 0 else 0:
      Utility.combat(f"\n\n{player.name} has done {damage} points of {skill.element} damage to {enemy.name}.\
      \n{enemy.name} has {enemy.hp} HP remaining.") if enemy.hp > 0 else 0
    else:
      Utility.combat(f"\n\n{player.name} has done no damage to {enemy.name}.\
      \n{enemy.name} still has {enemy.hp} HP remaining.")
    if player.type == "Player":
      if enemy.hp <= 0:
        Utility.enemy_killed(enemy, player)
      else:
        Utility.buff_check(enemy, player)
    else:
      if enemy.hp <= 0:
        Utility.player_killed(enemy)
      else:
        Utility.buff_check(enemy, player)
  

  type = "attack"
  effect = physical_damage


class Buff:
  
  def def_buff(skill, player, enemy):

    player.def_buff = skill
    if player.type == "Player":
        Turn.def_turns_passed = 0
    else:
        Turn.def_enemy_turns_passed = 0
    Utility.combat(f"\n{skill.effectdes}")
    Utility.combat(f"\n\n{player.name} raised their {skill.element} by {skill.maxbuff} for {skill.duration} turns.")
    enemy == False

  def atk_buff(skill, player, enemy):

    player.atk_buff = skill
    if player.type == "Player":
        Turn.atk_turns_passed = 0
    else:
        Turn.atk_enemy_turns_passed = 0
    Utility.combat(f"\n{skill.effectdes}")
    Utility.combat(f"\n\n{player.name} raised their {skill.element} by {skill.maxbuff} for {skill.duration} turns.")
    enemy == False


##### Warrior Abilities #####


class ShieldBash(Attack):

  name = "Shield Bash"
  role = "Warrior"
  skillcost = 5
  element = "bashing"
  mpcost = 4
  dice = Dice.d_8
  additionaldamage = Dice.d_0
  skilldes = "\nAttacks with the player's shield. Does 1d8 damage."
  effectdes = "\nYou throw the weight of your shield into the enemy!\n"


class OverheadSlash(Attack):

  name = "Overhead Slash"
  role = "Warrior"
  skillcost = 6
  element = "slashing"
  mpcost = 5
  dice = Dice.d_10
  additionaldamage = Dice.d_0
  skilldes = "\nA powerful overhead slash. Does 1d10 damage."
  effectdes = "\nYou swing your weapon from overhead!\n"


class Rage(Buff):

  name = "Blinding Rage"
  role = "Warrior"
  type = 'atk_buff'
  skillcost = 4
  element = 'attack'
  mpcost = 4
  duration = 2
  dice = Dice.d_8
  maxbuff = "1d8"
  effect = Buff.atk_buff
  skilldes = "\nYour attack is raised by 1d8 for two turns!"
  effectdes =  "\nYou are filled with rage!"


##### Barbarian Abilities #####


class Kick(Attack):

  name = "Fierce Kick"
  role = "Barbarian"
  skillcost = 5
  element = "kicking"
  mpcost = 5
  dice = Dice.d_8
  additionaldamage = Dice.d_2
  skilldes = "\nA powerful kick. 1d8 + 1d2 kicking damage."
  effectdes = "\nYou kick with all of your might!\n"


class Flurry(Attack):

  name = "Flurry of Blows"
  role = "Barbarian"
  type = 'attack'
  skillcost = 8
  element = "striking"
  mpcost = 4
  dice = Dice.d_8
  additionaldamage = Dice.d_2
  skilldes = "\nUnleash a flurry of blows for 1d8 + 1d2 damage."
  effectdes = "\nYou unleash a barrage of attacks!\n"


class Anger(Buff):

  name = 'Anger'
  role = "Barbarian"
  type = 'atk_buff'
  skillcost = 4
  element = 'attack'
  mpcost = 4
  duration = 2
  dice = Dice.d_8
  maxbuff = "1d8"
  effect = Buff.atk_buff
  skilldes = "\nYou get angry! Your attack is raised by 1d8 for two turns!"
  effectdes = "\nYou're furious!"


##### Mage Abilities #####


class Fireball(Attack):

  name = "Fireball"
  role = 'Mage'
  type = 'attack'
  skillcost = 6
  element = "fire"
  mpcost = 4
  dice = Dice.d_8
  additionaldamage = Dice.d_0
  skilldes = "\nAttacks with a fireball. Does 1d8 damage."
  effectdes = "\nYou cast a mighty fireball!\n"


class IceWall(Attack):

  name = "Ice Wall"
  role = 'Mage'
  type = 'attack'
  skillcost = 4
  element = "ice"
  mpcost = 3
  dice = Dice.d_6
  additionaldamage = Dice.d_2
  skilldes = "\nAttacks with a sheet of ice. Does 1d6 damage."
  effectdes = "\nA sheet of ice emerges from the staff into the enemy!\n"


class Lightning(Attack):

  name = "Lightning Strike"
  role = 'Mage'
  type = 'attack'
  skillcost = 4
  element = "lightning"
  mpcost = 3
  dice = Dice.d_6
  additionaldamage = Dice.d_2
  skilldes = "\nA lightning strike! Does 1d6 + 1d4 of lightning damage."
  effectdes = "\nA bolt of lightning comes from the heavens!\n"


class Barrier(Buff):

  name = "Magical Barrier"
  role = 'Mage'
  type = 'def_buff'
  skillcost = 6
  element = 'defense'
  mpcost = 6
  duration = 3
  dice = Dice.d_6
  maxbuff = "1d6"
  effect = Buff.def_buff
  skilldes = "\nRaises defense by 1d6 for 3 turns."
  effectdes = "\nYou form a magical barrier around yourself!\n"


##### Rogue Abilities #####


class Backstab(Attack):

  name = "Backstab"
  role = "Rogue"
  type = 'attack'
  skillcost = 8
  element = "critical"
  mpcost = 4
  dice = Dice.d_8
  additionaldamage = Dice.d_2
  skilldes = "\nSneak around to the back of the enemy for 1d8 + 1d2 damage."
  effectdes = "\nYou backstab the enemy!\n"


class TripWire(Attack):

  name = "Trip Wire"
  role = "Rogue"
  type = 'attack'
  skillcost = 4
  element = "critical"
  mpcost = 4
  dice = Dice.d_6
  additionaldamage = Dice.d_4
  skilldes = "\nSet up a trip wire for the enemy. Does 1d6 + 1d4 damage."
  effectdes = "\nThe enemy hits the trip wire!\n"


class Shadows(Buff):

  name = "Hide in Shadows"
  role = "Rogue"
  type = 'def_buff'
  skillcost = 6
  element = 'defense'
  mpcost = 4
  duration = 3
  dice = Dice.d_4
  maxbuff = "1d4"
  effect = Buff.def_buff
  skilldes = "\nRaises defense by 1d4 for 3 turns."
  effectdes = "\nYou hide in shadows!\n"


##### Enemy Abilities #####


class Legshot(Attack):

  name = "Leg Shot"
  role = "Enemy"
  type = 'attack'
  skillcost = 3
  element = "leg"
  mpcost = 4
  dice = Dice.d_8
  additionaldamage = Dice.d_0
  skilldes = "\nA shot to the legs for 1d8 damage."
  effectdes = "\nAim for the legs!\n"


class Aim(Attack):

  name = "Aim for the Head"
  role = "Enemy"
  type = 'attack'
  skillcost = 6
  element = "head"
  mpcost = 6
  dice = Dice.d_10
  additionaldamage = Dice.d_0
  skilldes = "\nA headshot for 1d10 damage."
  effectdes = "\nSteben aims for the head!\n"


class ExitCamp(Buff):

  name = "Exit Camp"
  role = "Enemy"
  type = 'atk_buff'
  skillcost = 6
  element = 'attack'
  mpcost = 4
  duration = 2
  dice = Dice.d_8
  maxbuff = '1d8'
  effect = Buff.atk_buff
  skilldes = "\nExit camps for 1d8 for two turns."
  effectdes = "\nSteven exit camps for an attack buff of 1d8 for two turns!\n"


class Bush(Buff):

  name = "Hide in Bush"
  role = "Enemy"
  type = 'def_buff'
  skillcost = 6
  element = 'defense'
  mpcost = 4
  duration = 2
  dice = Dice.d_8
  maxbuff = '1d8'
  effect = Buff.def_buff
  skilldes = "\nHide in a bush for two turns."
  effectdes = "\nNick hides in a bush!\n"


##### Recovery Skills #####


class Recovery:

  def hp_recovery(skill, player, enemy):
    recovery = skill.dice()
    player.hp += recovery
    Utility.combat(f"\n\n{skill.effectdes}")
    Utility.combat(f"\n{player.name} recovered {recovery} HP from {skill.name}.")
    if enemy.type == "Enemy":
      None
    else:
      None

  def mp_recovery(player):
    recovery = player.mprecover()
    player.mp += recovery
    Utility.combat(f'\n{player.name} naturally recovered {recovery} MP this turn.\n\n')


class HealMinor(Recovery):

    name = "Heal Minor Wounds"
    role = ''
    type = 'heal'
    skillcost = 4
    element = 'healing'
    mpcost = 5
    dice = Dice.d_4
    effect = Recovery.hp_recovery
    skilldes = "\nA minor healing spell. Recovers 1d4 HP on casting."
    effectdes = "\nYou cast heal minor wounds!\n"


class HealMajor(Recovery):

    name = "Heal Major Wounds"
    role = ''
    type = 'heal'
    skillcost = 6
    element = 'healing'
    mpcost = 8
    dice = Dice.d_6
    effect = Recovery.hp_recovery
    skilldes = "\nA major healing spell. Recovers 1d6 HP on casting.",
    effectdes = "\nYou cast heal major wounds!\n"


class Bandage(Recovery):

    name = "Bandage Wounds"
    role = ''
    type = 'heal'
    skillcost = 3
    element = 'healing'
    mpcost = 3
    dice = Dice.d_2
    effect = Recovery.hp_recovery
    skilldes = "\nAn attempt to bandage wounds. Recovers 1d2 HP."
    effectdes = "\nYou attempt to bandage your wounds.\n"
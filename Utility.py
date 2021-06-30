##### Imports #####
import time, sys
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


##### INITIATIVE #####


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


##### BUFF FUNCTIONS #####


  def def_buff_check(player, enemy):
    
    TextSpeed.instant('\n' * 5)
    if player.type == "Player":
      if player.def_buff.duration != Turn.def_turns_passed and player.def_buff.type != 'none':
        Utility.combat(f"{player.name} has {player.def_buff.duration - Turn.def_turns_passed} turns of \"{player.def_buff.name}\" remaining.")
        Utility.atk_buff_check(player, enemy)
      elif player.def_buff.type == 'none':
        Utility.atk_buff_check(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.def_buff.name}\" has worn off!")
        player.def_buff = Default
        Turn.def_turns_passed = 0
        Utility.atk_buff_check(player, enemy)
    else:
      if player.def_buff.duration != Turn.def_enemy_turns_passed and player.def_buff.type != "none":
        Utility.combat(f"{player.name} has {player.def_buff.duration - Turn.def_enemy_turns_passed} turns of \"{player.def_buff.name}\" remaining.")
        SkillUse.enemy_skill(player, enemy)
      elif player.def_buff.type == 'none':
        SkillUse.enemy_skill(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.def_buff.name}\" has worn off!")
        player.def_buff = Default
        Turn.def_enemy_turns_passed = 1
        SkillUse.enemy_skill(player, enemy)
  

  def atk_buff_check(player, enemy):

    TextSpeed.instant('\n' * 5)
    if player.type == "Player":
      if player.atk_buff.duration != Turn.atk_turns_passed and player.atk_buff != Default:
        Utility.combat(f"{player.name} has {player.atk_buff.duration - Turn.atk_turns_passed} turns of \"{player.atk_buff.name}\" remaining.")
        Utility.player_combat_prompt(player, enemy)
      elif player.atk_buff == Default:
        Utility.player_combat_prompt(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.atk_buff.name}\" has worn off!")
        player.atk_buff = Default
        Turn.atk_turns_passed = 0
        Utility.player_combat_prompt(player, enemy)
    else:
      if player.atk_buff.duration != Turn.atk_enemy_turns_passed and player.atk_buff != Default:
        Utility.combat(f"{player.name} has {player.atk_buff.duration - Turn.atk_enemy_turns_passed} turns of \"{player.atk_buff.name}\" remaining.")
        SkillUse.enemy_skill(player, enemy)
      elif player.atk_buff == Default:
        SkillUse.enemy_skill(player, enemy)
      else:
        Utility.combat(f"{player.name}'s buff \"{player.atk_buff.name}\" has worn off!")
        player.atk_buff = Default
        Turn.atk_enemy_turns_passed = 1
        SkillUse.enemy_skill(player, enemy)


  def buff_clear(player, enemy):

    if player.def_buff.name != "default" and player.atk_buff.name != "default":
      Turn.def_turns_passed = player.def_buff.duration
      Turn.atk_turns_passed = player.atk_buff.duration
      player.def_buff = Default
      player.atk_buff = Default
      enemy.def_buff = Default
      enemy.atk_buff = Default
      Turn.def_turns_passed = 0
      Turn.def_enemy_turns_passed = 0
      Turn.atk_turns_passed = 0
      Turn.atk_enemy_turns_passed = 0
    elif player.def_buff.name != "default":
      Turn.def_turns_passed = player.def_buff.duration
      player.def_buff = Default
      enemy.def_buff = Default
      Turn.def_turns_passed = 0
      Turn.def_enemy_turns_passed = 0
    elif player.atk_buff.name != "default":
      Turn.atk_turns_passed = player.atk_buff.duration
      player.atk_buff = Default
      enemy.atk_buff = Default
      Turn.atk_turns_passed = 0
      Turn.atk_enemy_turns_passed = 0
    else:
      None


##### COMBAT FUNCTIONS #####


  def player_combat_prompt(player, enemy):

    this_turn = Turn.current_turn
    Turn.def_turns_passed += 1
    Turn.def_enemy_turns_passed += 1
    Turn.atk_turns_passed += 1
    Turn.atk_enemy_turns_passed += 1
    Turn.turn_count(this_turn)
    TextSpeed.fast('\n\n#############') 
    TextSpeed.fast(f'\n#  Turn: {Turn.current_turn}  #')
    TextSpeed.fast('\n#############\n')
    TextSpeed.fast("\n\n##############################################") 
    TextSpeed.fast("\n#  Do you (A)ttack or do you use a (S)kill?  #")
    TextSpeed.fast("\n##############################################\n")
    Utility.combat("\nHP: " + str(player.hp))
    Utility.combat("\nMP: " + str(player.mp))
    if player.def_buff.name != "default":
      Utility.combat(f"\nBuff: {player.def_buff.name}")
      Utility.combat(f"\nDefense: {player.defense} + {player.def_buff.maxbuff}")
    else:
      Utility.combat(f"\nDefense: {player.defense}")
    if player.atk_buff.name != "default":
      Utility.combat(f"\nBuff: {player.atk_buff.name}")
      Utility.combat(f"\nAttack: {player.max_attack_str} + {player.atk_buff.maxbuff}")
    else:
      Utility.combat(f"\nAttack: {player.max_attack_str}")
    TextSpeed.fast('\n\n--------------------')
    TextSpeed.fast('\n|      Skills      |')  
    TextSpeed.fast('\n--------------------\n')  
    for skill in player.skills:
      Utility.combat(f'\n{skill.name} | MP: {skill.mpcost}')
    answer = input('\n\n>>> ')
    if 'a' in answer.lower():
      Utility.attack(player, enemy)
    elif 's' in answer.lower():
      SkillUse.player_skill(player, enemy)
     

  def attack(player, enemy):

    Utility.combat('\n\nYou have chosen to attack!')
    attack = player.atk()
    attackbuff = player.atk_buff.dice()
    if enemy.def_buff.type != 'none':
      enemybuff = enemy.def_buff.dice()
    else:
      enemybuff = 0
    enemyblock = enemy.blk()
    damage = (attack + player.additional_damage + attackbuff) - (enemyblock + enemybuff) \
      if (attack + player.additional_damage + attackbuff) - (enemyblock + enemybuff) > 0 else 0
    enemy.hp -= damage
    if (enemyblock + enemybuff) >= attack:
        finalblock = "all"
    else:
        finalblock = enemyblock + enemybuff
    Utility.combat(f"\n\nYou rolled a {attack + attackbuff} on your damage dice and {enemy.name} blocked {finalblock} of it.\
    \nYou have dealt {damage} points of damage. The enemy has {enemy.hp} hit points remaining.") if enemy.hp > 0 else 0
    if enemy.hp <= 0:
      Recovery.mp_recovery(player)
      Utility.enemy_killed(enemy, player)
    else:
      Recovery.mp_recovery(player)
      Utility.def_buff_check(enemy, player)


  def enemy_attack(enemy, player):
    
      Utility.combat(f'\n\n{enemy.name} attacks!')
      enemyattack = enemy.atk()
      enemyattackbuff = enemy.atk_buff.dice()
      playerbuff = player.def_buff.dice()
      playerblock = player.blk()
      damage = (enemyattack + enemy.additional_damage + enemyattackbuff) - (playerblock + playerbuff) \
        if (enemyattack + enemy.additional_damage + enemyattackbuff) - (playerblock + playerbuff) > 0 else 0
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
        Recovery.mp_recovery(enemy)
        Utility.def_buff_check(player, enemy)


##### DEATH FUNCTIONS #####


  def player_killed(player):

    if player.hp <= 0:
      Utility.combat('\n\nYou have been killed!\n')
      Utility.gameOver()

  def enemy_killed(enemy, player):

    if enemy.hp <= 0:
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
          Utility.def_buff_check(enemy, player)
        elif choice.type == 'atk_buff' and player.atk_buff.type == 'none' and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.def_buff_check(enemy, player)
        elif choice.type == 'atk_buff' and player.atk_buff.type != 'none':
          Utility.combat('\nYou already have an attack buff. Please make a different selection.')
          Turn.clear_turn()
          Utility.continue_prompt()
          Utility.player_combat_prompt(player, enemy)
        elif choice.type == 'def_buff' and player.def_buff.type == 'none' and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.def_buff_check(enemy, player)
        elif choice.type == 'def_buff' and player.def_buff.type != 'none':
          Utility.combat('\nYou already have a defensive buff. Please make a different selection.')
          Turn.clear_turn()
          Utility.continue_prompt()
          Utility.player_combat_prompt(player, enemy)
        elif choice.type == 'heal' and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.def_buff_check(enemy, player)
        elif choice.mpcost > player.mp:
          Utility.combat('\nYou do not have enough mana.')
          Turn.clear_turn()
          Utility.continue_prompt()
          Utility.player_combat_prompt(player, enemy)
      elif int(selection) == count:
        Turn.clear_turn()
        Utility.player_combat_prompt(player, enemy)
      else:
        Utility.combat('\nPlease make a valid selection.')
        Turn.clear_turn()
        Utility.continue_prompt()
        Utility.player_combat_prompt(player, enemy)

  
    def enemy_skill(enemy, player):

      temp = []
      if enemy.atk_buff.name == 'default' and enemy.def_buff.name == 'default':
        for skill in enemy.skills:
          if skill.type == "atk_buff" or "def_buff":
            temp.append(skill)
          else:
            Utility.enemy_attack(enemy, player)
        selection = random.choice(temp)
        if enemy.mp >= selection.mpcost:
          selection.effect(selection, enemy, player)
          enemy.mp -= skill.mpcost
          Utility.def_buff_check(player, enemy)
        else:
          Utility.enemy_attack(enemy, player)
      elif enemy.atk_buff.name == 'default' and enemy.def_buff.name != 'default':
        for skill in enemy.skills:
          if skill.type == "atk_buff":
            temp.append(skill)
          else:
            Utility.enemy_attack(enemy, player)
        selection = random.choice(temp)
        if enemy.mp >= selection.mpcost:
          selection.effect(selection, enemy, player)
          enemy.mp -= skill.mpcost
          Utility.def_buff_check(player, enemy)
        else:
          Utility.enemy_attack(enemy, player)
      elif enemy.atk_buff.name != 'default' and enemy.def_buff.name == 'default':
        for skill in enemy.skills:
          if skill.type == "def_buff":
            temp.append(skill)
          else:
            Utility.enemy_attack(enemy, player)
        selection = random.choice(temp)
        if enemy.mp >= selection.mpcost:
          selection.effect(selection, enemy, player)
          enemy.mp -= skill.mpcost
          Utility.def_buff_check(player, enemy)
        else:
          Utility.enemy_attack(enemy, player)
      elif enemy.atk_buff.name != 'default' and enemy.def_buff.name != 'default':
        for skill in enemy.skills:
          if skill.type != "atk_buff" or "def_buff" and skill.mpcost <= enemy.mp:
            skill.effect(skill, enemy, player)
            enemy.mp -= skill.mpcost
            Utility.def_buff_check(player, enemy)
      else:
        Utility.enemy_attack(enemy, player)
          
     
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
    damage = (skill.dice() + skill.additionaldamage()) - block
    if damage > 0:
      enemy.hp -= damage
      Utility.combat(f"\n\n{skill.effectdes}")
      Utility.combat(f"\n\n{player.name} has done {damage} points of {skill.element} damage to {enemy.name}.")
    else:
      damage = 0
      Utility.combat(f"\n\n{skill.effectdes}")
      Utility.combat(f"\n{player.name} has done {damage} points of {skill.element} damage to {enemy.name}.")
    if player.type == "Player" and enemy.hp <= 0:
      Utility.enemy_killed(enemy, player)
    elif player.type == "Enemy" and enemy.hp <= 0:
      Utility.player_killed(enemy)
    else:
      return True

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
    Utility.combat(f"\n{player.name} raised their {skill.element} by {skill.maxbuff} for {skill.duration} turns.")
    enemy == False

  def atk_buff(skill, player, enemy):

    player.atk_buff = skill
    if player.type == "Player":
        Turn.atk_turns_passed = 0
    else:
        Turn.atk_enemy_turns_passed = 0
    Utility.combat(f"\n{skill.effectdes}")
    Utility.combat(f"\n{player.name} raised their {skill.element} by {skill.maxbuff} for {skill.duration} turns.")
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
  mpcost = 3
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
  mpcost = 2
  dice = Dice.d_6
  additionaldamage = Dice.d_0
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
  additionaldamage = Dice.d_4
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
  mpcost = 5
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
  mpcost = 5
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
  effectdes = "\nNick hides in a bush for an additional 1d8 defense for two turns!\n"


##### Recovery Skills #####


class Recovery:

  def hp_recovery(skill, player, enemy):
    recovery = skill.dice()
    player.hp += recovery
    Utility.combat(f"\n\n{skill.effectdes}")
    Utility.combat(f"\n{player.name} recovered {recovery} HP from {skill.name}.")
    enemy == False

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
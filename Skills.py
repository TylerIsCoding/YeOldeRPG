##### Imports #####
from Dice import *
from Utility import Utility, Turn
###################

class SkillUse:

    def player_skill(player, enemy):
      count = 1
      for skill in player.skills:
        Utility.combat(f'\n{count}.) {skill.name} | {skill.mpcost}')
        count += 1
      Utility.combat(f'\n{count}.) Return')
      selection = input('\n\n>>> ')
      if int(selection) <= len(player.skills):
        choice = player.skills[(int(selection) - 1)]
        if choice.type == 'attack' and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.def_buff_check(enemy, player)
        elif choice.type == 'atk_buff' and player.atk_buff == Default and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.def_buff_check(enemy, player)
        elif choice.type == 'atk_buff' and player.atk_buff != Default:
          Utility.combat('\nYou already have an attack buff. Please make a different selection.')
          Turn.clear_turn()
          Utility.continue_prompt()
          Utility.player_combat_prompt(player, enemy)
        elif choice.type == 'def_buff' and player.def_buff == Default and choice.mpcost <= player.mp:
          player.mp -= choice.mpcost
          choice.effect(choice, player, enemy)
          Utility.def_buff_check(enemy, player)
        elif choice.type == 'def_buff' and player.def_buff != Default:
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


##### Warrior Abilities #####


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

  type = "attack"
  effect = physical_damage


class Buff:
  
  def def_buff(skill, player, enemy):

    player.def_buff = skill
    if player.type == "Player":
        Turn.def_turns_passed = 1
    else:
        Turn.def_enemy_turns_passed = 1
    Utility.combat(f"\n{skill.effectdes}")
    Utility.combat(f"\n{player.name} raised their {skill.element} by {skill.maxbuff}.")
    enemy == False

  def atk_buff(skill, player, enemy):

    player.atk_buff = skill
    if player.type == "Player":
        Turn.atk_turns_passed = 1
    else:
        Turn.atk_enemy_turns_passed = 1
    Utility.combat(f"\n{skill.effectdes}")
    Utility.combat(f"\n{player.name} raised their {skill.element} by {skill.maxbuff}.")
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
  duration = 3
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
  duration = 3
  dice = Dice.d_8
  maxbuff = "1d8"
  effect = Buff.atk_buff
  skilldes = "\nYou get angry! Your attack is raised by 1d8 for two turns!"
  effectdes = "\nYou're furious!"


##### Mage Abilities #####


class Fireball(Attack):

  name = "Fireball"
  role = 'Mage'
  type = 'magic'
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
  effectdes = "\nYou hide in shadows!\n"


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
  mpcost = 3
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
  skilldes = "\nA shot to the legs for 1d8 damage."
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
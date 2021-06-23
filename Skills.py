from Utility import *


class SkillUse:

    def skill1(player, enemy):

        skill = player.skill1
        player.skill1['effectdes']
        print('\n')
        player.skill1['effect'](skill, player, enemy)
        Utility.combat(f"\nThis action cost {player.name} {player.skill1['mpcost']} mana.")
        player.mp -= player.skill1['mpcost']
        Utility.combat(f"\n{player.name} has {player.mp} MP remaining.")
        if enemy.hp <= 0:
          Utility.enemy_killed(enemy, player)
        else:
          Utility.def_buff_check(enemy, player)


    def enemy_skill1(enemy, player):

        skill = enemy.skill1
        enemy.skill1['effectdes']
        enemy.skill1['effect'](skill, enemy, player)
        Utility.combat(f"\nThis action cost {enemy.name} {enemy.skill1['mpcost']} mana.")
        enemy.mp -= enemy.skill1['mpcost']
        Utility.combat(f"\n{enemy.name} has {enemy.mp} MP remaining.")
        if player.hp <= 0:
          Utility.player_killed(player)
        else:
          Utility.def_buff_check(player, enemy)
    


class WarriorAttack:

        role = "Warrior"
        type = "attack"
        effect = AttackSkill.physical_damage
        
class ShieldBash(WarriorAttack):

        name = "Shield Bash"
        skillcost = 5
        element = "bashing"
        mpcost = 4
        dice = Dice.d_8
        additionaldamage = Dice.d_0
        skilldes = "\nAttacks with the player's shield. Does 1d8 damage."
        effectdes = "\nYou throw the weight of your shield into the enemy!\n"

class OverheadSlash(WarriorAttack):

        name = "Shield Bash"
        skillcost = 6
        element = "slashing"
        mpcost = 5
        dice = Dice.d_10
        additionaldamage = Dice.d_0
        skilldes = "\nA powerful overhead slash. Does 1d10 damage."
        effectdes = "\nYou swing your weapon from overhead!\n"

class WarriorBuff:
    
    role = "Warrior"

class Rage(WarriorBuff):

    name = "Blinding Rage"
    type = 'attack'
    skillcost = 4
    element = 'attack'
    mpcost = 4
    duration = 3
    dice = Dice.d_8
    maxbuff = "1d8"
    effect = BuffSkill.atk_buff
    skilldes = "\nYou rage out! Your attack is raised by 1d8 for two turns!"
    effectdes =  "\nYou are filled with rage!"



class RecoverySkill:


  def mp_recovery(player):
        recovery = player.mprecover()
        player.mp += recovery
        Utility.combat(f'\n{player.name} naturally recovered {recovery} MP this turn.\n\n')

    
  def hp_recovery(skill, player, enemy):
        recovery = skill['dice']()
        player.hp += recovery
        Utility.combat(f"\n\n{skill['effectdes']}")
        Utility.combat(f"\n{player.name} recovered {recovery} HP from {skill['name']}.")
        enemy == False

  
  heal_minor = {
    'name': 'Heal Minor Wounds',
    'type': 'heal',
    'skillcost': 4,
    'element': 'healing',
    'mpcost': 5,
    'dice': Dice.d_4,
    'effect': hp_recovery,
    'skilldes': "\nA minor healing spell. Recovers 1d4 HP on casting.",
    'effectdes': "\nYou cast heal minor wounds!\n"
  }

  heal_major = {
    'name': 'Heal Major Wounds',
    'type': 'heal',
    'skillcost': 6,
    'element': 'healing',
    'mpcost': 8,
    'dice': Dice.d_6,
    'effect': hp_recovery,
    'skilldes': "\nA major healing spell. Recovers 1d6 HP on casting.",
    'effectdes': "\nYou cast heal major wounds!\n"
  }

  bandage = {
    'name': 'Bandage Wounds',
    'type': 'heal',
    'skillcost': 3,
    'element': 'healing',
    'mpcost': 3,
    'dice': Dice.d_2,
    'effect': hp_recovery,
    'skilldes': "\nAn attempt to bandage wounds. Recovers 1d2 HP.",
    'effectdes': "\nYou attempt to bandage your wounds.\n"
  }

  recovery_list = [
    heal_minor,
    heal_major,
    bandage
  ]


class AttackSkill:

    @staticmethod
    def physical_damage(skill, player, enemy):

      block = enemy.blk() + enemy.def_buff['dice']()
      damage = (skill['dice']() + skill['additionaldamage']()) - block
      if damage > 0:
        enemy.hp -= damage
        Utility.combat(f"\n\n{skill['effectdes']}")
        Utility.combat(f"\n\n{player.name} has done {damage} points of {skill['element']} damage to {enemy.name}.")
      else:
        damage = 0
        Utility.combat(f"\n\n{skill['effectdes']}")
        Utility.combat(f"\n{player.name} has done {damage} points of {skill['element']} damage to {enemy.name}.")


    ### Barbarian Skills ###

    kick = {
      'name': "Fierce Kick",
      'type': 'attack',
      'role': 'Barbarian',
      'skillcost': 5,
      'element': "kicking",
      'mpcost': 5,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_2,
      'effect': physical_damage,
      'skilldes': "\nA powerful kick. 1d8 + 1d2 kicking damage.",
      'effectdes': "\nYou kick with all of your might!\n"
    }

    flurry = {
      'name': "Flurry of Blows",
      'type': 'attack',
      'role': 'Barbarian',
      'skillcost': 8,
      'element': "striking",
      'mpcost': 4,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_2,
      'effect': physical_damage,
      'skilldes': "\nUnleash a flurry of blows for 1d8 + 1d2 damage.",
      'effectdes': "\nYou unleash a barrage of attacks!\n"
    }

  ### Mage Skills ###

    fireball = {
      'name': "Fireball",
      'type': 'magic',
      'role': 'Mage',
      'skillcost': 6,
      'element': "fire",
      'mpcost': 3,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nAttacks with a fireball. Does 1d8 damage.",
      'effectdes': "\nYou cast a mighty fireball!\n"
    }


    icewall = {
      'name': "Ice Wall",
      'type': 'magic',
      'role': 'Mage',
      'skillcost': 4,
      'element': "ice",
      'mpcost': 2,
      'dice': Dice.d_6,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nAttacks with a sheet of ice. Does 1d6 damage.",
      'effectdes': "\nA sheet of ice emerges from the staff into the enemy!\n"
    }


    lightning = {
      'name': "Lightning Strike",
      'type': 'magic',
      'role': 'Mage',
      'skillcost': 4,
      'element': "lightning",
      'mpcost': 3,
      'dice': Dice.d_6,
      'additionaldamage': Dice.d_4,
      'effect': physical_damage,
      'skilldes': "\nA lightning strike! Does 1d6 + 1d4 of lightning damage.",
      'effectdes': "\nA bolt of lightning comes from the heavens!\n"
    }

  ### Rogue Skills ###

    backstab = {
      'name': "Backstab",
      'type': 'attack',
      'role': 'Rogue',
      'skillcost': 8,
      'element': "critical",
      'mpcost': 5,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_2,
      'effect': physical_damage,
      'skilldes': "\nSneak around to the back of the enemy for 1d8 + 1d2 damage.",
      'effectdes': "\nYou backstab the enemy!\n"
    }


    tripwire = {
      'name': "Trip Wire",
      'type': 'attack',
      'role': 'Rogue',
      'skillcost': 4,
      'element': "critical",
      'mpcost': 4,
      'dice': Dice.d_6,
      'additionaldamage': Dice.d_4,
      'effect': physical_damage,
      'skilldes': "\nSet up a trip wire for the enemy. Does 1d6 + 1d4 damage.",
      'effectdes': "\nThe enemy hits the trip wire!\n"
    }

  ### Enemy Skills ##
  
    legshot = {
      'name': "Leg Shot",
      'type': 'attack',
      'role': 'Enemy',
      'skillcost': 3,
      'element': "leg",
      'mpcost': 3,
      'dice': Dice.d_8,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nA shot to the legs for 1d8 damage.",
      'effectdes': "\nAim for the legs!\n"
    }


    aim = {
      'name': "Aim for the Head",
      'type': 'attack',
      'role': 'Enemy',
      'skillcost': 6,
      'element': "head",
      'mpcost': 6,
      'dice': Dice.d_10,
      'additionaldamage': Dice.d_0,
      'effect': physical_damage,
      'skilldes': "\nA shot to the legs for 1d8 damage.",
      'effectdes': "\nSteben aims for the head!\n"
    }

class BuffSkill:

    @staticmethod
    def def_buff(skill, player, enemy):

        player.def_buff = skill
        if player.type == "Player":
            Turn.def_turns_passed = 1
        else:
            Turn.def_enemy_turns_passed = 1
        Utility.combat(f"\n{player.def_buff['effectdes']}")
        Utility.combat(f"\n{player.name} raised their {player.def_buff['element']} by {player.def_buff['maxbuff']}.")
        enemy == False
  

    @staticmethod
    def atk_buff(skill, player, enemy):

        player.atk_buff = skill
        if player.type == "Player":
            Turn.atk_turns_passed = 1
        else:
            Turn.atk_enemy_turns_passed = 1
        Utility.combat(f"\n{player.atk_buff['effectdes']}")
        Utility.combat(f"\n{player.name} raised their {player.atk_buff['element']} by {player.atk_buff['maxbuff']}.")
        enemy == False
  
### Default Buff ###

    default = {
    'name': "default",
    'type': 'none',
    'skillcost': 0,
    'element': 'none',
    'mpcost': 0,
    'duration': 0,
    'dice': Dice.d_0,
    'maxbuff': 'none',
    'effect': 'none',
    'skilldes': "\nERROR",
    'effectdes': "\nERROR"
  }

### Warrior Buff ###


### Barbarian Buff ###

    rage = {
        'name': "Blinding Rage",
        'type': 'atk_buff',
        'role': 'Barbarian',
        'skillcost': 4,
        'element': 'attack',
        'mpcost': 4,
        'duration': 3,
        'dice': Dice.d_8,
        'maxbuff': "1d8",
        'effect': atk_buff,
        'skilldes': "\nYou rage out! Your attack is raised by 1d8 for two turns!",
        'effectdes': "\nYou rage out!"
    }

### Rogue Buff ###

    shadows = {
      'name': "Hide in Shadows",
      'type': 'def_buff',
      'role': 'Rogue',
      'skillcost': 6,
      'element': 'defense',
      'mpcost': 5,
      'duration': 3,
      'dice': Dice.d_4,
      'maxbuff': "1d4",
      'effect': def_buff,
      'skilldes': "\nRaises defense by 1d4 for 3 turns.",
      'effectdes': "\nYou hide in shadows!\n"
    }

### Mage Buff ###

    barrier = {
      'name': "Magical Barrier",
      'type': 'def_buff',
      'role': 'Mage',
      'skillcost': 6,
      'element': 'defense',
      'mpcost': 6,
      'duration': 3,
      'dice': Dice.d_6,
      'maxbuff': "1d6",
      'effect': def_buff,
      'skilldes': "\nRaises defense by 1d6 for 3 turns.",
      'effectdes': "\nYou hide in shadows!\n"
  }

### Enemy Buff ###

    bush = {
      'name': "Hide in a Bush",
      'type': 'def_buff',
      'role': 'Enemy',
      'skillcost': 4,
      'element': 'defense',
      'mpcost': 4,
      'duration': 3,
      'dice': Dice.d_4,
      'maxbuff': "1d4",
      'effect': def_buff,
      'skilldes': "\nHide in a bush! Defense raises by 1d4 for two turns.",
      'effectdes': "\nThe enemy hides in a bush!\n"
  }


    exit_camp = {
      'name': "Exit Camp",
      'type': 'atk_buff',
      'role': 'Enemy',
      'skillcost': 6,
      'element': 'attack',
      'mpcost': 4,
      'duration': 2,
      'dice': Dice.d_8,
      'maxbuff': '1d8',
      'effect': atk_buff,
      'skilldes': "\nExit camps for 1d8 for two turns.",
      'effectdes': "\nSteven exit camps for an attack buff of 1d8 for two turns!\n"
    }

    buff_skill_list = [
        shadows,
        rage,
        barrier,
        bush,
        exit_camp
    ]
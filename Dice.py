import random


### Dice Rolls ###
class Dice:

    @staticmethod
    def d_20():
        result = random.randint(1, 20)
        print("You rolled a " + str(result) + " on your 1d20.")
        return result

    @staticmethod
    def d_12():
        result = random.randint(1, 12)
        print("You rolled a " + str(result) + " on your 1d12.")
        return result

    @staticmethod
    def d_10():
        result = random.randint(1, 10)
        print("You rolled a " + str(result) + " on your 1d10.")
        return result

    @staticmethod
    def d_8():
        result = random.randint(1, 8)
        print("You rolled a " + str(result) + " on your 1d8.")
        return result

    @staticmethod
    def d_6():
        result = random.randint(1, 6)
        print("You rolled a " + str(result) + " on your 1d6.")
        return result

    @staticmethod
    def d_4():
        result = random.randint(1, 4)
        print("You rolled a " + str(result) + " on your 1d4.")
        return result


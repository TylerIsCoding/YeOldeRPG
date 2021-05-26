import random


### Dice Rolls ###
class Dice:
    @staticmethod
    def d_20():
        return random.randint(1, 20)

    @staticmethod
    def d_12():
        return random.randint(1, 12)

    @staticmethod
    def d_10():
        return random.randint(1, 10)

    @staticmethod
    def d_8():
        return random.randint(1, 8)

    @staticmethod
    def d_6():
        return random.randint(1, 6)

    @staticmethod
    def d_4():
        return random.randint(1, 4)


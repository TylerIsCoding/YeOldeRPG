import random


### Dice Rolls ###
class Dice:

    @staticmethod
    def d_20():
        result = random.randint(1, 20)
        return result

    @staticmethod
    def d_12():
        result = random.randint(1, 12)
        return result

    @staticmethod
    def d_10():
        result = random.randint(1, 10)
        return result

    @staticmethod
    def d_8():
        result = random.randint(1, 8)
        return result

    @staticmethod
    def d_6():
        result = random.randint(1, 6)
        return result

    @staticmethod
    def d_4():
        result = random.randint(1, 4)
        return result

    @staticmethod
    def d_2():
        result = random.randint(1, 2)
        return result

    @staticmethod
    def d_0():
        result = random.randint(0, 0)
        return result


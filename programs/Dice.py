import random

class Dice:
    def roll(self):
        numbers = (1,2,3,4,5,6)
        print(f'({random.choice(numbers)}, {random.choice(numbers)})')

    def roll_efficiently(self):      
        print(f'({random.randint(1,6)}, {random.randint(1,6)})')



dice = Dice()
dice.roll()
dice.roll_efficiently()
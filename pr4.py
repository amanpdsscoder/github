from random import randint
class Dice():
    def _init_ (self):
        self.value = None
    def roll(self):
        self.value = randint(1,6)
        print(f"Dice Rolled for{i+1}th time = {self.value}")
        return self.value
dice= Dice()
n = int(input("How many times you want to roll a dice: "))
for i in range(n):
    dice.roll()
# Create a multisided die in a class
import random as rand

class MSDie:
    """
    Create a multisided die object that will 
    randomly decide a side to output.
    """

    def __init__(self, sides):
        self.sides = sides
        self.cur_value = self.roll()

    def __str__(self):
        return str(self.cur_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.sides, self.cur_value)

    def roll(self):
        self.cur_value = rand.randint(1, self.sides)
        return self.cur_value


six_die = MSDie(6)

for i in range(1, 3):
    print(six_die)
    six_die.roll()

print([MSDie(6), MSDie(20)])
print(MSDie(6).__repr__())
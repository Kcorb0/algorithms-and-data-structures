class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):

        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        newnum = (self.num * other_fraction.den) + (self.den * other_fraction.num)
        newden = self.den * other_fraction.den
        common = gcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)

    def __sub__(self, other_fraction):
        newnum = (self.num * other_fraction.den) - (self.den * other_fraction.num)
        newden = self.den * other_fraction.den
        common = gcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)

    def __mul__(self, other):
        
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)
    
    def __eq__(self, other_fraction):
        firstnum = self.num * other_fraction.den
        secondnum = other_fraction.num * self.den

        return firstnum == secondnum



def gcd(a, b):
    while a%b != 0:
        olda = a
        oldb = b
    
        a = oldb
        b = olda%oldb

    return b


f_one = Fraction(8, 5)
f_two = Fraction(20, 4)

f_three = f_one + f_two
print(f_three)

f_three = f_one * f_two
print(f_three)

f_three = f_one - f_two
print(f_three)
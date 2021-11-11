class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

        self.checkParams(self.num, self.den)
        self.gcd(self.num, self.den)

    def __str__(self):

        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        newnum = (self.num * other_fraction.den) + (self.den * other_fraction.num)
        newden = self.den * other_fraction.den
        
        return Fraction(newnum, newden)

    def __sub__(self, other_fraction):
        newnum = (self.num * other_fraction.den) - (self.den * other_fraction.num)
        newden = self.den * other_fraction.den
        
        return Fraction(newnum, newden)

    def __mul__(self, other):
        
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)
    
    def __eq__(self, other_fraction):
        firstnum = self.num * other_fraction.den
        secondnum = other_fraction.num * self.den

        return firstnum == secondnum

    def __gt__(self, other_fraction):
        firstnum = self.num * other_fraction.den
        secondnum = other_fraction.num * self.den

        return firstnum > secondnum

    def __lt__(self, other_fraction):
        firstnum = self.num * other_fraction.den
        secondnum = other_fraction.num * self.den

        return firstnum < secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def gcd(self, a, b):
        while a%b != 0:
            olda = a
            oldb = b
        
            a = oldb
            b = olda%oldb

        self.num = self.num // b
        self.den = self.den // b

    def checkParams(self, num, den):
        if num != int(num) or den != int(den):
            raise Exception("Fraction Numerator and Denominator must be positive integers.")




f_one = Fraction(1, 2)
f_two = Fraction(10, 4)

print(f_one)
print(f_two)

f_three = f_one + f_two
print(f_three)

f_three = f_one * f_two
print(f_three)

f_three = f_one - f_two
print(f_three)

f_four = f_one < f_two
print(f_four)
import random as rand

class Card:
    def __init__(self, num, csuit):
        self.num = num
        self.csuit = csuit
        self.ctype = None
        self.colour = None
        
        self.setType()
        self.setColour()

    def __repr__(self):
        rep = 'Card(' + str(self.num) + ', ' + str(self.ctype) + ', ' + str(self.csuit) + ', ' + str(self.colour) + ')'
        return rep
     
    def setType(self):
        if self.num == 1:
            self.ctype = 'Ace'
        elif self.num == 11:
            self.ctype = 'Jack'
        elif self.num == 12:
            self.ctype = 'Queen'
        elif self.num == 13:
            self.ctype = 'King'
        else:
            self.ctype = 'Number'

    def setColour(self):
        if self.csuit == 'Diamonds' or self.csuit == 'Hearts':
            self.colour = 'red'
        else:
            self.colour = 'black'
        

class JokerCard(Card):
    def __init__(self, num):
        Card.__init__(self, num)


class Deck:
    def __init__(self, suits, joker=False):
        self.suits = suits
        self.joker = joker
        self.deck = None

    def createDeck(self):
        suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
        deck = []

        for suit in suits:
            for i in range(1, 14):
                deck.append(Card(i, suit))

        self.deck = deck

    def shuffleDeck(self):
        return rand.shuffle(self.deck)

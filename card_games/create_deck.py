import random as rand


class Card:
    def __init__(self, num, csuit):
        self.num = num
        self.csuit = csuit
        self.ctype = self.setType()
        self.colour = self.setColour()
        self.symbol = self.setSymbol()

    def __repr__(self):
        rep = (
            "Card("
            + str(self.num)
            + ", "
            + str(self.ctype)
            + ", "
            + str(self.csuit)
            + ", "
            + str(self.colour)
            + ")"
        )
        return rep

    def setType(self):
        if self.num == 1:
            return "Ace"
        elif self.num == 11:
            return "Jack"
        elif self.num == 12:
            return "Queen"
        elif self.num == 13:
            return "King"
        else:
            return f"{self.num}"

    def setColour(self):

        if self.csuit == "Diamonds" or self.csuit == "Hearts":
            return "red"
        else:
            return "black"

    def setSymbol(self):

        s = self.ctype[0]

        if self.csuit == "Diamonds":
            return f"{s}♦"
        elif self.csuit == "Hearts":
            return f"{s}♥"
        elif self.csuit == "Clubs":
            return f"{s}♣"
        else:
            return f"{s}♠"


class JokerCard(Card):
    def __init__(self, num):
        Card.__init__(self, num)


class Deck:
    def __init__(self, suits, size=1, joker=False):
        self.suits = suits
        self.joker = joker
        self.size = size
        self.deck = self.createDeck()

    def createDeck(self):
        suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
        deck = []
        cnt = self.size

        while cnt != 0:
            for suit in suits:
                for i in range(1, 14):
                    deck.append(Card(i, suit))
            cnt -= 1

        return deck

    def shuffleDeck(self):
        return rand.shuffle(self.deck)

import os
from create_deck import Deck
from symbols import *

class HorsesGame:
    def __init__(self, players, length, deck_size=1):
        self.players = players
        self.length = length
        self.deck_size = deck_size

    def StartGame(self):
        newdeck = Deck(self.players, size=self.deck_size, joker=False)
        newdeck.createDeck()
        newdeck.shuffleDeck()

        scores = {
            'rounds': ["Rounds  ", "\t".join([str(n) for n in range(1, self.length+1)])],
            'Diamonds': ['Diamonds'],
            'Hearts': ['Hearts  '],
            'Clubs': ['Clubs   '],
            'Spades': ['Spades  '],
        }
        
        for card in newdeck.deck:
            if (self.length+1) not in [len(i) for i in scores.values()]:

                os.system('cls')
                print(title)

                scores[card.csuit].append(card.symbol)
                for i in scores.values():
                    print("" + "\t".join(i))

                input("")
        

horses = HorsesGame(4, 10, 2)
horses.StartGame()



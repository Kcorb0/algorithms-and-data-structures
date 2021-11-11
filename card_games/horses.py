from create_deck import Deck
from symbols import *

class HorsesGame:
    def __init__(self, players):
        self.players = players

    def StartGame(self):
        run = True
        newdeck = Deck(self.players, joker=False)
        newdeck.createDeck()
        newdeck.shuffleDeck()

        scores = {
            'Diamonds': 0,
            'Hearts': 0,
            'Clubs': 0,
            'Spades': 0,
        } 
        
        for card in newdeck.deck:
            if 10 not in scores.values():
                scores[card.csuit] += 1
            else:
                break
    
        print(scores)


horses = HorsesGame(4)
horses.StartGame()

print(title)
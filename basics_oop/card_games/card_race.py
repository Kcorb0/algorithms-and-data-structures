import os
from create_deck import Deck
from ascii_text import *


class HorsesGame:
    def __init__(self, players, length, deck_size=1):
        self.players = players
        self.length = length + 1
        self.deck_size = deck_size

    def StartGame(self):
        newdeck = Deck(self.players, size=self.deck_size, joker=False)
        newdeck.createDeck()
        newdeck.shuffleDeck()

        round_nums = "\t".join([str(n) for n in range(1, self.length)])
        scores = {
            "Rounds": ["Rounds  ", round_nums],
            "Diamonds": ["Diamonds "],
            "Hearts": ["Hearts\t"],
            "Clubs": ["Clubs\t"],
            "Spades": ["Spades\t"],
        }

        cur_suit = None

        for card in newdeck.deck:
            if self.length not in [len(i) for i in scores.values()]:
                os.system("cls")
                print(title)
                cur_suit = card.csuit
                scores[cur_suit].append(card.symbol)

                for i in scores.values():
                    print("\t".join(i))

                print(f"\nLast card was, {card.ctype} of {cur_suit}\n")
                input("Press 'enter' for next card")

        print(f"\n{cur_suit} wins!!!\n")


if __name__ == "__main__":
    horses = HorsesGame(4, 10, 1)
    horses.StartGame()

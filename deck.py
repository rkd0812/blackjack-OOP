import random
from card import Card


class Deck:
    def __init__(self):
        self.card_set = []
        self.fill_deck()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.card_set)

    def get_card_set(self):
        return self.card_set

    def fill_deck(self):
        for p in ["Heart", "Clover", "Diamond", "Spade"]:
            for s in range(13):
                self.card_set.append(Card(p, s + 1))

    def draw_card(self):
        if len(self.card_set) == 0:
            return None

        return self.card_set.pop()




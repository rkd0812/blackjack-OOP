import unittest
import copy
from deck import Deck


class DeckTest(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = Deck()

    def test_deck_creation(self):
        # deck = Deck()
        print('======= Card Set =======')
        for card in self.deck.get_card_set():
            print(f'{card.get_pattern()} : {card.get_score()} ')

        print('======= Card Set =======')
        self.assertEqual(len(self.deck.get_card_set()), 52)

    def test_deck_shuffle(self):
        # deck = Deck()
        card_set1 = self.deck
        card_set2 = copy.deepcopy(card_set1)
        card_set2.shuffle()

        self.assertNotEqual(card_set1.get_card_set()[0], card_set2.get_card_set()[0])

    def test_draw_card(self):
        card = self.deck.draw_card()
        print(f'{card.get_pattern()} : {card.get_score()} ')
        print(len(self.deck.get_card_set()))
        self.assertGreater(card.get_score(), 0)

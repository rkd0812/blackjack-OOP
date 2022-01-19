import unittest
from card import Card


class CardTest(unittest.TestCase):
    def test_runs(self):
        card = Card("Diamond", 1)
        self.assertEqual(card.get_score(), 1)

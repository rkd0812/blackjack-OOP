class Dealer:
    def __init__(self):
        print(f'Created Dealer')
        self.cards = []
        self.score = 0

    def draw_card(self, card):
        self.cards.append(card)

    def get_total_score(self):
        self.score = 0
        for card in self.cards:
            self.score += card.get_score()
        return self.score

    def open(self):
        return self.get_total_score()

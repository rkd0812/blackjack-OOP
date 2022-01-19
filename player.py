class Player:
    def __init__(self):
        print(f'Player join this game~~!!!')
        self.cards = []
        self.score = 0

    def draw_card(self, card):
        print(f'Player Draw Card --> {card.get_pattern()} : {card.get_score()}')
        self.cards.append(card)

    def open(self):
        for card in self.cards:
            self.score += card.get_score()

        return self.score

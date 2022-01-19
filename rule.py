class Rule:
    def __init__(self, ref_score):
        self.ref_score = ref_score
        self.player_score = 0
        self.dealer_score = 0

    def open(self, dealer, player):
        self.player_score = player.open()
        self.dealer_score = dealer.open()

    def result(self):
        print(f' === Dealer Score --> {self.dealer_score}')
        print(f' === Player Score --> {self.player_score}')
        if self.dealer_win():
            print('=== Dealer Win ~ !! ===')
        elif self.player_win():
            print('=== Player Win ~ !! ===')
        else:
            print('=== Draw Game ~ !! ===')

    def dealer_win(self):
        if self.player_score - self.ref_score > 0:
            return True

        if self.ref_score - self.dealer_score > self.ref_score - self.player_score:
            return True
        return False

    def player_win(self):
        if self.ref_score - self.dealer_score < self.ref_score - self.player_score:
            return True
        return False


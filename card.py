class Card:
    def __init__(self, pattern, score):
        self.pattern = pattern
        self.score = score

    def get_score(self):
        return self.score

    def get_pattern(self):
        return self.pattern
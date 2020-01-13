
class GloomDrawChain:
    def __init__(self):
        self.draws = {}
        self.prob = 1.0
        return

    def card_count(self, card=None):
        if card is not None:
            return self.draws.get(card) or 0
        else:
            return sum(self.draws.values())

    def draw(self, card, prob):
        self.prob = self.prob * prob
        self.last_draw = card
        if card in self.draws:
            self.draws[card] += 1
        else:
            self.draws[card] = 1
        return


class GloomDrawChain:
    def __init__(self, draws, card, prob):
        self.draws = draws.copy()
        self.last_draw = card
        self.prob = prob
        return

    def __copy__(self):
        return GloomDrawChain(self.draws.copy(), self.last_draw, self.prob)

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

    def is_equal(self, drawchain):
        return (self.draws == drawchain.draws)

    def add_chain(self, drawchain):
        self.prob += drawchain.prob
        return

    def find_equal(self, l):
        for chain in l:
            if self.is_equal(chain):
                return chain

        return None

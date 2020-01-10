
from .gloomcards import GloomCards
from .gloomdrawchain import GloomDrawChain


class GloomDeck:
    def __init__(self, deck, cards=None):
        self.deck = deck
        if cards is None:
            self.cards = GloomCards()
        else:
            self.cards = cards
        return

    def set_cards(self, cards):
        self.cards = cards
        return

    def card_count(self, card=None):
        if card is not None:
            return self.deck[card] or 0
        else:
            return sum(self.deck.values())

    def cards_left(self, drawchain, card=None):
        return self.card_count(card) - drawchain.card_count(card)

    def probability(self, card, drawchain):
        totalcards = self.cards_left(drawchain)
        remainingcards = self.cards_left(drawchain, card)
        return remainingcards / totalcards

    def empty_draw(self):
        return GloomDrawChain({}, None, 1.0)

    def can_draw(self, card, drawchain):
        return self.cards_left(drawchain, card) > 0

    def draw_next(self, drawchain):
        res = []
        for card in self.deck:
            if self.can_draw(card, drawchain):
                prob = self.probability(card, drawchain)
                new_chain = drawchain.__copy__()
                new_chain.draw(card, prob)

                res.append(new_chain)
        return res

    def is_active(self, drawchain, draw_two=False):
        if draw_two and drawchain.card_count() == 1:
            return True
        elif draw_two and drawchain.card_count() == 2:
            for card in drawchain.draws.keys():
                if not self.cards.is_rolling(card):
                    return False

        last_card = drawchain.last_draw
        return self.cards.is_rolling(last_card)

    def compress_chains(self, chains):
        compressed = []
        for chain in chains:
            equal_chain = chain.find_equal(compressed)
            if not equal_chain:
                compressed.append(chain)
            else:
                equal_chain.add_chain(chain)

        return compressed

    # Draw two if advantage or disadvantage.
    def get_all_drawchains(self, draw_two=False):
        drawchains = []
        active_chains = self.draw_next(self.empty_draw())

        while len(active_chains) > 0:
            for cur in active_chains:
                active_chains.remove(cur)
                if not self.is_active(cur, draw_two):
                    drawchains.append(cur)
                else:
                    active_chains.extend(self.draw_next(cur))

            # Compress combinations
            active_chains = self.compress_chains(
                active_chains)

        return drawchains

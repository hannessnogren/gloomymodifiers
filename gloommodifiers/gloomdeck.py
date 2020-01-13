
from .gloomcards import GloomCards
from .gloomdrawchain import GloomDrawChain
import pandas as pd
import numpy as np
import itertools as it


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

    # Return probability for card when draws drawn
    def card_probability(self, card, draws):
        return self.cards_left(draws, card) / self.cards_left(draws)

    def probability(self, draws):
        drawchain = GloomDrawChain()
        for cardname, cardcount in draws.items():
            if cardcount > self.card_count(cardname):
                return 0.0
            for i in range(cardcount):
                drawchain.draw(
                    cardname, self.card_probability(
                        cardname, drawchain))
        return drawchain.prob

    def get_all_combinations(self, draw_two=False):
        card_counts = []
        card_names = []
        terminals = []
        for cardname, cardcount in self.deck.items():
            if cardcount > 0 and self.cards.is_rolling(cardname):
                card_names.append(cardname)
                card_counts.append(range(cardcount+1))
            elif cardcount > 0:
                terminals.append(cardname)

        rolling = pd.DataFrame(it.product(*card_counts), columns=card_names)
        terminal = pd.DataFrame(np.eye(len(terminals), dtype=int),
                                columns=terminals)

        # TODO Any way to avoid these keys?
        rolling['key'] = 1
        terminal['key'] = 1
        combinations = pd.merge(
            rolling, terminal, on='key').drop(
            columns='key')

        return combinations

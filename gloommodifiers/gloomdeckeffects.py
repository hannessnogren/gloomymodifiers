
from .gloomdeck import GloomDeck
from .gloomcards import GloomCards
import pandas as pd


class GloomDeckEffects:
    def __init__(self, deck):
        self.cards = GloomCards()
        self.deck = GloomDeck(deck, self.cards)
        self.combinations = self.deck.get_all_combinations
        self.probability = self.deck.probability
        return

    def set_deck(self, deck):
        self.deck = GloomDeck(deck, self.cards)
        return

    def set_cards(self, cards):
        self.cards = cards
        self.deck.set_cards(cards)
        return

    # Get effects of single chain
    def get_row_effects(self, cards, adv=False, disadv=False):
        if (adv and disadv) or not (adv or disadv):
            return self.cards.total_effect(cards)
        elif adv:
            return self.cards.total_adv_effect(cards)
        elif disadv:
            return self.cards.total_disadv_effect(cards)
        # Unreachable
        return None

    # Get all effects as pandas df
    def get_effects(self, advantage=False, disadvantage=False):
        all_effects = []
        c = self.combinations().to_dict('index')
        for index, draws in c.items():
            effects = self.get_row_effects(draws, advantage, disadvantage)
            effects["probability"] = self.probability(draws)

            print(index, ":", draws)
            print(effects)

            all_effects.append(effects)

        return pd.DataFrame(all_effects).fillna(0)

    def get_card_combinations(self):
        return self.combinations()

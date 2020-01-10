
from .gloomdeck import GloomDeck
from .gloomcards import GloomCards
# from .gloomdrawchains import GloomDrawChain
import pandas as pd


class GloomDeckEffects:
    def __init__(self, deck):
        self.cards = GloomCards()
        self.deck = GloomDeck(deck, self.cards)
        self.drawchains = self.deck.get_all_drawchains()
        return

    def set_deck(self, deck):
        self.deck = GloomDeck(deck, self.cards)
        self.drawchains = self.deck.get_all_drawchains()
        return

    def set_cards(self, cards):
        self.cards = cards
        self.deck.set_cards(cards)
        self.drawchains = self.deck.get_all_drawchains()

    # Get effects of single chain
    def get_chain_effects(self, cards, adv=False, disadv=False):
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
        for d in self.drawchains:
            effects = self.get_chain_effects(d.draws,
                                             advantage, disadvantage).copy()
            effects["prob"] = d.prob
            all_effects.append(effects)

        return pd.DataFrame(all_effects).fillna(0)

    # Get all combinations of cards as pandas df
    def get_card_combinations(self):
        all_chains = []
        for d in self.drawchains:
            chain = d.draws.copy()
            chain["prob"] = d.prob
            all_chains.append(chain)

        return pd.DataFrame(all_chains).fillna(0)

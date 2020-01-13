
class GloomCards:
    def __init__(self):
        self.cards = {}
        # TODO Make this general
        self.add_card("zero", "normal", {"dmg": 0})
        self.add_card("minusone", "normal", {"dmg": -1})
        self.add_card("minustwo", "normal", {"dmg": -2})
        self.add_card("plusone", "normal", {"dmg": 1})
        self.add_card("plustwo", "normal", {"dmg": 2})
        self.add_card("null", "null", {"null": True})
        self.add_card("double", "double", {"double": True})
        self.add_card("rollingone", "rolling", {"dmg": 1})
        self.add_card("rollingsun", "rolling", {"element_sun": True})
        self.add_card("rollingheal", "rolling", {"heal": 1})
        self.add_card("rollingshield", "rolling", {"shield": 1})
        self.add_card("rollingstun", "rolling", {"stun": True})

    def add_card(self, name, cardtype, effect):
        self.cards[name] = {"type": cardtype, "effect": effect}
        return

    def has_card(self, cardname):
        return cardname in self.cards

    def is_rolling(self, cardname):
        if not self.has_card(cardname):
            return False
        card = self.cards[cardname]
        return card["type"] == "rolling"

    def is_null(self, cardname):
        if not self.has_card(cardname):
            return False
        card = self.cards[cardname]
        return card["type"] == "null"

    def is_double(self, cardname):
        if not self.has_card(cardname):
            return False
        card = self.cards[cardname]
        return card["type"] == "double"

    def get_rollings(self, cardnamelist):
        res = []
        for name in cardnamelist:
            if self.is_rolling(name):
                res.append(name)
        return res

    def get_terminals(self, cardnamelist):
        res = []
        for name in cardnamelist:
            if not self.is_rolling(name):
                res.append(name)
        return res

    def total_adv_effect(self, cards):
        # TODO If 2 cards, return max dmg
        # If same dmg, return first
        return

    def total_disadv_effect(self, cards):
        # TODO Only return worst card
        # If two same dmg, return first
        return

    def total_effect(self, cards):
        total_effect = {}
        for cardname, cardcount in cards.items():
            if cardcount == 0:
                continue
            if cardname not in self.cards:
                print("Card ", cardname, ":", cardcount, " not found.")
                continue

            card = self.cards[cardname]
            effects = card["effect"]
            for effect, value in effects.items():
                if type(value) in [bool, str]:
                    total_effect[effect] = value
                elif effect not in total_effect:
                    total_effect[effect] = value*cardcount
                else:
                    total_effect[effect] += value*cardcount

        return total_effect

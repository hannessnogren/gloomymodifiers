
class GloomCards:
    def __init__(self):
        self.cards = {}
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

    def total_adv_effect(self, cards):
        # TODO If 2 cards, return max
        return

    def total_disadv_effect(self, cards):
        # TODO Only keep worst card
        return

    def total_effect(self, cards):
        total_effect = {}
        for cardname in cards:
            card = self.cards[cardname]
            cardcount = cards[cardname]
            effects = card["effect"]
            for e in effects:
                self.add_effect(e, cardcount, effects[e], total_effect)

        return total_effect

    def add_effect(self, effect, count, value, l):
        if type(value) in [bool, str]:
            l[effect] = value
        elif effect not in l:
            l[effect] = value*count
        else:
            l[effect] += value*count
        return

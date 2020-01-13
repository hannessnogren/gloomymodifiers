
from gloommodifiers import GloomDeckEffects
from timeit import timeit

# Build deck and feed into class
deck = {"zero": 6,
        "minusone": 5,
        "minustwo": 1,
        "plusone": 5,
        "plustwo": 1,
        "null": 1,
        "double": 1,
        "rollingone": 0,
        "rollingsun": 0,
        "rollingheal": 0,
        "rollingshield": 0,
        "rollingstun": 0
        }

gdeck = GloomDeckEffects(deck)

combs = gdeck.get_card_combinations()
print(combs)

timeit_count = 10
t1 = timeit(lambda: gdeck.get_card_combinations(), number=timeit_count)
print("Combinations t[s]: ", t1)

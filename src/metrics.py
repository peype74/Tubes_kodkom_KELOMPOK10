import math
from collections import Counter

def entropy(text):
    frequency = Counter(text)
    total = len(text)

    ent = 0
    for freq in frequency.values():
        p = freq / total
        ent -= p * math.log2(p)

    return ent

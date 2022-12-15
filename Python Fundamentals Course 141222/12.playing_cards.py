#Exercise 2.4 (kies 5 willekeurige kaarten).
import random

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')
combined = suits, ranks
combined = list(combined)
cards = [r + s for r in ranks for s in suits]
hand = [cards.pop() for _ in range(5)]

print(hand)

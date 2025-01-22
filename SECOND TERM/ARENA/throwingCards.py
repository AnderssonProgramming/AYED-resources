from sys import stdin
from collections import deque

def throwing_cards_away(n):
    cards = deque(range(1, n+1))
    discarded_cards = []

    while len(cards) > 1:
        discarded_cards.append(cards.popleft())  # throw away the top card
        cards.rotate(-1)  # move the top card to the bottom

    return discarded_cards, cards[0]

# Read from standard input
for line in stdin:
    n = int(line.strip())
    if n == 0:
        break
    discarded, remaining = throwing_cards_away(n)
    print(f"Discarded cards: {', '.join(map(str, discarded))}")
    print("Remaining card: ",remaining)

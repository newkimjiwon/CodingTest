from collections import deque

n = int(input())

cards = deque([i for i in range(1, n + 1)])

if len(cards) > 1:
    while True:
        one = cards.popleft()
        if len(cards) == 1:
            break
        two = cards.popleft()
        if len(cards) == 0:
            cards.append(two)
            break
        cards.append(two)

print(cards[0])
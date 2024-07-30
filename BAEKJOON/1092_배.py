from collections import deque

N = int(input())
crane_1 = list(map(int, input().split()))
load = int(input())
baggage_1 = list(map(int, input().split()))

def solution(crane, baggage):
    bag = deque(baggage)
    cnt = 0

    while bag:
        crane_sum = 0
        cra = deque(crane)

        while cra and bag:
            if (cra[0] + crane_sum) < bag[0]:
                crane_sum += cra.popleft()
            else:
                bag.popleft()
                crane_sum = 0
        cnt += 1

    return cnt

print(solution(crane_1, baggage_1))
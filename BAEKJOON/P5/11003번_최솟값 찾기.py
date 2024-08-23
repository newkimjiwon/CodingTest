# 이 풀이는 PyPy3로 제출해야 정답으로 인정 됩니다!
from heapq import heappush, heappop

N, L = map(int, input().split())
arrangement = [0] + list(map(int, input().split()))

# 최소 값을 구할 힙
heap = []

for i in range(1, N + 1):
    heappush(heap, (arrangement[i], i))
    value, index = heap[0]

    while 1 <= index < i - L + 1:
        heappop(heap)
        value, index = heap[0]

    print(value, end = " ")
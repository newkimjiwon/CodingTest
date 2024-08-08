import heapq
import sys

input = sys.stdin.readline

N = int(input())
left_heap = []  # 최대 힙 (부호를 반전시켜 구현)
right_heap = []  # 최소 힙
result = []

for _ in range(N):
    number = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -number)
    else:
        heapq.heappush(right_heap, number)

    if right_heap and -left_heap[0] > right_heap[0]:
        left_val = -heapq.heappop(left_heap)
        right_val = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -right_val)
        heapq.heappush(right_heap, left_val)

    result.append(-left_heap[0])

for value in result:
    print(value)
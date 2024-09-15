import heapq
import sys

input = sys.stdin.read

n, *operations = map(int, input().split())

# 최소 힙
min_heap = []
# 결과 값
answer = []

for m in operations:
    if min_heap and m == 0:
        min_val = heapq.heappop(min_heap)
        answer.append(min_val)
    elif not min_heap and m == 0:
        answer.append(0)
    elif m != 0:
        heapq.heappush(min_heap, m)

# 결과 출력
print("\n".join(map(str, answer)))
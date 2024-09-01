import heapq

N, K = map(int, input().split())

heap = list(map(int, input().split()))

heapq.heapify(heap)

count = 1

while True:
    if count == K:
        print(heapq.heappop(heap))
        break
    heapq.heappop(heap)
    count += 1
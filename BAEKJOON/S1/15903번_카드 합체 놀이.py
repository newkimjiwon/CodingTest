import heapq


if __name__=="__main__":
    n, m = map(int, input().split())
    heaq = list(map(int, input().split()))

    heapq.heapify(heaq)

    for _ in range(m):
        x = heapq.heappop(heaq)
        y = heapq.heappop(heaq)
        heapq.heappush(heaq, x + y)
        heapq.heappush(heaq, x + y)
    
    print(sum(heaq))
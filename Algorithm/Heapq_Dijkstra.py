import heapq

INF = int(1e9)
graph = {
    1: [(2, 2), (5, 3)],
    2: [(1, 2), (4, 1), (5, 5)],
    3: [(4, 2), (7, 3)],
    4: [(2, 1), (3, 2), (5, 2), (6, 4), (8, 5)],
    5: [(1, 3), (4, 2), (8, 3)],
    6: [(4, 4), (7, 4), (8, 1)],
    7: [(3, 3), (6, 4)],
    8: [(4, 5), (5, 3), (6, 1)]
}
d = [INF] * 9

def dijkstra(start):
    d[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))  # (distance, node)

    while pq:
        distance, current = heapq.heappop(pq)

        # 이미 더 짧은 경로가 존재하면 무시
        if d[current] < distance:
            continue

        for nxt, weight in graph[current]:
            nextDistance = distance + weight
            if nextDistance < d[nxt]:
                d[nxt] = nextDistance
                heapq.heappush(pq, (nextDistance, nxt))

dijkstra(1)

for i in range(1, 9):
    print(d[i], end=' ')

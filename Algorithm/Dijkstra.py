from collections import deque

INF = 1e8
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
       pq = deque()
       pq.append((start, 0))

       while pq:
              current, distance = pq.popleft()
              distance = -distance

              if (d[current] < distance):
                     continue

              for i in range(len(graph[current])):
                     next, weight = graph[current][i]
                     nextDistance = weight + distance
                     if (nextDistance < d[next]):
                            d[next] = nextDistance
                            pq.append((next, -nextDistance))

dijkstra(1)

for i in range(1, 9):
       print(d[i], end = ' ')
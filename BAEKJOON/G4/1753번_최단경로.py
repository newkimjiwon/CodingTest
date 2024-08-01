import heapq
import sys

input = sys.stdin.read
INF = float('inf')


def dijkstra(V, E, K, edges):
    graph = [[] for _ in range(V + 1)]

    for u, v, w in edges:
        graph[u].append((v, w))

    distances = [INF] * (V + 1)
    distances[K] = 0
    pq = [(0, K)]  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(pq, (distance, adjacent))

    return distances


# Read input
data = input().split()
idx = 0

V = int(data[idx])
idx += 1
E = int(data[idx])
idx += 1
K = int(data[idx])
idx += 1

edges = []
for _ in range(E):
    u = int(data[idx])
    idx += 1
    v = int(data[idx])
    idx += 1
    w = int(data[idx])
    idx += 1
    edges.append((u, v, w))

# Run dijkstra and get the result
distances = dijkstra(V, E, K, edges)

# Print the results
for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])
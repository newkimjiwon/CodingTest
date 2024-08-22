import heapq
import sys
input = sys.stdin.readline

INF = 1e9

def dijkstra(graph, start, target):
    q = []
    heapq.heappush(q, (0, start))
    distances = [INF] * (N + 1)
    distances[start] = 0

    while q:
        current_distance, current_node = heapq.heappop(q)

        if distances[current_node] < current_distance:
            continue

        for next_node, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(q, (distance, next_node))

    return distances[target]

# 입력 처리
N = int(input())
M = int(input())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, target = map(int, input().split())

# 다익스트라 알고리즘을 사용하여 최소 비용 계산
print(dijkstra(graph, start, target))
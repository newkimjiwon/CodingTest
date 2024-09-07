import heapq

INF = int(1e9)

# 다익스트라 알고리즘
def dijkstra(graph, start, n):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        dist, current = heapq.heappop(q)

        if dist > distance[current]:
            continue

        for next_node, next_dist in graph[current]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance

# 입력 받기
N, M, X = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    current, next_node, dis = map(int, input().split())
    graph[current].append((next_node, dis))

# X로 가는 최단 거리 계산
to_X = [0] * (N + 1)
for i in range(1, N + 1):
    dist_from_i = dijkstra(graph, i, N)
    to_X[i] = dist_from_i[X]

# X에서 출발해서 각 노드로 가는 최단 거리 계산
dist_from_X = dijkstra(graph, X, N)

# 왕복 시간이 가장 오래 걸리는 경우 계산
max_time = 0
for i in range(1, N + 1):
    max_time = max(max_time, to_X[i] + dist_from_X[i])

print(max_time)
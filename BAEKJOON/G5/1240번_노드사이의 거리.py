from collections import deque

INF = 1e8

def dijkstra(start, end):
    visited = [INF] * (N + 1)
    q = deque([(start, 0)])  # 이 부분을 수정합니다

    while q:
        current, distance = q.popleft()

        if (visited[current] < distance):
            continue

        for i in range(len(graph[current])):
            next, weight = graph[current][i]
            nextDistance = weight + distance
            if next == end:
                return nextDistance
            if (nextDistance < visited[next]):
                visited[next] = nextDistance
                q.append((next, nextDistance))

    return visited[end]  # 끝까지 못 찾은 경우, INF 반환 또는 종료


# 입력 처리
N, M = map(int, input().split())

result = []
graph = { i : [] for i in range(1, N + 1)}

for _ in range(N - 1):
    x, y, dis = map(int, input().split())
    graph[x].append((y, dis))
    graph[y].append((x, dis))

for _ in range(M):
    a, b = map(int, input().split())
    result.append(int(dijkstra(a, b)))

for i in result:
    print(i)
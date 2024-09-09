from collections import deque

def bfs(graph, start, visited):
    q = deque([start])

    visited[start] = True

    while q:
        x = q.popleft()

        for i in range(len(graph[x])):
            y = graph[x][i]
            if not visited[y]:
                q.append(y)
                visited[y] = True
    
    # 자기 자신은 제외해야함
    return visited.count(True) - 1

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

print(bfs(graph, 1, visited))
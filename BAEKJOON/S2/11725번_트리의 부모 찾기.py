import sys
sys.setrecursionlimit(10**6)

def dfs(start, graph):
    stack = [start]
    visited[start] = True

    while stack:
        s = stack.pop()
        for neighbor in graph[s]:
            if not visited[neighbor]:
                visited[neighbor] = True
                result[neighbor] = s
                stack.append(neighbor)

# 노드의 개수
N = int(input())

# 그래프
graph = [[] for _ in range(N + 1)]
# 탐색한 노드 재 방문 금지
visited = [False] * (N + 1)
# 결과 값을 담을 배열
result = {i : 0 for i in range(1, N + 1)}

for _ in range(N - 1):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

dfs(1, graph)

for i in range(2, N + 1):
    print(result[i])
from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph, n, m, r):
    result = [0] * (n + 1)

    q = deque([r])  # 시작 정점

    result[r] = 1
    visit = 2

    while q:
        x = q.popleft()

        for i in range(len(graph[x])):
            if result[graph[x][i]] == 0:
                result[graph[x][i]] = visit  # 현재 방문 갱신
                visit += 1  # 다음번째
                q.append(graph[x][i])  # 다음 방문

    return result


if __name__=="__main__":
    n, m, r = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n + 1):
        graph[i].sort(reverse = True)

    answer = bfs(graph, n, m, r)

    for i in range(1, n + 1):
        print(answer[i])
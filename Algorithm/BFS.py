from collections import deque

visit = [False] * 9


def bfs(graph, start, visit):
    queue = deque([start])

    visit[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


graph = [
    [],
    [2, 5],  # 1
    [1, 4, 5],  # 2
    [4, 7],  # 3
    [2, 3, 5, 6, 8],  # 4
    [1, 2, 4, 8],  # 5
    [4, 7, 8],  # 6
    [3, 6],  # 7
    [4, 5, 6]  # 8
]

bfs(graph, 1, visit)
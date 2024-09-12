from collections import deque

def bfs(graph, start, target):
    n, m = len(graph), len(graph[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, count)
    visited[start[0]][start[1]] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y, count = queue.popleft()

        if x == target[0] and y == target[1]:
            return count

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == '1':
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    return -1

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

start = (0, 0)
target = (N - 1, M - 1)

result = bfs(maze, start, target)
print(result + 1 if result != -1 else -1)
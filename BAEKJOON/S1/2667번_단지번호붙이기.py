from collections import deque

N = int(input())
grid = []

for _ in range(N):
    line = list(map(int, input().strip()))
    grid.append(line)

visited = [[False] * N for _ in range(N)]

def bfs(grid, visited, start):
    q = deque([start])
    y, x = start
    visited[y][x] = True
    cnt = 1

    move = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    while q:
        y, x = q.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] == 1 and not visited[ny][nx]:
                cnt += 1
                q.append((ny, nx))
                visited[ny][nx] = True
    return cnt

result = []
repeat = 0

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            result.append(bfs(grid, visited, (i, j)))
            repeat += 1

print(repeat)
for i in sorted(result):
    print(i)
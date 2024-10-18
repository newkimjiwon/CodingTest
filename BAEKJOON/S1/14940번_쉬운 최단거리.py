from collections import deque

def bfs(tile, visit):
    q = deque()

    # 상하좌우로 움직여야함
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    b = False
    for i in range(len(tile)):
        for j in range(len(tile[i])):
            # 2 찾으면 종료 시킬 반복문
            if tile[i][j] == 2:
                q.append((i, j, 1))
                tile[i][j] = 0
                visit[i][j] = True
                b = True
                break
        if b:
           break

    while q:
        y, x, distance = q.popleft()

        for iy, ix in move:
            ny = iy + y
            nx = ix + x
            if 0 <= ny < len(tile) and 0 <= nx < len(tile[0]):
                if tile[ny][nx] == 1 and not visit[ny][nx]:
                    tile[ny][nx] = distance
                    visit[ny][nx] = True
                    q.append((ny, nx, distance + 1))

    for i in range(len(tile)):
        for j in range(len(tile[i])):
            if not visit[i][j] and tile[i][j] == 1:
                tile[i][j] = -1

n, m = map(int, input().split())

tile = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

bfs(tile, visited)

for t in tile:
    for i in t:
        print(i, end = ' ')
    print()
from collections import deque

def bfs():
    q = deque()
    vc = [row[:] for row in virus]

    for i in range(N):
        for j in range(M):
            if vc[i][j] == 2:
                q.append((i, j))

    while q:
        y, x = q.popleft()
        for iy, ix in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + iy, x + ix
            if 0 <= ny < N and 0 <= nx < M and vc[ny][nx] == 0:
                vc[ny][nx] = 2
                q.append((ny, nx))

    # 안전 구역(0의 개수) 세기
    return sum(row.count(0) for row in vc)

def set_wall(count):
    global max_safe_zone

    if count == 3:
        safe_zone = bfs()
        max_safe_zone = max(max_safe_zone, safe_zone)
        return

    for i in range(N):
        for j in range(M):
            if virus[i][j] == 0:
                virus[i][j] = 1
                set_wall(count + 1)
                virus[i][j] = 0

                # 가지치기: 중간에 이미 비효율적이라고 판단되면 탐색 중단
                if max_safe_zone >= sum(row.count(0) for row in virus):
                    return

N, M = map(int, input().split())

virus = [list(map(int, input().split())) for _ in range(N)]

max_safe_zone = 0
set_wall(0)
print(max_safe_zone)
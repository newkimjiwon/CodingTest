from collections import deque


# 상 하 좌 우 움직임
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution():
    n, m, k = map(int, input().split())

    block = [[0] * m for _ in range(n)]  # 블럭 생성

    visited = [[False] * m for _ in range(n)]  # 방문처리

    result = []  # 결과 값

    for _ in range(k):
        nx, ny, ix, iy = map(int, input().split())
        for y in range(ny, iy):
            for x in range(nx, ix):
                block[y][x] = 1

    for i in range(n):
        for j in range(m):
            if block[i][j] == 0 and not visited[i][j]:
                q = deque([(i, j)])

                visited[i][j] = True

                count = 1

                while q:
                    iy, ix = q.popleft()

                    for ny, nx in move:
                        y = ny + iy
                        x = nx + ix
                        if 0 <= y < n and 0 <= x < m and not visited[y][x] and block[y][x] == 0:
                            q.append((y, x))
                            visited[y][x] = True
                            count += 1

                result.append(count)

    print(len(result))

    result.sort()

    for i in result:
        print(i, end = ' ')


solution()
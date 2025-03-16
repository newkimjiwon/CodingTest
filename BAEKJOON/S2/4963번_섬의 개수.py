from collections import deque


def bfs(land, w, h):
    answer = 0

    # 대각선 포함 상 하 좌 우
    move = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    visited = [[False] * w for _ in range(h)]  # 방문 처리

    for cy in range(h):
        for cx in range(w):
            if land[cy][cx] == 1 and not visited[cy][cx]:
                visited[cy][cx] = True

                dq = deque()
                dq.append((cy, cx))

                while dq:
                    iy, ix = dq.popleft()  # pop

                    for ny, nx in move:
                        y = iy + ny
                        x = ix + nx
                        if 0 <= y < h and 0 <= x < w and not visited[y][x]:
                            if land[y][x] == 1:
                                visited[y][x] = True
                                dq.append((y, x))
                
                answer += 1


    return answer

result = []  # 결과 값

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    land = [list(map(int, input().split())) for _ in range(h)]  # 섬

    result.append(bfs(land, w, h))

for i in result:
    print(i)
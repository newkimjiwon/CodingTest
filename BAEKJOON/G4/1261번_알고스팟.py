from collections import deque


def solve(M, N):
    mazes = [list(input().strip()) for _ in range(N)]
    dist = [[float('inf')] * M for _ in range(N)]
    dq = deque()

    dq.append((0, 0))  # 데크
    dist[0][0] = 0

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 움직임

    while dq:
        y, x = dq.popleft()

        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                cost = dist[y][x] + (mazes[ny][nx] == '1')
                if cost < dist[ny][nx]:
                    dist[ny][nx] = cost
                    if mazes[ny][nx] == '0':
                        dq.appendleft((ny, nx))
                    else:
                        dq.append((ny, nx))

    return dist[N - 1][M - 1]


if __name__=="__main__":
    M, N = map(int, input().split())

    print(solve(M, N))
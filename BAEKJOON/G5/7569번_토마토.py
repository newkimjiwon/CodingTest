from collections import deque

def bfs(m, n, h, tomato):
    move = [(0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]  # 상, 하, 좌, 우, 위, 아래
    dq = deque()

    # 초기 익은 토마토 위치를 큐에 추가
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 1:
                    dq.append((i, j, k))

    total_time = 0  # 시간

    while dq:
        next_dq = deque()  # 다음날 익을 토마토를 저장할 큐
        while dq:
            ih, iy, ix = dq.popleft()  # 현재 익은 토마토 좌표

            for dz, dy, dx in move:
                nh, ny, nx = ih + dz, iy + dy, ix + dx

                if 0 <= nh < h and 0 <= ny < n and 0 <= nx < m and tomato[nh][ny][nx] == 0:
                    tomato[nh][ny][nx] = 1  # 익게 만들기
                    next_dq.append((nh, ny, nx))  # 다음날 익을 토마토 저장

        if next_dq:  # 새롭게 익은 토마토가 있으면 하루 증가
            dq = next_dq
            total_time += 1

    # 모든 토마토가 익었는지 확인
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 0:  # 아직 익지 않은 토마토가 남아있다면
                    return -1

    return total_time


def main():
    m, n, h = map(int, input().split())
    tomato = []

    for _ in range(h):
        box = []
        for _ in range(n):
            line = list(map(int, input().split()))
            box.append(line)
        tomato.append(box)

    print(bfs(m, n, h, tomato))


main()
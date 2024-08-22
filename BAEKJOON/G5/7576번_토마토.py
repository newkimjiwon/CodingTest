from collections import deque

def solution(B):
    m = len(B[0])
    n = len(B)
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()

    # 먼저 익은 토마토를 모두 큐에 넣어준다.
    for y in range(n):
        for x in range(m):
            if B[y][x] == 1:
                queue.append((y, x, 0))  # (y, x, 시간)

    # 박스 안에 있는 토마토가 모두 익을 때까지 시간을 측정한다.
    max_time = 0

    while queue:
        y, x, time = queue.popleft()
        max_time = max(max_time, time)

        for iy, ix in move:
            ny = y + iy
            nx = x + ix
            if 0 <= ny < n and 0 <= nx < m and B[ny][nx] == 0:
                B[ny][nx] = 1
                queue.append((ny, nx, time + 1))

    # 아직 익지 않은 토마토가 있는지 확인
    for row in B:
        if 0 in row:
            return -1  # 모든 토마토를 익힐 수 없는 경우

    return max_time

M, N = map(int, input().split())
box = []

for _ in range(N):
    line = list(map(int, input().split()))
    box.append(line)

print(solution(box))
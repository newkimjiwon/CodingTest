from collections import deque

def bfs(chee):
    q = deque()
    q.append((0, 0))

    time = 0

    # 이동: 오른쪽 왼쪽 위 아래
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while True:
        # 반복 제어
        count = True
        # 방문 탐색
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1  # (0, 0)은 항상 공기

        # 치즈 탐색
        while q:
            ny, nx = q.popleft()

            # 상하좌우로 이동
            for iy, ix in move:
                y = iy + ny
                x = ix + nx
                if 0 <= y < len(chee) and 0 <= x < len(chee[0]):
                    if chee[y][x] == 0 and visited[y][x] == 0:
                        q.append((y, x))
                        visited[y][x] = 1 # 공기 영역
                    elif chee[y][x] == 1 and visited[y][x] == 0:
                        # 치즈 주변 공기 체크
                        air = 0
                        for ty, tx in move:
                            ty_y = y + ty
                            tx_x = x + tx
                            if 0 <= ty_y < len(chee) and 0 <= tx_x < len(chee[0]):
                                # 안쪽에 있는 공기를 택하면 안되므로 방문했던
                                # 공기를 위주로 탐색한다.
                                if chee[ty_y][tx_x] == 0 and visited[ty_y][tx_x] == 1:
                                    air += 1
                        if air >= 2:  # 두 면 이상이 공기와 접촉한 경우
                            visited[y][x] = 2  # 녹을 치즈로 표시

        # 치즈 반영
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if visited[i][j] == 2:
                    chee[i][j] = 0
                    count = False

        # 시간 반영
        time += 1

        if count:
            break
        else:
            q.append((0, 0))

    # 마지막 시간은 빼야함
    return time - 1

n, m = map(int, input().split())

cheeze = [list(map(int, input().split())) * 1 for _ in range(n)]

print(bfs(cheeze))
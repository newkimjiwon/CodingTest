from collections import deque

# 빨간 공과 파란 공의 최단 경로를 찾는 함수
def solve(startlink, n, m):
    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 빨간 공, 파란 공, 구멍의 위치 찾기
    red_x = red_y = blue_x = blue_y = goal_x = goal_y = 0
    for i in range(n):
        for j in range(m):
            if startlink[i][j] == 'R':
                red_x, red_y = i, j
            elif startlink[i][j] == 'B':
                blue_x, blue_y = i, j
            elif startlink[i][j] == 'O':
                goal_x, goal_y = i, j

    # BFS 초기화 (큐에 (red_x, red_y, blue_x, blue_y, 이동 횟수))
    queue = deque([(red_x, red_y, blue_x, blue_y, 0)])
    visited = set()
    visited.add((red_x, red_y, blue_x, blue_y))

    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        # 이동 횟수가 10을 초과하면 실패
        if depth > 10:
            return -1

        # 빨간 공이 구멍에 들어가면 성공
        if (rx, ry) == (goal_x, goal_y):
            return depth

        # 4방향으로 공 이동
        for dx, dy in directions:
            # 빨간 공 이동
            nrx, nry, red_count = move_until_wall_or_hole(startlink, rx, ry, dx, dy)
            # 파란 공 이동
            nbx, nby, blue_count = move_until_wall_or_hole(startlink, bx, by, dx, dy)

            # 파란 공이 구멍에 들어가면 실패
            if (nbx, nby) == (goal_x, goal_y):
                continue

            # 빨간 공과 파란 공이 같은 위치에 있다면
            if (nrx, nry) == (nbx, nby):
                # 더 많이 이동한 공을 뒤로 이동
                if red_count > blue_count:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            # 이미 방문한 상태가 아니면 큐에 추가
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))

    return -1  # 모든 경우를 탐색했으나 성공하지 못한 경우

# 공이 벽이나 구멍에 닿을 때까지 이동시키는 함수
def move_until_wall_or_hole(board, x, y, dx, dy):
    count = 0
    while True:
        # 다음 위치로 이동
        nx, ny = x + dx, y + dy
        # 벽에 닿으면 멈춤
        if board[nx][ny] == '#':
            break
        # 구멍에 들어가면 멈춤
        if board[nx][ny] == 'O':
            x, y = nx, ny
            break
        # 위치 갱신
        x, y = nx, ny
        count += 1
    return x, y, count

def main():
    # 세로 크기 n, 가로 크기 m
    n, m = map(int, input().split())
    # 보드 정보 입력
    startlink = [list(input().strip()) for _ in range(n)]
    # 결과 출력
    print(solve(startlink, n, m))

main()
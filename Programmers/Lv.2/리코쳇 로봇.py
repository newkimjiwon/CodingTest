from collections import deque


def solution(board):
    move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    boards = []

    for i in board:
        boards.append(list(i))

    r_y, r_x, g_y, g_x = 0, 0, 0, 0

    for i in range(len(boards)):
        for ii in range(len(boards[0])):
            if boards[i][ii] == 'R':
                r_y, r_x = i, ii
            if boards[i][ii] == 'G':
                g_y, g_x = i, ii

    # BFS (처음 로봇 위치 y, x, 이동횟수)
    queue = deque([(r_y, r_x, 0)])
    visited = set()
    visited.add((r_y, r_x))

    while queue:
        ry, rx, depth = queue.popleft()
        
        # 도착지점에 도착
        if (ry, rx) == (g_y, g_x):
            return depth
        
        for dy, dx in move:
            nry, nrx = r_move(boards, ry, rx, dy, dx)
            if (nry, nrx) not in visited:
                visited.add((nry, nrx))
                queue.append((nry, nrx, depth + 1))

    return -1


# 로봇이 움직이는 로직
def r_move(boards, y, x, dy, dx):
    while True:
        ny, nx = y + dy, x + dx

        # 경계 밖이거나 장애물이면 현재 자리에서 멈춤
        if ny < 0 or nx < 0 or ny >= len(boards) or nx >= len(boards[0]) or boards[ny][nx] == 'D':
            return y, x

        # 한 칸 전진
        y, x = ny, nx
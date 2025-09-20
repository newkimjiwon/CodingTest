# 1) 방향 테이블 + 회전(좌/우) + 반대 방향
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

def turn_left(d):
    return {1:4, 4:2, 2:3, 3:1}[d]

def turn_right(d):
    return {1:3, 3:2, 2:4, 4:1}[d]

def reverse_dir(d):
    return {1:2, 2:1, 3:4, 4:3}[d]


# 2) 격자 회전(1-based 격자용)
def rotate_clockwise_90(grid, R, C):
    # 크기: R x C -> C x R
    res = [[0]*(R+1) for _ in range(C+1)]
    for r in range(1, R+1):
        for c in range(1, C+1):
            nr = c
            nc = R - r + 1
            res[nr][nc] = grid[r][c]
    return res, C, R  # 새 R, C

def rotate_counterclockwise_90(grid, R, C):
    res = [[0]*(R+1) for _ in range(C+1)]
    for r in range(1, R+1):
        for c in range(1, C+1):
            nr = C - c + 1
            nc = r
            res[nr][nc] = grid[r][c]
    return res, C, R


# 3) 행/열 회전(시프트)
def shift_row_right(grid, R, C, row, k=1):
    k %= C
    if k == 0: return
    tmp = [0] + [grid[row][c] for c in range(1, C+1)]
    for c in range(1, C+1):
        nc = ((c - 1 + k) % C) + 1
        grid[row][nc] = tmp[c]

def shift_col_down(grid, R, C, col, k=1):
    k %= R
    if k == 0: return
    tmp = [0] + [grid[r][col] for r in range(1, R+1)]
    for r in range(1, R+1):
        nr = ((r - 1 + k) % R) + 1
        grid[nr][col] = tmp[r]


# 4) BFS (1-based 격자, 최단거리)
from collections import deque

def bfs_grid_1based(grid, R, C, sy, sx, block_value=None):
    dist = [[-1]*(C+1) for _ in range(R+1)]
    q = deque()
    q.append((sy, sx))
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for i in range(1, 5):  # 1..4 방향
            ny, nx = y + dy[i], x + dx[i]
            if 1 <= ny <= R and 1 <= nx <= C:
                if dist[ny][nx] == -1 and (block_value is None or grid[ny][nx] != block_value):
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
    return dist  # dist[r][c] 최단거리, 도달 불가 -1


# 5) 다중 시작점 BFS(불/전염 등)
from collections import deque

def multi_bfs_1based(starts, grid, R, C, block_value=None):
    dist = [[-1]*(C+1) for _ in range(R+1)]
    q = deque()
    for (sy, sx) in starts:
        dist[sy][sx] = 0
        q.append((sy, sx))
    while q:
        y, x = q.popleft()
        for i in range(1, 5):
            ny, nx = y + dy[i], x + dx[i]
            if 1 <= ny <= R and 1 <= nx <= C:
                if dist[ny][nx] == -1 and (block_value is None or grid[ny][nx] != block_value):
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
    return dist


# 6) DFS (재귀, 1-based)
def dfs_grid_1based(grid, R, C, sy, sx, block_value=None):
    # 필요시: import sys; sys.setrecursionlimit(1_000_000)
    visited = [[False]*(C+1) for _ in range(R+1)]
    def dfs(y, x):
        visited[y][x] = True
        for i in range(1, 5):
            ny, nx = y + dy[i], x + dx[i]
            if 1 <= ny <= R and 1 <= nx <= C:
                if not visited[ny][nx] and (block_value is None or grid[ny][nx] != block_value):
                    dfs(ny, nx)
    dfs(sy, sx)
    return visited


# 7) 반사 이동(왕복) — 한 축 O(1)
def move_axis(pos, steps, dir_sign, limit):
    # dir_sign: +1(증가; 아래/오른쪽), -1(감소; 위/왼쪽)
    if limit == 1 or steps == 0:
        return pos, dir_sign
    L = limit - 1
    period = 2 * L
    x0 = pos - 1
    start = x0 if dir_sign == 1 else (2 * L - x0) % period
    x = (start + steps) % period
    if x < L:
        return 1 + x, 1
    elif x == L:
        return 1 + x, -1
    else:
        return 1 + (2 * L - x), -1

def move_one(y, x, s, d, R, C):
    if d == 1 or d == 2:  # 세로
        step = (s % (2*(R-1))) if R > 1 else 0
        sign0 = -1 if d == 1 else 1
        ny, sign = move_axis(y, step, sign0, R)
        nx = x
        nd = 1 if sign == -1 else 2
    else:                 # 가로
        step = (s % (2*(C-1))) if C > 1 else 0
        sign0 = 1 if d == 3 else -1
        nx, sign = move_axis(x, step, sign0, C)
        ny = y
        nd = 4 if sign == -1 else 3
    return ny, nx, nd
from collections import deque


def bfs(maps, start_pos, target):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    dq = deque()
    dq.append((*start_pos, 0))  # (y, x, distance)
    visited[start_pos[0]][start_pos[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while dq:
        y, x, dist = dq.popleft()

        if maps[y][x] == target:
            return dist

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols:
                if not visited[ny][nx] and maps[ny][nx] != 'X':
                    visited[ny][nx] = True
                    dq.append((ny, nx, dist + 1))

    return -1  # target에 도달하지 못한 경우


def solution(maps):
    maps = [list(row) for row in maps]

    # 시작점, 레버, 출구 위치 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    # 두 단계로 나누어 BFS 실행
    to_lever = bfs(maps, start, 'L')
    to_end = bfs(maps, lever, 'E')

    if to_lever == -1 or to_end == -1:
        return -1
    return to_lever + to_end
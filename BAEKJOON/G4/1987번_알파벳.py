from collections import deque

R, C = map(int, input().split())

board = []

for _ in range(R):
    line = list(input())
    board.append(line)

def bfs(board):
    q = deque([(0, 0)])
    s = set()
    s.add(board[0][0])

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    steps = 0

    while q:
        y, x = q.popleft()

        for iy, ix in move:
            ny = iy + y
            nx = ix + x
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] not in s:
                q.append((ny, nx))
                s.add(board[ny][nx])

        steps += 1

    return steps

print(bfs(board))
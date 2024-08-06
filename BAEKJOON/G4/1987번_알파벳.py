R, C = map(int, input().split())

board = []

for _ in range(R):
    line = list(input())
    board.append(line)

def dfs(board, y, x, visited):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_steps = 0

    for iy, ix in move:
        ny = y + iy
        nx = x + ix
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] not in visited:
            visited.add(board[ny][nx])
            max_steps = max(max_steps, dfs(board, ny, nx, visited))
            visited.remove(board[ny][nx])

    return max_steps + 1

visited = set()
visited.add(board[0][0])
print(dfs(board, 0, 0, visited))
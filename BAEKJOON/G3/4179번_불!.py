from collections import deque
import sys

def bfs(mazes):
    R = len(mazes)
    C = len(mazes[0])
    
    # 지훈이와 불의 위치를 각각 다른 큐에 저장합니다.
    fire_q = deque()
    jihun_q = deque()
    visited = [[False] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if mazes[r][c] == 'J':
                jihun_q.append((r, c, 0))
                visited[r][c] = True
            elif mazes[r][c] == 'F':
                fire_q.append((r, c))
                
    time = 0
    while jihun_q:
        time += 1
        
        # 1. 불을 먼저 확산시킵니다.
        size_f = len(fire_q)
        for _ in range(size_f):
            y, x = fire_q.popleft()
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < R and 0 <= nx < C and mazes[ny][nx] != '#' and mazes[ny][nx] != 'F':
                    mazes[ny][nx] = 'F'
                    fire_q.append((ny, nx))
        
        # 2. 불이 번진 후, 지훈이를 이동시킵니다.
        size_j = len(jihun_q)
        for _ in range(size_j):
            y, x, count = jihun_q.popleft()
            
            # 탈출 성공
            if y == 0 or y == R - 1 or x == 0 or x == C - 1:
                return count + 1
            
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = y + dy, x + dx
                
                if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                    if mazes[ny][nx] == '.':
                        visited[ny][nx] = True
                        jihun_q.append((ny, nx, count + 1))
    
    # 지훈이가 더 이상 움직일 수 없을 때
    return 'IMPOSSIBLE'


if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    
    maze = [list(sys.stdin.readline().strip()) for _ in range(R)]

    print(bfs(maze))
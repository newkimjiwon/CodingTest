from collections import deque


def bfs(maps):
    answer = []
    
    N, M = len(maps), len(maps[0])
    
    visited = [[False] * M for _ in range(N)]
    
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for iy in range(N):
        for ix in range(M):
            if maps[iy][ix] != 'X' and not visited[iy][ix]:
                result = int(maps[iy][ix])
                visited[iy][ix] = True
                
                dq = deque()
                dq.append((iy, ix))
                
                while dq:
                    qy, qx = dq.popleft()
                    
                    for dy, dx in move:
                        y, x = qy + dy, qx + dx
                        if 0 <= y < N and 0 <= x < M and not visited[y][x]:
                            if maps[y][x] != 'X':
                                visited[y][x] = True
                                result += int(maps[y][x])
                                dq.append((y, x))
                answer.append(result)
                
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
    
                
    
def solution(maps):
    answer = []
    
    maps = [list(i) for i in maps]
    
    answer = bfs(maps)
    
    return answer
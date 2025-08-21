from collections import deque


def solution(lees, iy, ix):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 큐 2개로 분리: 물의 확장을 먼저 처리하기 위함
    water_dq = deque()
    hedgehog_dq = deque()
    
    # 방문 여부를 기록할 배열 (무한 루프 방지)
    visited = [[False] * ix for _ in range(iy)]
    
    for r in range(iy):
        for c in range(ix):
            if lees[r][c] == '*':
                water_dq.append((r, c))
                visited[r][c] = True
            elif lees[r][c] == 'S':
                hedgehog_dq.append((r, c, 0)) # y, x, 시간
                visited[r][c] = True
    
    while hedgehog_dq:
        # 1. 물 확장 (현재 시간 단계의 물만 확장)
        water_size = len(water_dq)
        for _ in range(water_size):
            wy, wx = water_dq.popleft()
            for ky, kx in move:
                ny, nx = wy + ky, wx + kx
                if 0 <= ny < iy and 0 <= nx < ix and lees[ny][nx] == '.':
                    lees[ny][nx] = '*'
                    water_dq.append((ny, nx))
        
        # 2. 고슴도치 이동 (현재 시간 단계의 고슴치만 이동)
        hedgehog_size = len(hedgehog_dq)
        for _ in range(hedgehog_size):
            hy, hx, time = hedgehog_dq.popleft()
            for ky, kx in move:
                ny, nx = hy + ky, hx + kx
                
                # 비버의 굴에 도착했으면 바로 반환
                if 0 <= ny < iy and 0 <= nx < ix and lees[ny][nx] == 'D':
                    return time + 1
                
                # 이동 가능한 조건: 범위 내, 빈 칸('.'), 아직 방문하지 않음
                if 0 <= ny < iy and 0 <= nx < ix and lees[ny][nx] == '.' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    hedgehog_dq.append((ny, nx, time + 1))
    
    return "KAKTUS"


if __name__=="__main__":
    r, c = map(int, input().split())

    lee = [list(input()) for _ in range(r)]

    print(solution(lee, r, c))
    """
    print(solution([['D', '.', '*'],
                    ['.', '.', '.'],
                    ['.', 'S', '.']], 3, 3))
    
    print(solution([['D', '.', '.', '.', '*', '.'],
                    ['.', 'X', '.', 'X', '.', '.'],
                    ['.', '.', '.', '.', 'S', '.']], 3, 6))
    """
    
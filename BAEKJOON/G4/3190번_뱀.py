# 3190번 뱀

from collections import deque


def solution():
    N = int(input())
    board = [[0]*(N+1) for _ in range(N+1)]
    
    K = int(input())
    for _ in range(K):
        r, c = map(int, input().split())
        board[r][c] = 1  # 사과
    
    L = int(input())
    turns = deque()
    for _ in range(L):
        X, C = input().split()
        turns.append((int(X), C))
    
    # 방향: 0 = 오른쪽, 1 = 아래, 2 = 왼쪽, 3 = 위
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direction = 0

    snake = deque()  # 뱀 배열
    snake.append((1,1))
    board[1][1] = 2  # 뱀 위치 표시

    time = 0

    while True:
        time += 1
        
        # 현재 머리
        hr, hc = snake[-1]
        nr = hr + dr[direction]
        nc = hc + dc[direction]

        # 1) 벽 충돌 체크
        if nr < 1 or nr > N or nc < 1 or nc > N:
            return time
        
        # 2) 자기 몸 충돌 체크
        if board[nr][nc] == 2:
            return time
        
        # 3) 이동
        if board[nr][nc] == 1:  # 사과 O → 머리만 늘림
            board[nr][nc] = 2
            snake.append((nr, nc))
        else:  # 사과 X → 꼬리 이동
            board[nr][nc] = 2
            snake.append((nr, nc))
            tr, tc = snake.popleft()
            board[tr][tc] = 0

        # 4) 방향 전환 처리
        if turns and time == turns[0][0]:
            _, c = turns.popleft()
            if c == 'L':  # 왼쪽 회전
                direction = (direction - 1) % 4
            else:         # 오른쪽 회전
                direction = (direction + 1) % 4


if __name__ == "__main__":
    print(solution())
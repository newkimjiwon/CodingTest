# d: 1=위, 2=아래, 3=오른쪽, 4=왼쪽
dy = [0, -1, 1, 0, 0]
dx = [0,  0, 0, 1,-1]


def reverse_dir(d):  # 방향 전환
    return 2 if d == 1 else 1 if d == 2 else 4 if d == 3 else 3


def move_shark(fishing, R, C):
    # fishing[r][c]는 "상어들의 리스트" 각 상어는 [z, s, d] 정보를 갖는다.
    g = [[[] for _ in range(C + 1)] for _ in range(R + 1)]

    for rr in range(1, R + 1):
        for cc in range(1, C + 1):
            if not fishing[rr][cc]:
                continue
            
            # 이 칸의 모든 상어 이동
            for z, s, d in fishing[rr][cc]:
                y, x = rr, cc

                # 속도 주기 축소
                if d == 1 or d == 2:   # 세로
                    steps = (s % (2 * (R - 1))) if R > 1 else 0
                else:                  # 가로
                    steps = (s % (2 * (C - 1))) if C > 1 else 0

                while steps:
                    ny, nx = y + dy[d], x + dx[d]
                    # 다음 칸이 범위를 벗어나면 방향만 바꾸고 재시도
                    if not (1 <= ny <= R and 1 <= nx <= C):
                        d = reverse_dir(d)
                        continue
                    y, x = ny, nx
                    steps -= 1

                g[y][x].append([z, s, d])

    return g  # 새로운 상어 배열을 반환


if __name__=="__main__":
    R, C, M = map(int, input().split())  # 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)

    fishing = [[[] for _ in range(C + 1)] for _ in range(R + 1)]  # 상어
    
    for _ in range(M):
        # 상어의 위치, z는 크기, s는 속력, d는 이동 방향이다
        r, c, s, d, z = map(int, input().split())
        fishing[r][c].append([z, s, d])  # 상어 정보를 배열에 넣는다

    # 잡은 양
    eat_count = 0

    # 시뮬레이션 시작
    for col in range(1, C + 1):
        # 1) 이 열에서 가장 위(r가 작은) 상어를 잡는다
        for row in range(1, R + 1):
            if fishing[row][col]:
                z, s, d = fishing[row][col][0]
                eat_count += z
                fishing[row][col] = []
                break

        # 2. 상어를 움직인다
        fishing = move_shark(fishing, R, C)

        # 3. 같은 배열에 상어가 있는 경우 잡아 먹는다.
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                # 상어가 있을 때
                if fishing[r][c]:
                    # 내림차순으로 size(Z)가 가장 큰 상어를 살린다.
                    if len(fishing[r][c]) >= 2:
                        # 크기 z 기준 내림차순 정렬 후 하나만 남김
                        fishing[r][c].sort(key=lambda t: t[0], reverse=True)
                        fishing[r][c] = [fishing[r][c][0]]
    
    print(eat_count)
import sys
input = sys.stdin.readline

# d: 1=위, 2=아래, 3=오른쪽, 4=왼쪽

def move_axis(pos, s, dir_sign, limit):
    """
    1D 반사 이동을 O(1)로 계산
    pos: 1..limit
    s: 이동 칸 수(축 주기로 이미 축소해둘 것)
    dir_sign: +1(아래/오른쪽), -1(위/왼쪽)
    limit: 축 길이 (R 또는 C)
    return: (새 위치, '다음 턴'에 사용할 방향 부호)
    """
    if limit == 1 or s == 0:
        return pos, dir_sign

    L = limit - 1
    period = 2 * L

    # 0..L의 좌표계를 정방향(+1) 기준으로 변환
    x0 = pos - 1
    start = x0 if dir_sign == +1 else (2 * L - x0) % period

    x = (start + s) % period

    if x <= L:
        # 증가 구간
        new_pos = 1 + x
        # 벽(x==L)에 정확히 도달하면 다음 턴은 반대(-1)
        new_dir = +1 if x < L else -1
    else:
        # 감소 구간
        x2 = 2 * L - x
        new_pos = 1 + x2
        new_dir = -1
    return new_pos, new_dir

def solve():
    R, C, M = map(int, input().split())
    grid = [[0] * (C + 1) for _ in range(R + 1)]  # 1-based
    sharks = [None] * (M + 1)                     # [r, c, s, d, z]
    alive  = [False] * (M + 1)

    for i in range(1, M + 1):
        r, c, s, d, z = map(int, input().split())
        sharks[i] = [r, c, s, d, z]
        alive[i]  = True
        grid[r][c] = i

    # 축 주기로 속도 축소 (세로: 2*(R-1), 가로: 2*(C-1))
    for i in range(1, M + 1):
        if not alive[i]:
            continue
        r, c, s, d, z = sharks[i]
        if d in (1, 2):
            sharks[i][2] = s % ((R - 1) * 2) if R > 1 else 0
        else:
            sharks[i][2] = s % ((C - 1) * 2) if C > 1 else 0

    ans = 0
    # 낚시왕이 열 1..C로 이동
    for col in range(1, C + 1):
        # 1) 포획: 해당 열에서 가장 위(r가 작은) 상어
        for row in range(1, R + 1):
            sid = grid[row][col]
            if sid and alive[sid]:
                ans += sharks[sid][4]  # z
                alive[sid] = False
                grid[row][col] = 0
                break

        # 2) 상어 이동 후 충돌 처리
        new_grid = [[0] * (C + 1) for _ in range(R + 1)]
        for sid in range(1, M + 1):
            if not alive[sid]:
                continue
            r, c, s, d, z = sharks[sid]

            if d == 1:      # 위
                nr, sign = move_axis(r, s, -1, R)
                nc = c
                nd = 1 if sign == -1 else 2
            elif d == 2:    # 아래
                nr, sign = move_axis(r, s, +1, R)
                nc = c
                nd = 1 if sign == -1 else 2
            elif d == 3:    # 오른쪽
                nc, sign = move_axis(c, s, +1, C)
                nr = r
                nd = 4 if sign == -1 else 3
            else:           # 왼쪽
                nc, sign = move_axis(c, s, -1, C)
                nr = r
                nd = 4 if sign == -1 else 3

            other = new_grid[nr][nc]
            if other == 0:
                new_grid[nr][nc] = sid
                sharks[sid] = [nr, nc, s, nd, z]
            else:
                # 큰 상어만 생존
                if sharks[other][4] < z:
                    alive[other] = False
                    new_grid[nr][nc] = sid
                    sharks[sid] = [nr, nc, s, nd, z]
                else:
                    alive[sid] = False

        grid = new_grid

    print(ans)

if __name__ == "__main__":
    solve()

# 파이프 이동 방향
directions = {
    1: [(0, 1, 1), (1, 1, 3)],  # 가로 상태
    2: [(1, 0, 2), (1, 1, 3)],  # 세로 상태
    3: [(0, 1, 1), (1, 0, 2), (1, 1, 3)]  # 대각선 상태
}


def search_with_memoization(home, n, current_status, r, c, dp):
    # 이미 도착점에 도달한 경우
    if r == n - 1 and c == n - 1:
        return 1

    # 메모이제이션 값이 존재하면 반환
    if dp[current_status][r][c] != -1:
        return dp[current_status][r][c]

    # 초기 경우의 수
    dp[current_status][r][c] = 0

    # 현재 상태에서 다음 상태 확인
    for dr, dc, new_state in directions[current_status]:
        nr, nc = r + dr, c + dc

        # 다음 상태에 탐색 가능 여부 확인
        if is_valid(home, n, current_status, r, c, dr, dc):
            dp[current_status][r][c] += search_with_memoization(home, n, new_state, nr, nc, dp)

    return dp[current_status][r][c]


# 유효성 검사
def is_valid(home, n, current_status, r, c, dr, dc):
    # 다음 탐색에 충돌이 발생하는 부분이 있는지 확인
    nr, nc = r + dr, c + dc

    # 벽에 부딪치면 더 이상 이동 불가능 판단
    # 범위 확인
    if nr < 0 or nc < 0 or nr >= n or nc >= n:
        return False

    # 대각선 이동인 경우
    if dr == 1 and dc == 1:
        if home[r][c + 1] == 1 or home[r + 1][c] == 1 or home[nr][nc] == 1:
            return False
    else:
        if home[nr][nc] == 1:
            return False

    return True


def main():
    # 집의 크기
    n = int(input())
    home = [list(map(int, input().split())) for _ in range(n)]

    # 초기 상태
    initial_status = 1

    # DP 테이블 초기화 (-1로 초기화)
    dp = [[[-1] * n for _ in range(n)] for _ in range(4)]

    # 탐색 시작
    answer = search_with_memoization(home, n, initial_status, 0, 1, dp)
    print(answer)


if __name__ == "__main__":
    main()

import sys

def main():
    n = int(sys.stdin.readline())
    home = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    INF = int(1e9)
    result = INF

    # 0: R, 1: G, 2: B
    for first_color in range(3):
        dp = [[INF] * 3 for _ in range(n)]
        # 첫 번째 집은 첫 색만 선택 가능
        dp[0][first_color] = home[0][first_color]

        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + home[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + home[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + home[i][2]

        # 마지막 집은 첫 번째 색과 다른 색만 고려
        for last_color in range(3):
            if last_color != first_color:
                result = min(result, dp[n-1][last_color])

    print(result)


if __name__ == "__main__":
    main()
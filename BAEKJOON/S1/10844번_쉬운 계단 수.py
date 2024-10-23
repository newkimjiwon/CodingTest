MOD = 1000000000

def solution(n):
    dp = [[0] * 10 for _ in range(n + 1)]

    # 길이가 1인 계단 수 초기화
    for j in range(1, 10):
        dp[1][j] = 1

    # DP 계산
    for i in range(2, n + 1):
        for j in range(10):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < 9:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD

    # 길이가 n인 계단 수의 총합
    result = sum(dp[n]) % MOD
    return result


n = int(input())
print(solution(n))
# 다이나믹 프로그래밍
def solution(N):
    dp = [0] * (N + 1)

    if N >= 0:
        dp[0] = 0
    if N >= 1:
        dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

n = int(input())

print(solution(n))
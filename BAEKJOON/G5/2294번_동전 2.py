# 동적 계획법
def solution(k, coins):
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[k] if dp[k] != float('inf') else -1


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

print(solution(k, coins))
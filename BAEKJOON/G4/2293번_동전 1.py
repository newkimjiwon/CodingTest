n, m = map(int, input().split())

coins = [int(input()) * 1 for _ in range(n)]

coins.sort()

dp = [0] * (m + 1)
dp[0] = 1
for c in coins:
    for i in range(c, m + 1):
        dp[i] += dp[i - c]
print(dp[m])
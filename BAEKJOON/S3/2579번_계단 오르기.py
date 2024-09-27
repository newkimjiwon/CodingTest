n = int(input())

stairs = [0] * 301
dp = [0] * 301

for i in range(1, n + 1):
    s = int(input())
    stairs[i] = s

dp[1] = stairs[1]
dp[2] = stairs[2] + dp[1]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])
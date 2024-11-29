n = int(input())  # 포도주 잔의 개수

# 포도주 양 입력
wine = [int(input()) for _ in range(n)]

# dp 배열 초기화
dp = [0] * (n + 1)

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

    print(dp[n - 1])
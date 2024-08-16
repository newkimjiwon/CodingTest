# 다이나믹 프로그래밍
def solution(N):
    dp = [0] * (N + 1)

    # 초기 값으로 필수다
    if N >= 2:
        dp[2] = 1
    if N >= 3:
        dp[3] = 1

    # 나눴을 때 점화식에 존재하는 값을 가져와서 더해주면 된다.
    for i in range(4, N + 1):
        if i % 3 != 0 and i % 2 == 0:
            check = min(dp[i - 1], dp[i // 2])
            dp[i] = 1 + check
        elif i % 3 == 0 and i % 2 != 0:
            check = min(dp[i - 1], dp[i // 3])
            dp[i] = 1 + check
        elif i % 3 == 0 and i % 2 == 0:
            check = min(dp[i - 1], dp[i // 3], dp[i // 2])
            dp[i] = 1 + check
        else:
            check = dp[i - 1]
            dp[i] = 1 + check

    return dp[N]

n = int(input())

print(solution(n))
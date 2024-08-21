def solution(N):
    dp = [0] * (N + 1)

    dp[1] = 1
    dp[2] = 1

    if N == 1:
        return 1
    elif N == 2:
        return 1
    
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

N = int(input())
print(solution(N))
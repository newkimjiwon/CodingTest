def solution(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 3
    if n >= 3:
        dp[3] = 5
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + (dp[i - 2] * 2)
    
    return dp[n] % 10007


def main():
    n = int(input())

    print(solution(n))


main()
def solution(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 1
    if n >= 3:
        dp[3] = 2
    if n >= 4:
        dp[4] = 3

    for i in range(5, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2])

    return dp[n]


def main():
    n = int(input())  # 숫자

    print(solution(n))


main()
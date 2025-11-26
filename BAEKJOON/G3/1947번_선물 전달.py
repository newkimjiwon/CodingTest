def solution(N):
    dp = [0] * (N + 1)  # 사람 수

    if N >= 1:
        dp[1] = 0
    if N >= 2:
        dp[2] = 1
    if N >= 3:
        dp[3] = 2

    for i in range(4, N + 1):
        dp[i] = ((i - 1) * (dp[i - 1] + dp[i - 2])) % 1000000000

    return dp[N]


def main():
    N = int(input())

    print(solution(N))


if __name__=="__main__":
    main()
def fi(n):
    dp = [0] * (n + 2)

    if n >= 0:
        dp[0] = 0
    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def main():
    n = int(input())

    print(fi(n))


if __name__=="__main__":
    main()
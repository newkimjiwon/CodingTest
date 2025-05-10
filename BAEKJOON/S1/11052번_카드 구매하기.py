def main():
    # 카드 개수
    n = int(input())
    # 카드 팩
    p = list(map(int, input().split()))

    # dp
    dp = [0] * (n + 1)

    for i in range(1, n + 1):           # i는 현재 만들고자 하는 카드 개수
        for j in range(1, i + 1):       # j는 카드팩에 들어있는 카드 개수
            dp[i] = max(dp[i], dp[i - j] + p[j - 1])

    print(dp[n])


if __name__=="__main__":
    main()
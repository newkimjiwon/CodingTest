def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 3

    if n > 1:  # 초기값
        dp[2] = 7

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901  # Dp

    return dp[n]  # 결과 값


def main():
    n = int(input())  # 케이지 수

    print(solution(n))


if __name__=="__main__":
    main()
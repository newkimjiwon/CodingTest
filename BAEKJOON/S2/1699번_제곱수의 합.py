import math


def min_square_sum(n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = i  # 최악의 경우: 1^2로만 이루어진 경우
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)

    return dp[n]


def main():
    # 예시 실행
    n = int(input())
    print(min_square_sum(n))

if __name__=="__main__":
    main()
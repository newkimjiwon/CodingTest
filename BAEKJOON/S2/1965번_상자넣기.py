def solution(n, boxs):
    # dp[i]: boxs[i]를 마지막으로 사용하는 가장 긴 증가 부분 수열의 길이
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if boxs[j] < boxs[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main():
    n = int(input())
    boxs = list(map(int, input().split()))
    print(solution(n, boxs))


if __name__ == "__main__":
    main()
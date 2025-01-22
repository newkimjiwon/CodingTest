
def solution(n):
    MOD = 10007  # 모듈러 값
    answer = 0

    # dp 초기화
    dp = [[0] * 10 for _ in range(n + 1)]

    # 초기값 부여
    for i in range(10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(10):
            for k in range(j, 10):
                dp[i][j] += dp[i - 1][k]
                dp[i][j] %= MOD  # 모듈러 연산 적용

    # 길이가 n인 모든 오르막 수의 합
    answer = sum(dp[n]) % MOD

    return answer


def main():
    # 길이 n를 입력
    n = int(input())

    print(solution(n))


main()
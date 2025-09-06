def solution(k, n):
    # 아파트 층수(k)와 호수(n)를 고려하여 2차원 배열 초기화
    # dp[i][j]는 i층 j호에 사는 사람의 수
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # 0층의 거주민 수 초기화 (0층의 i호에는 i명이 산다)
    for i in range(1, n + 1):
        dp[0][i] = i

    # 1층부터 k층까지 반복
    for i in range(1, k + 1):
        # 각 층의 1호부터 n호까지 반복
        for j in range(1, n + 1):
            # i층 j호의 거주민 수는 (i-1)층의 1호부터 j호까지의 합
            dp[i][j] = sum(dp[i-1][:j+1])

    return dp[k][n]


if __name__=="__main__":
    t = int(input())

    result = []

    for _ in range(t):
        k = int(input())
        n = int(input())
        result.append(solution(k, n))

    for i in result:
        print(i)
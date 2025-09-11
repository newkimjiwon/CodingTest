def solution(n, k):
    MOD = 1000000000

    # dp[i][j]: i개의 숫자로 합 j를 만드는 경우의 수
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # 초기값 설정: 0을 만드는 경우의 수는 항상 1가지 (모두 0)
    for i in range(k + 1):
        dp[i][0] = 1
    
    # 2중 반복문으로 DP 테이블 채우기
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            # 점화식 적용
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
            
    # k개의 수로 합 n을 만드는 경우의 수 반환
    return dp[k][n]


if __name__=='__main__':
    N, K = map(int, input().split())
    print(solution(N, K))
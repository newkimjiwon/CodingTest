def tile_filling(n):
    # N이 홀수이면 3xN 벽을 1x2, 2x1 타일로 채울 수 없습니다.
    if n % 2 != 0:
        return 0

    # DP 테이블 초기화. dp[i]는 3xi 벽을 채우는 경우의 수
    dp = [0] * (n + 1)
    
    # 기본 경우의 수 설정
    dp[0] = 1 # 3x0 벽을 채우는 경우의 수는 1가지 (아무것도 하지 않는 경우)
    dp[2] = 3 # N=2일 때의 경우의 수 (문제에서 제시한 값)
    
    # 동적 계획법을 사용하여 N까지 계산
    for i in range(4, n + 1, 2):
        dp[i] = (3 * dp[i - 2]) + (sum(dp[0:i - 2]) * 2)
        
    return dp[n]

N = int(input())
result = tile_filling(N)
print(result)
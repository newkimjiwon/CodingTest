def find_min_operations(N):
    # dp[i] = i를 1로 만들기 위한 최소 연산 횟수
    dp = [0] * (N + 1)
    # prev[i] = i에서 연산 후 가게 되는 숫자 (경로 추적용)
    prev = [0] * (N + 1)
    
    for i in range(2, N + 1):
        # 1을 빼는 연산
        dp[i] = dp[i-1] + 1
        prev[i] = i - 1
        
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
            dp[i] = dp[i//2] + 1
            prev[i] = i // 2
            
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
            dp[i] = dp[i//3] + 1
            prev[i] = i // 3
    
    # 경로 역추적
    path = []
    current = N
    while current >= 1:
        path.append(current)
        current = prev[current]
    
    return dp[N], path

# 입력 처리
N = int(input())
min_operations, path = find_min_operations(N)

# 출력
print(min_operations)
print(' '.join(map(str, path)))
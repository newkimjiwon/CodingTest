# 다이나믹 프로그래밍
def solution(N):
    dp = [0] * (N + 1)

    # 점화식 dp[N] = dp[N - 1] + dp[N - 2] + dp[N - 3]
    dp[0] = 1
    if N >= 1:
        dp[1] = 1
    if N >= 2:
        dp[2] = 2
    if N >= 3:
        dp[3] = 4

    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[N]

# 테스트 개수
T = int(input())

# 테스트 결과 값 담는 곳
result = []

for _ in range(T):
    n = int(input())
    result.append(solution(n))

# 결과 값 출력
for i in result:
    print(i)
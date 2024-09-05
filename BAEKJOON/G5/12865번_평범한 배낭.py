def solution(bp, k):
    # dp[i]는 무게가 i일 때 최대 가치
    dp = [0] * (k + 1)

    # 각 물건에 대해
    for weight, value in bp:
        # 현재 배낭 용량에서 물건을 넣었을 때의 가치를 갱신
        for i in range(k, weight - 1, -1):
            dp[i] = max(dp[i], dp[i - weight] + value)

    # dp[k]에 저장된 값이 최대 가치
    return dp[k]

N, K = map(int, input().split())

backpack = [list(map(int, input().split())) for _ in range(N)]

print(solution(backpack, K))
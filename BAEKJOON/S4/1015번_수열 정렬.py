def solution(p):
    dp = [0] * n
    # 가장 큰 값을 찾는다.
    max_value = max(p)

    count = 0

    for i in range(1, max_value + 1):
        for j in range(len(dp)):
            if p[j] == i:
                dp[j] = count
                count += 1

    return dp

# 개수를 입력하는 n
n = int(input())

# 배열
p = list(map(int, input().split()))

print(' '.join(map(str, solution(p))))
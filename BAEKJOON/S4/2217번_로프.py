# 로프의 개수
n = int(input())

# dp
dp = [0] * 100001
# 로프를 저장하는 배열
rope = [int(input()) for _ in range(n)]

# 내림차순으로 저장
rope.sort(reverse = True)

# 이전 무게
current_weight = rope[0]
# 각 상황의 무게를 측정
dp[0] = rope[0]

for i in range(1, n):
    # 이후 무게
    next_weight = rope[i] * (i + 1)
    dp[i] = next_weight

# 최대 중량을 구하는 변수
max_weight = max(dp)

print(max_weight)
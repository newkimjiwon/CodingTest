N, M = map(int, input().split())
line = list(map(int, input().split()))

# 누적 합 배열 생성
prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + line[i - 1]

# 구간 합 계산 및 출력
result = []
for _ in range(M):
    i, j = map(int, input().split())
    result.append(prefix_sum[j] - prefix_sum[i - 1])

for res in result:
    print(res)

import sys

# 입력을 최적화하여 한 번에 읽기
input = sys.stdin.read

data = input().split('\n')
n = int(data[0])  # 상담 기간

c = [list(map(int, line.split())) for line in data[1:n+1]]

dp = [0] * (n + 1)  # 최대 수익을 저장할 DP 테이블

for i in range(n):
    t, p = c[i]  # 상담 기간, 금액

    # 이전 최대 수익 유지
    dp[i] = max(dp[i], dp[i - 1] if i > 0 else 0)

    # 상담을 진행할 수 있는 경우
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)

# 마지막 날까지의 최대 수익 계산
print(max(dp))
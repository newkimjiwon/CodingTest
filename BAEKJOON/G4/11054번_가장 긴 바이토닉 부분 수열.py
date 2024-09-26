n = int(input())
s = list(map(int, input().split()))

# 각 인덱스까지의 가장 긴 증가하는 부분 수열의 길이를 저장
increase_dp = [1] * n
for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

# 각 인덱스부터의 가장 긴 감소하는 부분 수열의 길이를 저장
decrease_dp = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if s[i] > s[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

# 가장 긴 바이토닉 수열의 길이를 구함
max_length = 0
for i in range(n):
    # 바이토닉 수열의 길이는 increase_dp[i] + decrease_dp[i] - 1
    max_length = max(max_length, increase_dp[i] + decrease_dp[i] - 1)

print(max_length)
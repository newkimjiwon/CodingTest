n = int(input())
data = list(map(int, input().split()))

# dp를 저장할 리스트
dp = [1] * (n + 1)

for i in range(len(data)):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
x = max(dp)

result = []
for i in range(n - 1, -1, -1):
    if dp[i] == x:
        result.append(data[i])
        x -= 1

result.reverse()

for r in result:
    print(r, end=' ')
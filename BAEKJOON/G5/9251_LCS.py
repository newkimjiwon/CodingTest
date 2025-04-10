string_a = ' ' + input()
string_b = ' ' + input()

# dp[i][j]는 string_a의 i번째 문자까지, string_b의 j번째 문자까지의 LCS 길이
dp = [[0] * len(string_b) for _ in range(len(string_a))]

for i in range(1, len(string_a)):
    for j in range(1, len(string_b)):
        if string_a[i] == string_b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])  # 또는 dp[len(string_a) - 1][len(string_b) - 1]
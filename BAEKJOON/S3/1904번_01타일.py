def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # dp[N] = dp[N-1] + dp[N-2], % 15746
    prev2 = 1  # dp[1]
    prev1 = 2  # dp[2]

    for i in range(3, n + 1):
        current = (prev1 + prev2) % 15746
        prev2 = prev1
        prev1 = current

    return prev1

if __name__ == "__main__":
    n = int(input())
    print(solution(n))
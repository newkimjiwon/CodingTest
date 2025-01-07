def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    sz = 10**6 + 5
    dp = [[0, float('inf')] for _ in range(sz)]
    dp[0] = [0, 0]  # [숫자 구성 값, 자리수 합]

    # DP 배열 채우기
    for i in range(sz):
        if dp[i][0] == 0 and i != 0:
            continue

        for digit in [3, 5, 8]:
            if i + digit < sz:
                if dp[i + digit][0] == 0 or dp[i][1] + 1 < dp[i + digit][1]:
                    dp[i + digit][0] = digit
                    dp[i + digit][1] = dp[i][1] + 1

    t = int(data[0])
    results = []

    for k in range(1, t + 1):
        n = int(data[k])
        if dp[n][0] == 0:
            results.append("-1")
            continue

        nums = []
        while n > 0:
            nums.append(dp[n][0])
            n -= dp[n][0]

        results.append("".join(map(str, reversed(nums))))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
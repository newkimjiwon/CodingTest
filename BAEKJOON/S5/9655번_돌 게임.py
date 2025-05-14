def solution():
    # 돌의 개수
    n = int(input())

    dp = [False] * (n + 4)

    """
    dp[1] = True   (상근이가 1개 가져가서 이김)
    dp[2] = False  (상근이가 1 → 창영이 1 → 상근이 없음 → 패배)
    dp[3] = True   (상근이가 3개 한 번에 가져가서 이김)
    dp[4] = False  (상근이 1 → 창영이 3 or 상근이 3 → 창영이 1 → 항상 창영 승)
    ...
    """

    dp[1] = True
    dp[2] = False
    dp[3] = True

    for i in range(4, n + 1):
        dp[i] = not dp[i - 1] or not dp[i - 3]

    print("SK" if dp[n] else "CY")


if __name__=="__main__":
    solution()
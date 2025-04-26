def solution():
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[i] = i번째까지의 수를 마지막으로 하는 증가 부분 수열의 최대 합
    dp = a[:]  # 처음에는 자기 자신이 부분 수열이므로 a[i]로 초기화

    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + a[i])

    print(max(dp))


solution()
def solution(n):
    # dp 갱신
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    # 결과 값은 10007로 나눠서 결과 출력
    return dp[n] % 10007

if __name__=="__main__":
    # n이 주어진다.
    n = int(input())

    print(solution(n))
def solution(n, m):
    # 피사노 주기 계산 (1,000,000에 대한 피사노 주기는 1,500,000입니다)
    pisano_period = 1500000
    
    # n을 피사노 주기로 나눈 나머지
    n = n % pisano_period
    
    # 피보나치 수열 계산
    if n <= 1:
        return n
    
    previous, current = 0, 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    
    return current

n = int(input().strip())
print(solution(n, 1000000))
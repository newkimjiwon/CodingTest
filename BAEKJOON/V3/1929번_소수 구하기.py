import math

def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

M, N = map(int, input().split())

# 에레토스테네스의 체
prime = [True] * (N + 1)  # 모든 수를 소수로 가정하고 초기화
# 결과 값 담는 곳
result = []

# 0과 1은 소수가 아님
prime[0] = prime[1] = False

# 소수 판별
for i in range(2, int(math.sqrt(N)) + 1):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = False

for j in range(M, N + 1):
    if prime[j]:
        result.append(j)

for re in result:
    print(re)
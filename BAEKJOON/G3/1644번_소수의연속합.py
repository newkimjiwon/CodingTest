N = int(input())

# 에라토스테네스의 체 알고리즘
isPrime = [True] * (N + 1)
isPrime[0] = isPrime[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i * 2, N + 1, i):
            isPrime[j] = False

# 소수 리스트
primes = [i for i in range(2, N + 1) if isPrime[i]]

count = 0
prime_len = len(primes)

for i in range(prime_len):
    result = 0
    for j in range(i, prime_len):
        result += primes[j]
        if result == N:
            count += 1
            break
        elif result > N:
            break

print(count)
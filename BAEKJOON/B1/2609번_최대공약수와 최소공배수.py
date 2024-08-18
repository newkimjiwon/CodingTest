def gcd(n, m):
    if n > m:
        a = n
        b = m
    else:
        a = m
        b = n

    while b != 0:
        a, b = b, a % b

    return a

def lcm(n, m):
    return (n * m) // gcd(n, m)

N, M = map(int, input().split())

print(gcd(N, M))
print(lcm(N, M))
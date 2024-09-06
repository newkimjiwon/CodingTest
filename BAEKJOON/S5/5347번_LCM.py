def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm_gcd_based(a, b):
    return abs(a * b) // gcd(a, b)

N = int(input())

result = []

for _ in range(N):
    a, b = map(int, input().split())
    result.append(lcm_gcd_based(a, b))

for i in result:
    print(i)
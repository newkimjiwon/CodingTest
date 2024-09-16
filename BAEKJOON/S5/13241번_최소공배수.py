def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm_gcd_based(a, b):
    return abs(a * b) // gcd(a, b)

a, b = map(int, input().split())

print(lcm_gcd_based(a, b))
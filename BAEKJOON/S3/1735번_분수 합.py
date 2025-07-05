# 최대 공약수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 최소공배수
def lcm_gcd_based(a, b):
    return abs(a * b) // gcd(a, b)

# 메인 함수
def main():
    a0, b0 = map(int, input().split())
    a1, b1 = map(int, input().split())

    gcd_value = lcm_gcd_based(max(b0, b1), min(b0, b1))  # 곱해야할 숫자 및 분모

    a0 *= (gcd_value // b0)  # ex) 2 * 35 // 7
    a1 *= (gcd_value // b1)  # ex) 3 * 35 // 5

    total_a = a0 + a1  # 분자

    f = gcd(max(total_a, gcd_value), min(total_a, gcd_value))

    if f == 0:
        print(total_a, gcd_value)
    else:
        print(total_a // f, gcd_value // f)


main()
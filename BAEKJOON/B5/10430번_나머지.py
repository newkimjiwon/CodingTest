def solution(a, b, c):
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print(((a % c) * (b % c)) % c)

def main():
    # 변수 3개
    a, b, c = map(int, input().split())
    solution(a, b, c)

main()
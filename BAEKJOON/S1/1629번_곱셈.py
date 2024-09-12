def solution(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    else:
        temp = solution(a, b // 2, c)
        temp = (temp * temp) % c
        if b % 2 == 0:
            return temp
        else:
            return (temp * a) % c

A, B, C = map(int, input().split())

print(solution(A, B, C))
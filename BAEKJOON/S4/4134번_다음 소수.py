import math


def prime_number(n):
    # 소수가 아니면 False, 소수면 True
    if n == 0:
        return False
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(N, numbers):
    answer = []

    for i in numbers:
        while True:
            if prime_number(i):
                answer.append(i)
                break
            i += 1

    return answer


if __name__=="__main__":
    N = int(input())
    numbers = [int(input()) for _ in range(N)]

    result = solution(N, numbers)

    for i in result:
        print(i)
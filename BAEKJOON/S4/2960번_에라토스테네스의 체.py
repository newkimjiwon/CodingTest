import math

# 소수인지 확인하는 함수
def prime_check(i):
    if i == 2:
        return True
    elif i == 3:
        return True
    for j in range(2, int(math.sqrt(i))):
        if i % j == 0:
            return False
    return True

def era(target, k):
    # 에라토스테네스의 체 배열
    prime_visit = [False] * (target + 1)
    # k번째 지워지는 수를 확인하기 위한 수
    answer = 0

    for number in range(2, target + 1):
        if prime_check(number):
            for check in range(number, target + 1, number):
                if not prime_visit[check]:
                    prime_visit[check] = True
                    answer += 1
                    if answer == k:
                        return check
     # k번째 지워지는 수가 없는 경우
    return -1

n, k = map(int, input().split())

print(era(n, k))
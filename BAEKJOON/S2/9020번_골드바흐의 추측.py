import math


# 소수를 찾는 함수
def prime_number(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    else:
        # 제곱 수의 이하로 나눴을 때 0이면 소수가 아니가.
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    # 소수임
    return True


# 1. 2 ~ 10000까지의 숫자 중 소수의 배수가 되는 숫자를 모두 제거한다.
def euclid():
    prime = [False] * (10001) # 소수 배열을 만든다. 소수는 True, 논 소수면 False

    # 에라토스테네스의 체 초기화 (2부터 10000까지 True로 설정)
    for i in range(2, 10001):
        prime[i] = True

    # 체 적용
    for num in range(2, int(math.sqrt(10000)) + 1):
        if prime[num]:
            for multiple in range(num * num, 10001, num):
                prime[multiple] = False
    
    answer = [] # 정답

    t = int(input()) # 각 테스트 케이스

    for _ in range(t):
        n = int(input())

        num1, num2 = 0, 0
        
        # N/2부터 역순으로 탐색하여 두 소수를 찾는 로직
        for i in range(n // 2, 1, -1):
            if prime[i] and prime[n - i]:
                num1 = i
                num2 = n - i
                break
        
        if num1 != 0 and num2 != 0:
            answer.append((num1, num2))
    
    for i, j in answer:
        print(i, j)


euclid()
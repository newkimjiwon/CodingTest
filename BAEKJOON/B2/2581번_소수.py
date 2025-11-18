import math

def prime_number(n):
    # 1은 소수가 아님
    if n == 1:
        return False
    
    # 2는 유일한 짝수 소수
    if n == 2:
        return True
    
    # 짝수는 2 외에 소수가 될 수 없음
    if n % 2 == 0:
        return False
        
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
            
    return True


def solution(M, N):
    answer = []

    for i in range(M, N + 1):
        if prime_number(i):
            answer.append(i)

    return answer


if __name__=="__main__":
    M = int(input())
    N = int(input())

    answer = solution(M, N)

    if answer:
        print(sum(answer))
        print(answer[0])
    else:
        print(-1)
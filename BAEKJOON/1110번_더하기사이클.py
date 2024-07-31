N = int(input())

def solution(target):
    number = target
    cnt = 0

    while True:
        sum_digits = (target // 10) + (target % 10)
        new_number = ((target % 10) * 10) + (sum_digits % 10)
        
        cnt += 1
        if new_number == number:
            return cnt
        
        target = new_number

print(solution(N))
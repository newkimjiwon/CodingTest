def solution(n):
    count = 1
    remainder = 1 % n

    while remainder != 0:
        remainder = (remainder * 10 + 1) % n
        count += 1
    
    return count


if __name__ == "__main__":
    try:
        while True:
            n = int(input())
            print(solution(n))
    except EOFError:  # 입력 끝났을 때 종료
        pass
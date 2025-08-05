def solution(arr):
    answer = [0, 0]

    check = True # True = 1, False = 3

    for i in arr:
        # * 경우는 예외
        if i == '*':
            if check:
                answer[1] = 1
                check = False
            else:
                answer[1] = 3
                check = True
            continue

        if check:
            answer[0] += int(i) * 1
            check = False
        else:
            answer[0] += int(i) * 3
            check = True

    # 훼손된 숫자 찾기 0부터 계산해야함
    for i in range(0, 10):
        result = answer[0] + (answer[1] * i)
        if result % 10 == 0:
            return i

    return -1

if __name__=="__main__":
    s = list(input())
    print(solution(s))
    # print(solution(list('9788968322*73')))
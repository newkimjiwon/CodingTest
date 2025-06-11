def solution():
    arr = list(input())  # 입력 문자열
    stack = []
    answer = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if arr[i - 1] == '(':  # 레이저인 경우
                answer += len(stack)
            else:  # 쇠막대기의 끝인 경우
                answer += 1

    print(answer)


if __name__ == "__main__":
    solution()

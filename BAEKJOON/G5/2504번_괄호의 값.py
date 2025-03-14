def solution(arr):
    answer = 0
    stack = []  # 스택을 사용할 배열
    add_value = 1  # 현재 상태를 보고 더해줄 변수

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
            add_value *= 2
        elif arr[i] == '[':
            stack.append(arr[i])
            add_value *= 3
        elif arr[i] == ')':
            if not stack or stack[-1] == '[':  # 실패
                answer = 0
                break
            if arr[i - 1] == '(':
                answer += add_value
            stack.pop()
            add_value //= 2
        elif arr[i] == ']':
            if not stack or stack[-1] == '(':  # 실패
                answer = 0
                break
            if arr[i - 1] == '[':
                answer += add_value
            stack.pop()
            add_value //= 3

    if stack:
        return 0
    else:
        return answer


def main():
    words = input()  # 올바른 괄호

    print(solution(words))


main()
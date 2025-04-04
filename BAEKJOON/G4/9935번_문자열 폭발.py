def main():
    # 문장
    syntax = input()
    # 폭발 문자열
    check = input()
    # 스택
    stack = []

    for i in syntax:
        stack.append(i)

        if len(stack) >= len(check):
            if ''.join(stack[-len(check):]) == check:
                for _ in range(len(check)):
                    stack.pop()

    if not stack:
        print('FRULA')
    else:
        print(''.join(stack))


main()
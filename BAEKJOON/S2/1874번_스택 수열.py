def solution():
    n = int(input())

    answer = []
    stack = [] # Stack
    arr = [i for i in range(n, 0, -1)] # 배열

    result = []  # 원하는 수열

    for _ in range(n):
        num = int(input())  # 원하느 수열 값 넣는 것
        result.append(num)

    idx = 0  # 인덱스

    while arr:
        current_pop = arr.pop()  # 현재 pop()

        # 기본적으로 계속 넣어야함
        stack.append(current_pop)
        answer.append('+')

        # 뒷 부분이 같은 경우
        if stack[-1] == result[idx]:
            while stack and stack[-1] == result[idx]:
                stack.pop()
                answer.append('-')
                idx += 1

    if not stack:
        for i in answer:
            print(i)
    else:
        print('NO')


solution()
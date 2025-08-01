def solution(n, arr):
    answer = [0, 0]

    max_value = 2000000001  # 정답

    # 투 포인터
    left = 0
    right = n - 1

    while left < right:
        left_value = arr[left]
        right_value = arr[right]

        current = abs(left_value + right_value)

        if current < max_value:
            max_value = current
            answer[0] = left_value
            answer[1] = right_value

        if abs(left_value) > abs(right_value):
            left += 1
        else:
            right -= 1

    print(answer[0], answer[1])


if __name__=="__main__":
    # n = int(input())
    # arr = list(map(int, input().split()))
    # solution(n, arr)

    solution(5, [-10, -3, 2, 4, 8])
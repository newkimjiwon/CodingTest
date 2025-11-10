def solution():
    n = int(input())  # 정수의 개수
    arr = list(map(int, input().split()))

    dp_plus = [1] * (n + 1)
    dp_minus = [1] * (n + 1)

    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            dp_plus[i] = dp_plus[i - 1] + 1  # 더 큰 값을 갱신
        if arr[i] <= arr[i - 1]:
            dp_minus[i] = dp_minus[i - 1] + 1  # 더 작은 값을 갱신

    plus = max(dp_plus)
    minus = max(dp_minus)

    result = max(plus, minus)

    print(result)


if __name__=="__main__":
    solution()
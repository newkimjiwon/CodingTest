def two_point(n, arr):
    result = (arr[0], arr[-1])  # 초기값
    min_result = abs(arr[0] + arr[-1])  # 절댓값 기준

    left = 0  # 왼쪽
    right = n - 1  # 오른쪽

    while left < right:
        current = arr[left] + arr[right]
        abs_current = abs(current)  # 절댓값으로 양수만 비교할 예정

        if abs_current < min_result:  # 더 작은 용액이 나오면 갱신을 해야한다.
            min_result = abs_current
            result = [arr[left], arr[right]]

        if current < 0:
            left += 1
        elif current > 0:
            right -= 1
        else:
            return [arr[left], arr[right]]  # 가장 이상적인 경우

    return result


def main():
    n = int(input())

    # 용액 배열
    array = list(map(int, input().split()))

    # 오름차순으로 정렬
    # 왼쪽이 알칼리성 중 가장 낮고 오른쪽이 산성중 가장 큰 용액 순으로 정렬이 된다.
    array.sort()

    result = two_point(n, array)

    print(result[0], result[1])


if __name__=="__main__":
    main()
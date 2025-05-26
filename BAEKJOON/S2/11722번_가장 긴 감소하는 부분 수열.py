def solution(arr):
    arr_len = len(arr)

    result = [1001]

    for i in range(arr_len):
        current = arr[i]

        # 현재 값이 result의 마지막 값보다 크면 그대로 추가
        if current < result[-1]:
            result.append(current)
        else:
            # 이분 탐색으로 교체할 위치 찾기
            left = 0
            right = len(result) - 1

            while left < right:
                mid = (left + right) // 2
                if result[mid] > current:
                    left = mid + 1
                else:
                    right = mid

            result[left] = current  # 알맞은 위치에 값 교체

    print(len(result) - 1)  # 첫 dummy 값(1001)을 제외한 길이


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    solution(arr)


if __name__ == "__main__":
    main()
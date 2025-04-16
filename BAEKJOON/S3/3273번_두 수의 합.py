def solution(n, arr, k):
    answer = 0

    arr.sort()

    left = 0
    right = n - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == k:
            left += 1
            right -= 1
            answer += 1
        elif s < k:
            left += 1
        elif s > k:
            right -= 1

    return answer


def main():
    n = int(input())

    arr = list(map(int, input().split()))

    k = int(input())

    print(solution(n, arr, k))

main()
def dis(N, arr):
    arr.sort()
    prefix = [0] * (N + 1)

    for i in range(N):
        prefix[i + 1] = prefix[i] + arr[i]

    answer = 0

    for i in range(N):
        left_sum = prefix[i]
        right_sum = prefix[N] - prefix[i + 1]

        left_count = i
        right_count = N - i - 1

        answer += arr[i] * left_count - left_sum
        answer += right_sum - arr[i] * right_count

    return answer


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    print(dis(N, arr))
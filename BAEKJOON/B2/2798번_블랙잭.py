def solution(arr, m):
    answer = 0

    for i in range(len(arr) - 2):
        for ii in range(i + 1, len(arr) - 1):
            for iii in range(ii + 1, len(arr)):
                s = arr[i] + arr[ii] + arr[iii]
                if answer < s and s <= m:
                    answer = s

    return answer


if __name__=="__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(arr, m))
    # print(solution([5, 6, 7, 8, 9], 21))
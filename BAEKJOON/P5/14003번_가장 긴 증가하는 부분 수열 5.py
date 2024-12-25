def solution(a, arr):
    import bisect

    # LIS를 추적하기 위한 리스트
    lis = []
    # LIS를 복원하기 위한 경로 저장
    indices = [-1] * a
    prev = [-1] * a

    for i in range(a):
        # 이분 탐색을 통해 LIS의 위치를 찾음
        pos = bisect.bisect_left(lis, arr[i])

        if pos == len(lis):
            lis.append(arr[i])
        else:
            lis[pos] = arr[i]

        # 인덱스 추적
        indices[pos] = i
        if pos > 0:
            prev[i] = indices[pos - 1]

    # LIS 길이와 복원
    lis_length = len(lis)
    lis_seq = []
    cur = indices[lis_length - 1]
    while cur != -1:
        lis_seq.append(arr[cur])
        cur = prev[cur]

    lis_seq.reverse()
    print(lis_length)
    print(*lis_seq)

def main():
    a = int(input())
    arr_i = list(map(int, input().split()))
    solution(a, arr_i)

main()
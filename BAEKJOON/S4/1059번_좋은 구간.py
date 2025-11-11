def solution(L, S, N):
    S.sort()  # 반드시 정렬
    
    # n이 S 안에 있다면 좋은 구간은 존재하지 않음
    if N in S:
        return 0

    # n보다 작은 수 중 최댓값, n보다 큰 수 중 최솟값
    left, right = 0, 1001
    for s in S:
        if s < N:
            left = max(left, s)
        elif s > N:
            right = min(right, s)

    # 공식 적용
    return (N - left) * (right - N) - 1


def main():
    L = int(input())
    S = list(map(int, input().split()))  # 집합 S
    N = int(input())

    print(solution(L, S, N))


if __name__=='__main__':
    main()
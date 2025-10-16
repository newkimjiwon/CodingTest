def solution(M, N, x, y):
    # <x:y>가 몇 번째 해인지 구하기
    # k는 x부터 시작 (x 해는 이미 M 기준으로 맞춰져 있음)
    k = x

    while k <= M * N:  # 마지막 해는 최소공배수(lcm) = M*N보다 크지 않음
        # 현재 해(k)가 y 조건도 만족하면 정답
        if (k - y) % N == 0:
            return k
        # 아니면 M년 뒤로 건너뛰기 (x 주기가 M이므로)
        k += M

    # 끝까지 못 찾으면 존재하지 않는 해
    return -1


def main():
    T = int(input())  # 테스트 케이스

    for _ in range(T):
        M, N, x, y = map(int, input().split())   # <M:N>은 카잉 달력의 마지막 해를 나타낸다
        print(solution(M, N, x, y))


if __name__=="__main__":
    main()
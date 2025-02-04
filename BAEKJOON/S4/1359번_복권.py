import math


def lottery_probability(N, M, K):
    total_cases = math.comb(N, M)  # 전체 조합의 개수
    win_cases = 0  # 당첨될 경우의 수

    # 공통되는 개수 X가 K 이상일 경우를 계산
    for x in range(K, M + 1):
        if N - M < M - x:  # 조합이 불가능한 경우 제외
            continue
        win_cases += math.comb(M, x) * math.comb(N - M, M - x)

    # 확률 계산
    return win_cases / total_cases if total_cases > 0 else 0.0


def main():
    # 입력 받기
    n, m, k = map(int, input().split())

    # 결과 출력
    print(lottery_probability(n, m, k))


if __name__=="__main__":
    main()
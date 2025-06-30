def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    dice = list(map(int, input().split()))

    # N이 1일 때: 가장 큰 면을 바닥에 둠 (보이는 5면의 합)
    if N == 1:
        print(sum(dice) - max(dice))
        return

    # 마주보는 면 중 더 작은 값들만 사용 (A-F, B-D, C-E)
    min_pair = [
        min(dice[0], dice[5]),  # A-F
        min(dice[1], dice[4]),  # B-E
        min(dice[2], dice[3])   # C-D
    ]
    min_pair.sort()

    min1 = min_pair[0]                      # 1면만 보이는 경우
    min2 = min_pair[0] + min_pair[1]        # 2면 보이는 경우
    min3 = sum(min_pair)                    # 3면 보이는 경우

    # 주사위 면 개수 계산
    count_3 = 4                             # 꼭짓점 (3면)
    count_2 = 8 * N - 12                    # 모서리 (2면)
    count_1 = 5 * N * N - count_2 * 2 - count_3 * 3  # 나머지 외벽 (1면)

    # 총 최소합 계산
    answer = count_3 * min3 + count_2 * min2 + count_1 * min1
    print(answer)


if __name__ == "__main__":
    main()
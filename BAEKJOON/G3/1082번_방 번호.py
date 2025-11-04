def solution(N, P, M):
    dp = ["-1"] * (M + 1)
    dp[0] = ""  # 초기 상태

    for money in range(M + 1):
        if dp[money] == "-1":
            continue
        for num in range(N):
            cost = P[num]
            if money + cost <= M:
                new_num = dp[money] + str(num)
                # 0으로 시작하면 안 됨 (단, 한 자리 0은 예외)
                if new_num[0] == "0" and len(new_num) > 1:
                    continue

                # 아직 아무 숫자도 없을 때
                if dp[money + cost] == "-1":
                    dp[money + cost] = new_num
                else:
                    # 자리수 > 숫자 비교로 더 큰 번호 선택
                    dp[money + cost] = max(dp[money + cost], new_num, key=lambda x: (len(x), x))

    # dp 배열 중 만들 수 있는 것들만 비교
    candidates = [x for x in dp if x != "-1"]
    return max(candidates, key=lambda x: (len(x), x))


def main():
    N = int(input().strip())
    P = list(map(int, input().split()))
    M = int(input().strip())
    print(solution(N, P, M))


if __name__ == "__main__":
    main()
# 알고리즘
# 1. 각 열의 위/아래 스티커에 대해, 이전 열 또는 그 전 열에서 인접하지 않는 스티커 중 최대 점수를 선택하여 현재 스티커 점수와 더한다.
# 2. dp[0][i]는 i번째 열에서 위쪽 스티커를 선택했을 때의 최대 점수, dp[1][i]는 아래쪽 스티커 선택 시 최대 점수를 의미한다.
# 3. 점화식은 아래와 같다:
#    dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
#    dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]
# 4. 최종 결과는 max(dp[0][n-1], dp[1][n-1])로 구한다.


def solution(n, sticker):
    if n == 1:
        return max(sticker[0][0], sticker[1][0])
    
    dp = [[0] * n for _ in range(2)]

    # 초기값 설정
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

    return max(dp[0][n-1], dp[1][n-1])


def main():
    t = int(input())
    result = []

    for _ in range(t):
        n = int(input())
        sticker = [list(map(int, input().split())) for _ in range(2)]
        result.append(solution(n, sticker))

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
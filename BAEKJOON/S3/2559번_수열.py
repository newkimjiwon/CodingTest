def solution(n, k, temperature):
    answer = 0

    left = 1
    right = k

    # 구간의 합을 구할 배열
    dp = [0] * n

    # 첫 구간 합을 계산
    dp[k - 1] = sum(temperature[:k])
    answer = dp[k - 1]

    while right < len(temperature):
        dp[right] = dp[right - 1] - temperature[left - 1] + temperature[right]
        answer = max(answer, dp[right])
        right += 1
        left += 1

    return answer


def main():
    # 정수의 개수와 연속된 날짜의 수
    n, k = map(int, input().split())

    # 온도
    temperature = list(map(int, input().split()))

    print(solution(n, k, temperature))


main()
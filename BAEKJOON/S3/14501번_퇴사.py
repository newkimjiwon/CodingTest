def solution(schedules, len_n):
    # DP 배열 초기화 (최대 수익을 저장)
    dp = [0] * (len_n + 1)

    for day in range(len_n):
        time, profit = schedules[day]

        # 현재까지의 최대 이익을 다음 날로 넘김
        if day + 1 <= len_n:
            dp[day + 1] = max(dp[day + 1], dp[day])

        # 상담을 진행할 경우
        if day + time <= len_n:
            dp[day + time] = max(dp[day + time], dp[day] + profit)

    return max(dp)

if __name__ == "__main__":
    n = int(input())

    # 스케줄
    schedule = []
    for _ in range(n):
        t, p = map(int, input().split())
        schedule.append((t, p))

    print(solution(schedule, n))
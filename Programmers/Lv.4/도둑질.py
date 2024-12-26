def solution(money):
    home_count = len(money)

    # 첫 번째 집을 털고 마지막 집은 털지 않는 경우
    dp1 = [0] * home_count
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, home_count - 1):  # 마지막 집 제외
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫 번째 집은 털지 않고 마지막 집을 포함하는 경우
    dp2 = [0] * home_count
    dp2[0] = 0  # 첫 번째 집 제외
    dp2[1] = money[1]
    for i in range(2, home_count):  # 마지막 집 포함
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    # 두 경우의 최댓값 반환
    return max(dp1[-2], dp2[-1])
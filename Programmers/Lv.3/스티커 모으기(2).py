def solution(sticker):
    if len(sticker) == 1:  # 스티커 사이즈가 1이면 0번째를 뽑는다.
        return sticker[0]

    size = len(sticker)  # 스티커 전체 길이

    dp1 = [0] + sticker[:-1]  # dp1 1번째를 스티커를 선택했을 때

    for i in range(2, size):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    dp2 = [0] + sticker[1:]  # dp2 마지막 스티커를 선택햇을 때

    for i in range(2, size):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])

    answer = max(dp1[-1], dp2[-1])

    return answer
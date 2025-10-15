def watt(wh):
    if wh <= 100:
        return wh * 2
    elif wh <= 10000:
        return 100 * 2 + (wh - 100) * 3
    elif wh <= 1000000:
        return 100 * 2 + 9900 * 3 + (wh - 10000) * 5
    else:
        return 100 * 2 + 9900 * 3 + 990000 * 5 + (wh - 1000000) * 7


def solution(A, B):
    # 1. 총 사용량 찾기
    left, right = 0, 2 * 10**8
    total_wh = 0
    while left <= right:
        center = (left + right) // 2
        price = watt(center)
        if price < A:
            left = center + 1
        elif price > A:
            right = center - 1
        else:
            total_wh = center
            break
    if total_wh == 0:
        total_wh = right  # 탐색 종료 후 가장 가까운 값 보정

    # 2. 상근이 요금 찾기
    left, right = 0, total_wh
    while left <= right:
        my_wh = (left + right) // 2
        neighbor_wh = total_wh - my_wh
        diff = abs(watt(neighbor_wh) - watt(my_wh))

        if diff > B:
            left = my_wh + 1
        elif diff < B:
            right = my_wh - 1
        else:
            return watt(my_wh)

    return None


if __name__ == "__main__":
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        print(solution(A, B))
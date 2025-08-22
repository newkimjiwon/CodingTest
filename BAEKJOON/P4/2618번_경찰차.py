# 두 점 사이의 거리를 반환한다.
def dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

if __name__=="__main__":
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline

    n = int(input())  # 배열의 크기(도시 N)
    w = int(input())  # 사건의 개수

    start_1 = (1, 1)   # 경찰차 1 시작
    start_2 = (n, n)   # 경찰차 2 시작

    case = []          # 사건 좌표들 (0-index)
    for _ in range(w):
        a, b = map(int, input().split())
        case.append((a, b))

    # --- DP 준비: 상태는 (i, j). i, j는 각 차가 마지막으로 처리한 사건 인덱스, 아직 없음은 -1 ---
    from functools import lru_cache

    def pos1(i):
        """경찰차1의 현재 위치 (i == -1이면 시작점)"""
        return start_1 if i == -1 else case[i]

    def pos2(j):
        """경찰차2의 현재 위치 (j == -1이면 시작점)"""
        return start_2 if j == -1 else case[j]

    @lru_cache(None)
    def dp(i, j):
        """i, j: 1번/2번이 마지막으로 처리한 사건 인덱스(없으면 -1)
           반환값: 남은 사건들을 최적으로 배정했을 때의 최소 이동거리
        """
        k = max(i, j) + 1  # 다음에 처리할 사건 인덱스
        if k >= w:
            return 0

        # k번 사건을 1번 차가 처리
        cost1 = dis(pos1(i), case[k]) + dp(k, j)
        # k번 사건을 2번 차가 처리
        cost2 = dis(pos2(j), case[k]) + dp(i, k)

        return cost1 if cost1 <= cost2 else cost2

    # 최소 이동 거리
    answer = dp(-1, -1)
    print(answer)

    # --- 배정(경로) 복원 ---
    result = []

    i, j = -1, -1
    for _ in range(w):
        k = max(i, j) + 1
        # 두 선택지 비용 다시 계산 (dp 캐시를 이용해 비교)
        cost1 = dis(pos1(i), case[k]) + dp(k, j)
        cost2 = dis(pos2(j), case[k]) + dp(i, k)
        if cost1 <= cost2:
            result.append(1)
            i = k
        else:
            result.append(2)
            j = k

    # 배정 출력
    print("\n".join(map(str, result)))
import sys
input = sys.stdin.readline

INF = 10**15

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

if __name__ == "__main__":
    n, t = map(int, input().split())

    # 1-indexed 저장: (s, x, y)
    cities = [None]
    specials = []  # (x, y)만 저장
    for _ in range(n):
        s, x, y = map(int, input().split())
        cities.append((s, x, y))
        if s == 1:
            specials.append((x, y))

    # 각 도시에서 "가장 가까운 특별도시"까지의 거리 전처리
    # 특별도시가 없으면 텔레포트 경로는 사용할 수 없음(INF로 유지)
    nearest_special = [INF] * (n + 1)
    if specials:
        for i in range(1, n + 1):
            s, x, y = cities[i]
            if s == 1:
                nearest_special[i] = 0
            else:
                best = INF
                for sx, sy in specials:
                    d = abs(x - sx) + abs(y - sy)
                    if d < best:
                        best = d
                nearest_special[i] = best

    m = int(input())
    out = []
    for _ in range(m):
        a, b = map(int, input().split())
        _, x1, y1 = cities[a]
        _, x2, y2 = cities[b]

        direct = manhattan(x1, y1, x2, y2)
        via_tp = nearest_special[a] + t + nearest_special[b]  # specials 없으면 INF라 자동 배제
        out.append(str(min(direct, via_tp)))

    print("\n".join(out))

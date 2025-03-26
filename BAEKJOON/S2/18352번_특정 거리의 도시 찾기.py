import sys
from collections import deque


def dij(n, m, k, x, city):
    inf = 1e9
    # 결과
    answer = []

    distance = [inf] * (n + 1)  # 거리

    distance[x] = 0  # 시작 도시는 거리가 0이다

    dq = deque([(x, 0)])  # 시작 도시, 거리

    while dq:
        current, dis = dq.popleft()

        dis += 1  # 현재 위치에서 다른 도시 이동 비용은 +1 해야 한다

        if dis > k:  # 중간에서 k보다 더 긴 거리가 탐색되면 더이상 탐색하지 않는다.
            continue

        # city[current] = [] 형태 -> i = city[current]의 원소
        for i in city[current]:
            if dis < distance[i]:
                distance[i] = dis
                dq.append((i, dis))

    # i = city number
    for i in range(1, len(distance)):
        if distance[i] == k:
            answer.append(i)

    if answer:
        for i in answer:
            print(i)
    else:
        print(-1)


def main():
    input = sys.stdin.read
    data = list(map(int, input().split()))

    n = data[0]
    m = data[1]
    k = data[2]
    x = data[3]

    city = {i: [] for i in range(1, n + 1)}

    idx = 4
    for _ in range(m):
        a = data[idx]
        b = data[idx + 1]
        city[a].append(b)
        idx += 2

    dij(n, m, k, x, city)


main()
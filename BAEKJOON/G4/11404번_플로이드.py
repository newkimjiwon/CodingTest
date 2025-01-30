# 최대 비용
INF = int(1e9)


# 도시의 개수는 최대가 100개 이므로 100^3 < 1초(1억)으로 알고리즘을 사용할 수 있을 것이다.
# 그래프를 이용한 전체 최소 비용을 탐색한다 시간 복잡도는 O(N^3)이다.
def floyd_warshall(costs, n):
    # 그래프 갱신
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if costs[i][j] == INF:
                print('0', end = ' ')
            else:
                print(costs[i][j], end = ' ')
        print()


def main():  # main 함수에선 전체 비용을 계산할 그래프를 만든다.
    # 도시의 개수
    n = int(input())

    # 버스의 개수
    m = int(input())

    # 비용 정리
    cost = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        # 버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c
        a, b, c = map(int, input().split())
        # 같은 노선이 여러 개 주어질 경우, 더 작은 비용을 저장해야 함
        cost[a][b] = min(cost[a][b], c)

    # 자기 자신은 비용이 0이어야 한다.
    for i in range(1, n + 1):
        cost[i][i] = 0

    floyd_warshall(cost, n)


main()
import heapq


def dijkstra(graph, n, m, start, end):
    # 결과 값
    answer = []

    # 힙: (비용, 현재 위치)
    heap = [(0, start)]

    # 거리 배열: 무한대로 초기화
    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[start] = 0

    # 경로 추적을 위한 부모 테이블
    parent = [0] * (n + 1)

    while heap:
        distance, current = heapq.heappop(heap)

        # 이미 더 짧은 경로로 처리된 노드면 스킵
        if dist[current] < distance:
            continue

        for next_city, next_distance in graph[current]:
            cost = distance + next_distance
            if cost < dist[next_city]:
                dist[next_city] = cost
                parent[next_city] = current
                heapq.heappush(heap, (cost, next_city))

    # 경로 복원
    channel = []
    now = end
    while now != 0:
        channel.append(now)
        now = parent[now]
    channel.reverse()

    # 결과값 저장
    answer.append(dist[end])
    answer.append(len(channel))
    answer.append(channel)

    # 결과 출력
    print(answer[0])
    print(answer[1])
    for city in answer[2]:
        print(city, end=' ')
    print()


def main():
    n = int(input())  # 도시 개수
    m = int(input())  # 버스 개수

    # 그래프 형성
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        a, b, dis = map(int, input().split())
        graph[a].append((b, dis))  # 단방향 그래프

    # 시작과 끝
    start, end = map(int, input().split())

    dijkstra(graph, n, m, start, end)


if __name__ == "__main__":
    main()
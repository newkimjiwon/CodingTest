import heapq
from collections import defaultdict

INF = 1e8

def dijkstra(start, n, graph):
    """다익스트라 알고리즘을 사용해 start에서 모든 노드까지 최단 경로 계산"""
    distances = [INF] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]  # (현재 거리, 현재 노드)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # 이미 처리된 거리보다 크면 무시
        if current_distance > distances[current_node]:
            continue

        # 인접 노드 탐색
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def solution(n, graph, v1, v2):
    """특정 두 정점을 거치는 최단 경로 계산"""
    # 1번에서 모든 노드까지의 최단 경로
    dist_from_1 = dijkstra(1, n, graph)
    # v1에서 모든 노드까지의 최단 경로
    dist_from_v1 = dijkstra(v1, n, graph)
    # v2에서 모든 노드까지의 최단 경로
    dist_from_v2 = dijkstra(v2, n, graph)

    # 가능한 두 경로의 거리 계산
    path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]  # 1 → v1 → v2 → N
    path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]  # 1 → v2 → v1 → N

    # 두 경로 중 최단 경로 선택
    result = min(path1, path2)

    # 경로가 유효하지 않으면 -1 반환
    return result if result < INF else -1

if __name__ == "__main__":
    # 정점의 개수와 간선의 개수 입력
    n, m = map(int, input().split())

    # 그래프 생성
    graph = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 반드시 거쳐야 하는 두 정점 입력
    v1, v2 = map(int, input().split())

    # 결과 출력
    print(solution(n, graph, v1, v2))
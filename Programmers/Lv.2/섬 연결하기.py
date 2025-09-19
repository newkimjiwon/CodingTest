import heapq


def prim(graphs, start):
    answer = 0

    pq = []  # 힙
    visited = [False] * len(graphs)  # 방문처리
    seen = 0

    # 거리, 노드 순으로 삽입
    pq = [(0, start)]

    while pq and seen < len(graphs):
        c_dis, c_node = heapq.heappop(pq)

        if visited[c_node]:
            continue
        visited[c_node] = True
        seen += 1
        answer += c_dis

        for n_node, n_dis in graphs[c_node]:
            # 아직 연결하지 않았으면 추가
            if not visited[n_node]:
                heapq.heappush(pq, (n_dis, n_node))

    return answer 


def solution(n, costs):
    answer = 0

    # 그래프
    graph = {i: [] for i in range(n)}

    for a, b, c in costs:
        # 양방향
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    answer = prim(graph, 0)

    return answer
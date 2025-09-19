import heapq

INF = 10**15


def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0  # 시작 지점은 0

    heap = []
    heapq.heappush(heap, (0, start))  # 가중치, 시작 노드

    while heap:
        current_dis, current_node = heapq.heappop(heap)

        # 더 큰 경우는 제외
        if current_dis > dist[current_node]:
            continue

        for next_node, next_dis in graph[current_node]:
            # 더 작아야 탐색함
            if current_dis + next_dis < dist[next_node]:
                dist[next_node] = current_dis + next_dis
                heapq.heappush(heap, (current_dis + next_dis, next_node))

    return dist


if __name__=="__main__":
    T = int(input())

    result = []

    for _ in range(T):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        graph = {i: [] for i in range(1, n + 1)}

        for _ in range(m):
            a, b, d = map(int, input().split())
            graph[a].append((b, d))
            graph[b].append((a, d))
            # g_h는 필연적으로 지나가야함
            if (a == g and b == h) or (a == h and b == g):
                w_gh = d
        
        candidates = [int(input().strip()) for _ in range(t)]
        candidates.sort()

        # 다익스트라 3회
        distS = dijkstra(s)
        distG = dijkstra(g)
        distH = dijkstra(h)

        ans = []
        for x in candidates:
            # s->g->(g-h)->h->x  vs  s->h->(g-h)->g->x
            cand1 = distS[g] + w_gh + distH[x]
            cand2 = distS[h] + w_gh + distG[x]
            if distS[x] == min(cand1, cand2):
                ans.append(x)

        print(*ans)
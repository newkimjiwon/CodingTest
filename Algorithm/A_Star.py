import heapq

INF = float('inf')
graph = {
    1: [(2, 2), (5, 3)],
    2: [(1, 2), (4, 1), (5, 5)],
    3: [(4, 2), (7, 3)],
    4: [(2, 1), (3, 2), (5, 2), (6, 4), (8, 5)],
    5: [(1, 3), (4, 2), (8, 3)],
    6: [(4, 4), (7, 4), (8, 1)],
    7: [(3, 3), (6, 4)],
    8: [(4, 5), (5, 3), (6, 1)]
}
# g_score[i]: 시작점에서 i까지의 실제 비용 g(n)
g_score = [INF] * 9

# --- A*를 위한 휴리스틱 함수 정의 (위치 정보가 없으므로 임의로 0 반환) ---
# 실제 A* 문제에서는 이 함수가 (node, goal)을 받아 추정 비용을 반환해야 함.
def heuristic(node, goal):
    """실제 A* 구현 시 노드 위치 정보를 기반으로 목적지까지의 추정 비용 h(n)을 반환해야 함."""
    # 노드 8을 목표로 가정하고, 임의의 휴리스틱 값을 부여하거나 0을 사용.
    # 여기서는 Dijkstra와 구별하기 위해 임의의 작은 값을 부여 (h(n) >= 0 조건 충족)
    if node == goal:
        return 0
    return 1 
# -----------------------------------------------------------------

def a_star(start, goal):
    g_score[start] = 0
    
    # f(n) = g(n) + h(n)
    start_h = heuristic(start, goal)
    pq = []
    # 힙에는 (f_score, g_score, node)를 넣습니다. g_score는 갱신 확인용입니다.
    # f_score는 우선순위 결정에 사용됩니다.
    heapq.heappush(pq, (g_score[start] + start_h, g_score[start], start))

    while pq:
        f_score, g_current, current = heapq.heappop(pq)
        
        # 현재 노드의 g_score가 힙에서 꺼낸 g_score보다 작다면 무시 (이미 더 좋은 경로 발견)
        if g_score[current] < g_current:
            continue

        # 목표에 도달하면 실제 비용 g(n)을 반환 (A* 종료)
        if current == goal:
            return g_score[current]

        for nxt, weight in graph[current]:
            # g(n+1) = g(n) + cost(n, n+1)
            new_g_score = g_current + weight
            
            if new_g_score < g_score[nxt]:
                g_score[nxt] = new_g_score
                
                # f(n+1) = g(n+1) + h(n+1)
                h_nxt = heuristic(nxt, goal)
                new_f_score = new_g_score + h_nxt
                
                # 힙에는 (f_score, g_score, node)를 다시 넣습니다.
                heapq.heappush(pq, (new_f_score, new_g_score, nxt))
    
    # 목표에 도달하지 못한 경우
    return INF

# --- 실행 ---
start_node = 1
goal_node = 8
min_cost = a_star(start_node, goal_node)

# 결과 출력
print(f"시작 노드 {start_node}에서 목표 노드 {goal_node}까지의 최단 경로 비용: {min_cost}")
import sys
sys.setrecursionlimit(10**6)


# count를 파라미터에서 빼고 전역 변수로 관리
def dfs(graph, r, visit_order):
    global count  # 전역 변수 count를 사용하겠다고 선언

    # 현재 정점 r에 방문 순서 기록
    visit_order[r] = count
    
    # "전체" 카운터를 1 증가
    count += 1

    for neighbor in graph[r]:
        # 아직 방문하지 않은 정점이라면
        if visit_order[neighbor] == 0:
            dfs(graph, neighbor, visit_order)


if __name__=="__main__":
    n, m, r = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        graph[i].sort(reverse=True)

    # 방문 순서 기록 배열
    visit_order = [0] * (n + 1)
    
    # 전역 카운터 초기화
    count = 1
    
    dfs(graph, r, visit_order)

    for i in range(1, n + 1):
        print(visit_order[i])
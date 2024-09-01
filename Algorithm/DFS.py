# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True # 방문하면 순서 나타내기
    print(v)
    
    for i in graph[v]:
        if not visited[i]: # 방문 안한 노드이면
            dfs(graph, i, visited) # dfs 재귀

N, M, R = map(int, input().split())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(N + 1)]

# 방문 여부 기록
visited = [False] * (N + 1)

# 그래프 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for case in graph:
    case.sort()

# DFS 실행
dfs(graph, R, visited)

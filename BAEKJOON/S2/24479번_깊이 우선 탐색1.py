import sys
sys.setrecursionlimit(10**6)  # 재귀 한도 증가
input = sys.stdin.readline

# 방문한 순서 표시 변수
c = 1

# dfs 함수
def dfs(graph, v, visited):
    global c
    visited[v] = c # 방문하면 순서 나타내기
    
    for i in graph[v]:
        if visited[i] == 0: # 방문 안한 노드이면
            c += 1
            dfs(graph, i, visited) # dfs 재귀

N, M, R = map(int, input().split())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(N + 1)]

# 방문 여부 기록
visited = [0] * (N + 1)

# 그래프 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 노드 번호 순으로 방문하기 위해 각 리스트를 정렬
for neighbors in graph:
    neighbors.sort()

# DFS 실행
dfs(graph, R, visited)

# 결과 출력
for i in range(1, N + 1):
    print(visited[i])
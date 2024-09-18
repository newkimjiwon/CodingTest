from collections import deque
import sys

def bfs(graph, start):
    q = deque([start])
    visited[start] = True

    power = False

    while q:
        x = q.popleft()

        for next in graph[x]:
            if not visited[next]:
                power = True
                visited[next] = True
                q.append(next)
    
    return power

# 전체 입력을 한 번에 읽음
data = sys.stdin.read().split()

# 정점의 개수, 간선의 개수
n = int(data[0])
m = int(data[1])

# 그래프와 방문 배열 초기화
graph = [[] for _ in range(n + 1)]  # 1-based index 사용
visited = [False] * (n + 1)
cnt = 0

index = 2  # 입력 데이터에서 간선 시작 위치

# 그래프 연결 정보 입력
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    graph[u].append(v)
    graph[v].append(u)
    index += 2

# BFS를 이용해 각 연결 요소 탐색
for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i)
        cnt += 1

# 결과 출력
print(cnt)
from collections import deque, defaultdict

# 입력 처리
N, M = map(int, input().split())

# 그래프를 인접 리스트로 표현
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)  # A가 B를 신뢰한다는 것을 B에서 A로 간선으로 표현

def bfs(start):
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True
    count = 1

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                count += 1
    return count

# 각 컴퓨터를 시작점으로 BFS 수행
max_hacks = 0
result = []

for i in range(1, N + 1):
    hack_count = bfs(i)
    if hack_count > max_hacks:
        max_hacks = hack_count
        result = [i]
    elif hack_count == max_hacks:
        result.append(i)

# 결과 출력
result.sort()
print(" ".join(map(str, result)))
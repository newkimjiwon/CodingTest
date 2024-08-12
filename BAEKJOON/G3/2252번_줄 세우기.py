from collections import deque

def topological_sort(N, graph, indegree):
    result = []
    queue = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        # 현재 노드에서 이어진 간선을 따라가면서
        # 연결된 노드들의 진입차수를 감소시킴
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result

# 입력 처리
N, M = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 간선 정보 입력
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

# 위상 정렬 실행
result = topological_sort(N, graph, indegree)

# 결과 출력
print(" ".join(map(str, result)))
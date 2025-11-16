from collections import deque

# 방향 그래프 형태로 간선을 정의
# weight는 위상정렬에 필요 없으므로 제거
graph = {
    1: [2, 5],
    2: [4, 5],
    3: [4, 7],
    4: [5, 6, 8],
    5: [8],
    6: [7, 8],
    7: [],
    8: []
}

# 노드 개수만큼 진입차수 배열 준비
indegree = [0] * 9

# 진입차수 계산
for u in graph:
    for v in graph[u]:
        indegree[v] += 1

def topological_sort():
    q = deque()
    result = []

    # 진입차수가 0인 노드 삽입
    for i in range(1, 9):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return result

print(topological_sort())

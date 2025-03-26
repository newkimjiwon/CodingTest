from collections import deque


def bfs(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count


def solution(n, wires):
    answer = float('inf')

    for i in range(len(wires)):
        # 간선 하나 제거
        temp = wires[:i] + wires[i+1:]

        # 그래프 만들기
        graph = [[] for _ in range(n + 1)]
        for v1, v2 in temp:
            graph[v1].append(v2)
            graph[v2].append(v1)

        # BFS로 송전탑 개수 세기
        count = bfs(graph, 1, n)

        # 두 전력망의 송전탑 차이 계산
        diff = abs((n - count) - count)
        answer = min(answer, diff)

    return answer
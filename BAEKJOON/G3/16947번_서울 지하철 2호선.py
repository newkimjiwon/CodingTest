import sys 
sys.setrecursionlimit(10**6)

def round(graph, N, result, start, c_station, visited, count):
    result.append(c_station)
    visited[c_station] = True

    for n_station in graph[c_station]:
        if count >= 3 and n_station == start:
            # 순환선 찾음
            return True
        if not visited[n_station]:
            if round(graph, N, result, start, n_station, visited, count + 1):
                return True  # 찾았으면 pop() 안 하고 바로 종료
    result.pop()
    return False

from collections import deque


def dis(start, result, graph, N):
    dq = deque([(start, 1)])

    visited = [False] * (N + 1)
    visited[start] = True

    while dq:
        c_station, count = dq.popleft()

        for n_station in graph[c_station]:
            if n_station in result:
                return count
            if not visited[n_station]:
                dq.append((n_station, count + 1))
                visited[n_station] = True


if __name__=="__main__":
    N = int(input())

    graph = {i: [] for i in range(1, N + 1)}  # 노선

    for _ in range(N):
        # 순환로 만들기
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = [0] * (N + 1)  # 순환로 거리

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        result = []
        if round(graph, N, result, i, i, visited, 1) != False:
            break

    for i in range(1, N + 1):
        if i in result:
            answer[i] = 0
        else:
            answer[i] = dis(i, result, graph, N)

    for i in range(1, N + 1):
        print(answer[i], end = ' ')
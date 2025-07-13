from collections import deque
import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(graph, r, n):
    visited_order = [0] * (n + 1)  # 방문 순서 저장 (0은 방문 안 한 상태)
    dq = deque([r])
    visited_order[r] = 1
    order = 2  # 다음 방문 순서부터는 2부터 시작

    while dq:
        current = dq.popleft()
        for neighbor in graph[current]:
            if visited_order[neighbor] == 0:
                visited_order[neighbor] = order
                order += 1
                dq.append(neighbor)

    return visited_order


def main():
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n + 1):
        graph[i].sort()  # 오름차순으로 방문해야 하므로 정렬
    
    result = bfs(graph, r, n)
    
    for i in range(1, n + 1):
        print(result[i])


if __name__ == "__main__":
    main()
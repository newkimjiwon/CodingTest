# 문제 알고리즘: Prim 알고리즘 사용
# 최소신장트리 이용

from collections import deque
import heapq, sys

input = sys.stdin.readline


def solution(graph, n):
    print(prim(graph, n))


def prim(graph, n):
    visited = [False] * n
    min_edge = [(0, 0)]  # (cost, node)
    total_cost = 0

    while min_edge:
        cost, u = heapq.heappop(min_edge)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_edge, (weight, v))
    return total_cost


def main():
    n = int(input())
    m = int(input())

    # 그래프
    graph = {i: [] for i in range(n)}

    # 1번 노드를 0번으로
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        # 양방향 그래프
        graph[a].append((b, c))
        graph[b].append((a, c))

    solution(graph, n)


if __name__ == "__main__":
    main()
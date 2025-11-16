import sys
sys.setrecursionlimit(100000)


def dfs(node, dist, visited, graph):
    visited[node] = True
    far_node = node
    max_dist = dist

    for nxt, weight in graph[node]:
        if not visited[nxt]:
            new_node, new_dist = dfs(nxt, dist + weight, visited, graph)
            if new_dist > max_dist:
                far_node, max_dist = new_node, new_dist

    return far_node, max_dist


def solution(graph, n):
    # 1단계: 임의의 노드(1)에서 가장 먼 노드 찾기
    visited = [False] * (n + 1)
    far_node, _ = dfs(1, 0, visited, graph)

    # 2단계: 해당 노드에서 다시 가장 먼 노드까지 거리 계산
    visited = [False] * (n + 1)
    _, diameter = dfs(far_node, 0, visited, graph)

    return diameter


def main():
    input = sys.stdin.readline
    n = int(input().strip())

    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(n - 1):
        a, b, dis = map(int, input().split())
        graph[a].append((b, dis))
        graph[b].append((a, dis))

    print(solution(graph, n))


if __name__ == "__main__":
    main()
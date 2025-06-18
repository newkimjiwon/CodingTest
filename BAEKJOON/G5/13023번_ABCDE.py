import sys
sys.setrecursionlimit(2000)


def dfs(graph, visited, node, depth):
    if depth == 4:
        return True  # 조건 만족

    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(graph, visited, neighbor, depth + 1):
                return True  # 하위 탐색에서 조건 만족
    visited[node] = False  # 백트래킹
    return False  # 현재 경로는 실패


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    for i in range(n):
        if dfs(graph, visited, i, 0):
            print(1)
            return  # 조건 만족하면 종료
    print(0)


if __name__ == "__main__":
    main()

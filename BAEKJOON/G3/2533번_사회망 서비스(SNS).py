import sys
# Python의 기본 재귀 한도인 1,000으로는 부족할 수 있으므로 넉넉하게 설정합니다.
sys.setrecursionlimit(1000000) 
input = sys.stdin.readline

def dp(c, parent, graph, dp_mat):
    # dp_mat[c][0]: c가 EA가 아닐 때의 최소 EA 수
    # dp_mat[c][1]: c가 EA일 때의 최소 EA 수

    # 모든 리프 노드에 대해,
    # 자신이 얼리어답터이면 1, 아니면 0입니다.
    # dp_mat[c][1] = 1은 for문 밖에서 초기화하는 것이 더 명확합니다.
    dp_mat[c][1] = 1

    for nei in graph[c]:
        if nei != parent:
            dp(nei, c, graph, dp_mat)
            
            # c가 EA가 아닐 경우, 모든 자식(nei)은 반드시 EA여야 함
            # 자식들의 dp[v][1] 값을 더합니다.
            dp_mat[c][0] += dp_mat[nei][1]

            # c가 EA일 경우, 자식(nei)은 EA여도 되고 아니어도 됨.
            # 자식의 dp[v][0]와 dp[v][1] 중 최소값을 더합니다.
            dp_mat[c][1] += min(dp_mat[nei][0], dp_mat[nei][1])


if __name__ == "__main__":
    n = int(input())

    # N=1인 경우 예외 처리
    if n == 1:
        print(1)
        sys.exit(0)

    graph = [[] for _ in range(n + 1)]

    # 트리는 n-1개의 간선을 가집니다.
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # dp_mat[i][0]는 i가 EA가 아닐 때, dp_mat[i][1]은 i가 EA일 때의 최소 EA 수를 저장합니다.
    dp_mat = [[0, 0] for _ in range(n + 1)]

    # 1번 노드를 루트로 가정하고 탐색을 시작합니다.
    dp(1, 0, graph, dp_mat)

    # 최종적으로 루트(1번 노드)가 EA일 때와 아닐 때 중 더 작은 값을 출력합니다.
    print(min(dp_mat[1][0], dp_mat[1][1]))
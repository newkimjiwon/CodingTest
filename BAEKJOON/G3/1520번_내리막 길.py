import sys
sys.setrecursionlimit(10 ** 6)

# DFS + DP로 경로의 수를 계산하는 함수
def dfs(y, x, graph, dp):
    if y == len(graph) - 1 and x == len(graph[0]) - 1:
        return 1  # 목표 지점에 도착하면 경로 수 1 리턴

    if dp[y][x] != -1:  # 이미 계산된 경로가 있으면 그 값을 리턴
        return dp[y][x]

    # 상, 하, 좌, 우 이동
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dp[y][x] = 0  # 현재 위치에서 경로 수 초기화

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(graph) and 0 <= nx < len(graph[0]):
            if graph[y][x] > graph[ny][nx]:  # 내리막길 조건
                dp[y][x] += dfs(ny, nx, graph, dp)

    return dp[y][x]

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 (-1로 초기화)
dp = [[-1] * m for _ in range(n)]

# DFS 탐색 시작
print(dfs(0, 0, graph, dp))
import sys
sys.setrecursionlimit(10**6)  # 재귀함수 깊이 제한


move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상 하 좌 우


def dfs(y, x):
    # 이미 계산된 경우 반환
    if dp[y][x] != 0:
        return dp[y][x]
    
    best = 1  # 최소 자기 자신 1칸
    current = bamboo[y][x]

    for ny, nx in move:
        iy, ix = ny + y, nx + x
        if 0 <= iy < n and 0 <= ix < n and bamboo[iy][ix] > current:
            best = max(best, 1 + dfs(iy, ix))
    
    dp[y][x] = best
    return best


if __name__=="__main__":
    n = int(input())
    
    bamboo = [list(map(int, input().split())) for _ in range(n)]  # 대나무
    dp = [[0] * n for _ in range(n)]  # dp

    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, dfs(i, j))

    print(ans)
def main():
    n, m = map(int, input().split())

    maze = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = maze[0][0]

    move = [(0, 1), (1, 0), (1, 1)]  # 상하좌우 움직임

    for ix in range(m):
        for iy in range(n):
            ny, nx = iy, ix
            for ty, tx in move:
                y = ny + ty
                x = nx + tx
                if 0 <= y < n and 0 <= x < m:
                    dp[y][x] = max(dp[y][x], dp[ny][nx] + maze[y][x])
    
    print(dp[n - 1][m - 1])


if __name__=="__main__":
    main()
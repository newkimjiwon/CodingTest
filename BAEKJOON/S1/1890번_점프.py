def solution():
    n = int(input())  # n은 게임판의 수

    maps = [list(map(int, input().split())) for _ in range(n)]  # 게임 판
    dp = [[0] * n for _ in range(n)]  # dp

    dp[0][0] = 1  # 처음에 방문함

    for y in range(n):
        for x in range(n):

            if maps[y][x] == 0:
                continue
            
            dis = maps[y][x]
            if x + dis < n:
                dp[y][x + dis] += dp[y][x]
            if y + dis < n:
                dp[y + dis][x] += dp[y][x]
                
    return dp[n - 1][n - 1]


if __name__=="__main__":
    print(solution())
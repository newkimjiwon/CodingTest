import sys
input = sys.stdin.readline
sys.setrecursionlimit(350000)
def inrange(r, c, R, C):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False

def dfs(r,c,R,C):
    global ans
    check[r][c] = 2    # 방문 체크를 해두기, 일단 불가능 한 것으로 기록
    v = maze[r][c]
    nr, nc = r + direction[v][0], c + direction[v][1]

    # 탈출 가능시 탈출 가능을 기록 하고, 값에 True를 반환
    if not inrange(nr, nc, R, C):
        check[r][c] = 1
        return True

    # 다음 지점이 탈출 가능한것으로 기록되었으면 현재 지점도 탈출 가능한 것으로 기록
    if check[nr][nc] == 1:
        check[r][c] = 1
        return True
    # 다음 지점이 탈출 불가능하면, 현재 지점도 탈출 불가능
    elif check[nr][nc] == 2:
        return False

    # 재귀를 이용하여 얻은 값, 탈출이 가능하다면 True, 불가능 하다면 False
    value = dfs(nr, nc, R, C)
    if value:    # 탈출 가능
        check[r][c] = 1
        return True
    return False    # 탈출 불가

N, M = map(int,input().split())
maze = [input().rstrip() for _ in range(N)]
direction = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
check = [[0] * M for _ in range(N)]    # 좌표 방문 여부를 기록 // 값 - 0 : 미방문, 1 : 탈출가능, 2 : 탈출 불가

for r in range(N):
    for c in range(M):
        if not check[r][c]:
            dfs(r, c, N, M)
ans = 0
for r in range(N):
    for c in range(M):
        if check[r][c] == 1:
            ans += 1
print(ans)
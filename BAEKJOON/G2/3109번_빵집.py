import sys
sys.setrecursionlimit(10000)


# 대각선을 포함한 이동
move = [(-1, 1), (0, 1), (1, 1)]


def dfs(y, x, pipe, r, c):
    pipe[y][x] = 'x'  # 방문 표시

    if x == c - 1:
        return True  # 성공 도착

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < r and 0 <= nx < c and pipe[ny][nx] == '.':
            if dfs(ny, nx, pipe, r, c):
                return True  # 성공 경로는 계속 True 리턴

    return False  # 도달 실패


def main():
    r, c = map(int, input().split())
    pipe = [list(input()) for _ in range(r)]

    answer = 0
    for i in range(r):
        if dfs(i, 0, pipe, r, c):
            answer += 1

    print(answer)


if __name__=="__main__":
    main()
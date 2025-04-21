import sys
input = sys.stdin.readline


def is_perfect_square(s):
    num = int(s)
    root = int(num ** 0.5)
    return root * root == num


def main():
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    max_square = -1

    for i in range(N):        # 시작 행
        for j in range(M):    # 시작 열
            for dx in range(-N, N):
                for dy in range(-M, M):
                    if dx == 0 and dy == 0:
                        continue

                    x, y = i, j
                    s = ""

                    while 0 <= x < N and 0 <= y < M:
                        s += board[x][y]
                        if is_perfect_square(s):
                            max_square = max(max_square, int(s))
                        x += dx
                        y += dy

    print(max_square)


if __name__ == "__main__":
    main()

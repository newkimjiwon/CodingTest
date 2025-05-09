# 정답
answer = 0


def solution(n, m, block):
    global answer
    answer = 0  # 수정됨: 여러 테스트 케이스가 있을 경우 초기화 필요

    # 이동 방향 (상, 하, 좌, 우)
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = [[False] * m for _ in range(n)]

    def dfs(iy, ix, count, total):
        global answer
        if count == 4:
            answer = max(answer, total)
            return
        for ny, nx in move:
            y = iy + ny
            x = ix + nx
            if 0 <= y < n and 0 <= x < m and not visited[y][x]:
                visited[y][x] = True
                dfs(y, x, count + 1, total + block[y][x])  # 수정됨: block[i][j] → block[y][x]
                visited[y][x] = False

    # DFS 탐색: ㅗ 제외한 테트로미노 모양
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, block[i][j])
            visited[i][j] = False

    # ㅗ, ㅏ, ㅓ, ㅜ 모양 (중간 분기형)
    shapes = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅗ
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
        [(0, 0), (1, -1), (1, 0), (1, 1)],  # ㅜ
        [(0, 0), (1, -1), (1, 0), (2, 0)]  # ㅓ
    ]

    # 하드코딩 탐색: ㅗ 계열 모양
    for i in range(n):
        for j in range(m):
            for shape in shapes:
                total = 0
                valid = True
                for dy, dx in shape:
                    y = i + dy
                    x = j + dx
                    if 0 <= y < n and 0 <= x < m:
                        total += block[y][x]
                    else:
                        valid = False
                        break
                if valid:
                    answer = max(answer, total)


def main():
    n, m = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(n)]
    solution(n, m, block)
    print(answer)


if __name__ == "__main__":
    main()

answer = 4


# 모든 세로선이 자기 자신으로 돌아오는지 확인
def is_valid(ladder, n, h):
    for start in range(1, n + 1):
        k = start
        for i in range(1, h + 1):
            if ladder[i][k]:       # 오른쪽 연결
                k += 1
            elif ladder[i][k - 1]: # 왼쪽 연결
                k -= 1
        if k != start:
            return False
    return True


# 사다리 추가 DFS 탐색
def dfs(ladder, n, h, count, x, y):
    global answer
    if count >= answer:
        return
    if is_valid(ladder, n, h):
        answer = count
        return

    for i in range(x, h + 1):
        j_start = y if i == x else 1
        for j in range(j_start, n):
            # 인접한 위치에 사다리가 있으면 안 됨
            if ladder[i][j] or ladder[i][j - 1] or ladder[i][j + 1]:
                continue
            ladder[i][j] = True
            dfs(ladder, n, h, count + 1, i, j + 2)  # j + 2로 다음 사다리 위치 이동
            ladder[i][j] = False

def main():
    global answer
    n, m, h = map(int, input().split())
    ladder = [[False] * (n + 2) for _ in range(h + 2)]  # 경계 처리 위해 +2

    for _ in range(m):
        a, b = map(int, input().split())
        ladder[a][b] = True

    # 시작 전에 이미 정답이면 바로 출력
    if is_valid(ladder, n, h):
        print(0)
        return

    dfs(ladder, n, h, 0, 1, 1)
    print(answer if answer <= 3 else -1)


if __name__ == "__main__":
    main()
# 결과 값
answer = 0
# 상 하 좌 우 움직임
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(load, visited, count ,iy, ix, r, c, k):
    global answer

    # 무한 반복을 종료한다.
    if count > k:
        return

    if iy == 0 and ix == c - 1 and count == k:
        answer += 1
        return

    for ny, nx in move:
        y = ny + iy
        x = nx + ix
        if 0 <= y < r and 0 <= x < c and not visited[y][x] and load[y][x] == '.':
            visited[y][x] = True
            solution(load, visited, count + 1, y, x, r, c, k)
            visited[y][x] = False


def main():
    # 정답
    global answer

    r, c, k = map(int, input().split())

    # 길
    load = [list(input()) for _ in range(r)]

    # 방문 처리
    visited = [[False] * c for _ in range(r)]

    visited[r - 1][0] = True

    solution(load, visited, 1, r - 1, 0, r, c, k)

    print(answer)


if __name__=="__main__":
    main()
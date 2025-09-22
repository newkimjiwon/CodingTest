from collections import deque


def bfs(buildings, W, H):
    # 서로 다른 q 생성
    sang_dq = deque()
    fire_dq = deque()
    visited = [[False] * W for _ in range(H)]  # 방문처리

    # h는 세로, w 가로 탐색
    for h in range(H):
        for w in range(W):
            if buildings[h][w] == '*':
                fire_dq.append((h, w))
            elif buildings[h][w] == '@':
                sang_dq.append((h, w))
                visited[h][w] = True

    time = 0  # 시간
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 움직임

    while sang_dq:
        time += 1  # 1분이 지남

        # 불이 먼저 움직이는 경우
        size_f = len(fire_dq)
        for _ in range(size_f):
            ny, nx = fire_dq.popleft()

            for iy, ix in move:
                y, x = ny + iy, nx + ix
                # 범위 안에 있으면서 * != 불도 아니고 벽(#)도 아니면 불태울 수 있음
                if 0 <= y < H and 0 <= x < W and buildings[y][x] != '*' and buildings[y][x] != '#':
                    buildings[y][x] = '*'
                    fire_dq.append((y, x))


        # 상근이가 움직이는 경우
        size_s = len(sang_dq)
        for _ in range(size_s):
            ny, nx = sang_dq.popleft()  # 처음 자표를 (ny, nx)로 뽑는다.

            # 탈출 하는 경우 (y == H, 0, x == W, 0) 일때 탈출 가능
            if ny == 0 or ny == H - 1 or nx == 0 or nx == W - 1:
                return time

            for iy, ix in move:
                y, x = ny + iy, nx + ix  # 새로운 좌표
                if 0 <= y < H and 0 <= x < W and not visited[y][x]:
                    if buildings[y][x] == '.':
                        visited[y][x] = True  # 방문 처리
                        sang_dq.append((y, x))  # 다음 탐색

    # 탈출 경우가 없는 경우
    return "IMPOSSIBLE"


if __name__=="__main__":
    t = int(input())  # 테스트 케이스

    for _ in range(t):
        w, h = map(int, input().split())
        building = [list(input()) for _ in range(h)]
        print(bfs(building, w, h))
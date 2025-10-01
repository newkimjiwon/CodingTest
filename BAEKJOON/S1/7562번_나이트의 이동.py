from collections import deque
import sys
input = sys.stdin.readline


def bfs(l, ny, nx, gy, gx):
    dq = deque()
    moves = [(2, -1), (2, 1), (1, 2), (-1, 2),
             (-2, 1), (-2, -1), (1, -2), (-1, -2)]
    dq.append((ny, nx, 0))
    visited = {(ny, nx)}

    while dq:
        iy, ix, cnt = dq.popleft()
        if (iy, ix) == (gy, gx):
            return cnt
        for dy, dx in moves:
            y, x = iy + dy, ix + dx
            if 0 <= y < l and 0 <= x < l and (y, x) not in visited:
                dq.append((y, x, cnt + 1))
                visited.add((y, x))
    return -1


if __name__ == "__main__":
    T = int(input())

    result = []

    for _ in range(T):
        l = int(input())
        ny, nx = map(int, input().split())
        gy, gx = map(int, input().split())
        result.append(bfs(l, ny, nx, gy, gx))

    for i in result:
        print(i)
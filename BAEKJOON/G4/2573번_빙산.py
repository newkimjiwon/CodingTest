import sys
from collections import deque


input = sys.stdin.readline


def solution(n, m, ice):
    answer = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    # 빙산이 있는 좌표만 저장
    ice_coords = [(i,j) for i in range(n) for j in range(m) if ice[i][j] > 0]

    while True:
        # 1. 빙산 덩어리 수 세기 (BFS)
        visited = [[False]*m for _ in range(n)]
        chunks = 0

        for i, j in ice_coords:
            if not visited[i][j]:
                chunks += 1
                if chunks >= 2:
                    return answer

                q = deque()
                q.append((i,j))
                visited[i][j] = True

                while q:
                    y, x = q.popleft()
                    for dy, dx in directions:
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < n and 0 <= nx < m:
                            if not visited[ny][nx] and ice[ny][nx] > 0:
                                visited[ny][nx] = True
                                q.append((ny, nx))

        if chunks == 0:
            return 0

        # 2. 녹을 양 계산
        melt = [[0]*m for _ in range(n)]
        for y, x in ice_coords:
            sea = 0
            for dy, dx in directions:
                ny, nx = y+dy, x+dx
                if 0 <= ny < n and 0 <= nx < m and ice[ny][nx] == 0:
                    sea += 1
            melt[y][x] = sea

        # 3. 얼음 녹이기 & 얼음 있는 좌표 업데이트
        new_ice_coords = []
        for y, x in ice_coords:
            ice[y][x] = max(0, ice[y][x] - melt[y][x])
            if ice[y][x] > 0:
                new_ice_coords.append((y,x))

        ice_coords = new_ice_coords
        answer += 1


def main():
    n, m = map(int, input().split())
    ice = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, ice))


if __name__ == "__main__":
    main()

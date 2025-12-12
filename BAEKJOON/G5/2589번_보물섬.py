from collections import deque


move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 움직임

def find(N, M):
    answer = -1

    maps = [list(input()) for _ in range(N)]  # 지도

    # 완전 탐색
    for iy in range(N):
        for ix in range(M):
            if maps[iy][ix] == 'W':  # 바다인 경우 Pass
                continue

            visited = [[False] * M for _ in range(N)]  # 방문처리
            visited[iy][ix] = True

            q = deque()  
            q.append((iy, ix, 0))  # y좌표, x좌표, distance
            count = -1

            while q:
                qy, qx, dis = q.popleft()

                if dis > count:
                    count = dis
                
                for dy, dx in move:
                    y = qy + dy
                    x = qx + dx
                    if 0 <= y < N and 0 <= x < M and not visited[y][x]:
                        if maps[y][x] == 'L':
                            q.append((y, x, dis + 1))
                            visited[y][x] = True
            
            answer = max(answer, count)

    return answer


if __name__=="__main__":
    N, M = map(int, input().split())

    print(find(N, M))
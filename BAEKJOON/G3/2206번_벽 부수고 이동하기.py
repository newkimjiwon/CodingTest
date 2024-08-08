from collections import deque

def bfs(n, m, graph):
    q = deque([(0, 0, 0)])
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    steps = 1  # 시작하는 칸도 포함해서 세므로 초기값을 1로 설정

    while q:
        for _ in range(len(q)):
            y, x, wall_break = q.popleft()

            if y == n - 1 and x == m - 1:
                return steps

            for iy, ix in move:
                ny, nx = y + iy, x + ix

                if 0 <= ny < n and 0 <= nx < m:
                    if graph[ny][nx] == '0' and not visited[ny][nx][wall_break]:
                        visited[ny][nx][wall_break] = True
                        q.append((ny, nx, wall_break))

                    if graph[ny][nx] == '1' and wall_break == 0 and not visited[ny][nx][1]:
                        visited[ny][nx][1] = True
                        q.append((ny, nx, 1))

        steps += 1

    return -1

# 입력 받기
N, M = map(int, input().split())
Map = [input().strip() for _ in range(N)]

# 결과 출력
print(bfs(N, M, Map))

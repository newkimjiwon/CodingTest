from collections import deque
import copy

INF = int(1e9)


def bfs(N: int, M: int, lab: list[list[int]], active):
    dq = deque()

    visited = [[-1] * N for _ in range(N)]

    for y, x in active:
        dq.append((y, x))
        visited[y][x] = 0

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    max_time = 0

    while dq:
        y, x = dq.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                # 벽은 통과 불가, 방문 안한 곳만 감염
                if lab[ny][nx] != 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    dq.append((ny, nx))

    # BFS 끝나고 빈 칸이 남았는지 확인
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:  # 빈 칸인데
                if visited[i][j] == -1:  # 감염 안 됐으면 실패
                    return INF
                max_time = max(max_time, visited[i][j])

    return max_time


def solution(N: int, M: int, lab: list[list[int]]):
    answer = INF
    virus = []

    for iy in range(N):
        for ix in range(N):
            if lab[iy][ix] == 2:
                virus.append((iy, ix))  # 바이러스 위치 저장

    visited = [False] * len(virus)
    selected = []

    def dfs(start):
        nonlocal answer
        
        if len(selected) == M:
            labs = copy.deepcopy(lab)
            time = bfs(N, M, labs, selected)
            answer = min(answer, time)
            return

        for i in range(start, len(virus)):
            if not visited[i]:
                visited[i] = True
                selected.append(virus[i])
                dfs(i + 1)
                visited[i] = False
                selected.pop()

    dfs(0)

    return -1 if answer == INF else answer


if __name__=="__main__":
    N, M = map(int, input().split())

    lab = [list(map(int, input().split())) for _ in range(N)]  # 연구소

    print(solution(N, M, lab))
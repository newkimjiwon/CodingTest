import heapq
from collections import deque

# 상하좌우 이동을 위한 방향 설정
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS로 먹을 수 있는 가장 가까운 물고기 찾기
def bfs(shark, n, shark_size):
    q = deque([shark])  # 아기 상어의 위치를 시작점으로 BFS
    visited = [[False] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = True
    dist = [[-1] * n for _ in range(n)]  # 거리 저장
    dist[shark[0]][shark[1]] = 0

    fish_list = []  # 먹을 수 있는 물고기 후보들

    while q:
        y, x = q.popleft()

        for iy, ix in move:
            ny, nx = y + iy, x + ix

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if ftank[ny][nx] <= shark_size:  # 상어가 지나갈 수 있는 칸
                    visited[ny][nx] = True
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

                    # 먹을 수 있는 물고기를 발견
                    if 0 < ftank[ny][nx] < shark_size:
                        heapq.heappush(fish_list, (dist[ny][nx], ny, nx))

    if fish_list:
        # 가장 가까운 물고기를 반환 (거리가 가까운, 가장 위, 가장 왼쪽)
        return heapq.heappop(fish_list)
    return None

def solution(ftank, n):
    # 아기 상어 초기 상태
    for i in range(n):
        for j in range(n):
            if ftank[i][j] == 9:
                shark = (i, j)  # 상어의 위치
                ftank[i][j] = 0  # 상어가 있는 칸을 빈 칸으로

    shark_size = 2  # 초기 크기
    shark_eat = 0  # 먹은 물고기 수
    time = 0  # 걸린 시간

    while True:
        # BFS로 가장 가까운 먹을 수 있는 물고기 찾기
        result = bfs(shark, n, shark_size)

        if result is None:  # 더 이상 먹을 물고기가 없으면 종료
            break

        # 물고기를 먹고, 상어의 위치와 시간 갱신
        dist, ny, nx = result
        time += dist  # 이동한 거리가 시간
        shark = (ny, nx)
        ftank[ny][nx] = 0  # 물고기를 먹은 자리는 빈 칸으로

        # 상어가 물고기를 먹으면 크기 증가 여부 확인
        shark_eat += 1
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0

    return time

# 입력 받기
N = int(input())
ftank = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(solution(ftank, N))
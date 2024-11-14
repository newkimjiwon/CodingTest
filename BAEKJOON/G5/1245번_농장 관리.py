from collections import deque

# bfs 함수
def bfs(mount, visit, start_y, start_x):
    # 시작 위치의 높이
    peak_height = mount[start_y][start_x]
    # 봉우리 여부를 판단하는 플래그
    is_peak = True
    # bfs 큐 초기화
    q = deque([(start_y, start_x)])
    visit[start_y][start_x] = True
    
    # 상하좌우 및 대각선을 포함한 8방향 이동
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    while q:
        y, x = q.popleft()
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            # 격자 범위 내에서만 탐색
            if 0 <= ny < len(mount) and 0 <= nx < len(mount[0]):
                if mount[ny][nx] > peak_height:
                    # 인접 격자가 현재 높이보다 크면 산봉우리가 아님
                    is_peak = False
                elif mount[ny][nx] == peak_height and not visit[ny][nx]:
                    # 같은 높이의 인접 격자를 탐색
                    visit[ny][nx] = True
                    q.append((ny, nx))
    
    return is_peak  # 봉우리인지 여부를 반환

# 산봉우리의 개수를 세는 함수
def count_peaks(mount):
    n, m = len(mount), len(mount[0])
    visited = [[False] * m for _ in range(n)]
    total_peaks = 0
    
    for i in range(n):
        for j in range(m):
            if mount[i][j] > 0 and not visited[i][j]:
                # bfs 호출하여 봉우리 여부 확인
                if bfs(mount, visited, i, j):
                    total_peaks += 1
    
    return total_peaks

# 입력 받기
n, m = map(int, input().split())
mount = [list(map(int, input().split())) for _ in range(n)]

# 산봉우리 개수 출력
print(count_peaks(mount))
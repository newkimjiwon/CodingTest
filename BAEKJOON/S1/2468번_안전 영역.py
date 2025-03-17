from collections import deque


def solution(n, local, water_high):
    answer = 0

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상 하 좌 우

    visited = [[False] * n for _ in range(n)]  # 방문처리

    # 잠기는 지역부터 체크
    for i in range(n):
        for j in range(n):
            if local[i][j] <= water_high:
                visited[i][j] = True  # 물 보다 낮은 높이는 잠긴다

    # 잠기지 않는 지역을 체크 위에서 비의 양보다 무조건 큰 지역들만 있으므로
    # local를 다시 체크할 필요가 없다.
    for k in range(n):
        for l in range(n):
            if not visited[k][l]:
                dq = deque()  # deque

                dq.append((k, l))  # 값 넣기
                visited[k][l] = True

                while dq:
                    iy, ix = dq.popleft()  # 좌표 추출

                    for ny, nx in move:
                        y = iy + ny
                        x = ix + nx
                        if 0 <= y < n and 0 <= x < n and not visited[y][x]:
                            visited[y][x] = True
                            dq.append((y, x))

                answer += 1

    return answer


n = int(input())  # 지역의 크기

local = [list(map(int, input().split())) for _ in range(n)]  # 지역

# 최대 높이 찾기 (최적화)
max_high = max(map(max, local))

# 물 높이 0부터 시작해야 안전 영역 최댓값을 찾을 수 있음
result = [solution(n, local, w) for w in range(max_high + 1)]

print(max(result))
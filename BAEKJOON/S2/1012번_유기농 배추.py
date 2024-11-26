from collections import deque

# 테스트 케이스
T = int(input())

# 배추 찾기
def earthworm(napa_cabbage, visit, m, n):
    answer = 0

    # 상하좌우로 움직이기
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(n):
        for j in range(m):
            if not visit[i][j] and napa_cabbage[i][j] == 1:
                q = deque([(i, j)])
                visit[i][j] = True
                # 배추를 찾으면 상하좌우에 배추가 있는지 확인 후 퍼트린다
                while q:
                    iy, ix = q.popleft()

                    for ny, nx in move:
                        y = iy + ny
                        x = ix + nx
                        if 0 <= y < n and 0 <= x < m:
                            # 배추가 더 있는지 확인
                            if napa_cabbage[y][x] == 1 and visit[y][x] == False:
                                visit[y][x] = True
                                q.append((y, x))
                answer += 1
            elif not visit[i][j] and napa_cabbage[i][j] == 0:
                visit[i][j] = True

    return answer

def main():
    for _ in range(T):
        m, n, k = map(int, input().split())
        # 배추 심기
        napa_cabbage = [[0] * m for _ in range(n)]
        # 방문 체크
        visited = [[False] * m for _ in range(n)]

        for _ in range(k):
            a, b = map(int, input().split())
            napa_cabbage[b][a] = 1
        
        # 배추 찾아서 반환 값 출력
        print(earthworm(napa_cabbage, visited, m, n))

main()
from collections import deque


answer = 100000  # 결과는 양 끝단에 있더라도 100000 이하이다.
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상 하 좌 우


def continent_split(n, maps):
    visited = [[0] * n for _ in range(n)]  # 방문 처리
    continent = 1  # 대륙을 표기할 변수

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1 and visited[i][j] == 0:
                dq = deque()
                dq.append((i, j))
                visited[i][j] = continent

                while dq:
                    iy, ix = dq.popleft()

                    for ny, nx in move:
                        y, x = iy + ny, ix + nx
                        if 0 <= y < n and 0 <= x < n and maps[y][x] == 1 and visited[y][x] == 0:
                            dq.append((y, x))
                            visited[y][x] = continent  # 대륙으로 표시
                continent += 1  # 다른 대륙으로 표기해야함

    return visited


def bfs(n, maps):
    global answer
    visited = continent_split(n, maps)  # 대륙간 나눠진 방문을 받는다.

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1 and visited[i][j] > 0:  # 0보다 크면 대륙
                current_continent = visited[i][j]  # 현재 대륙
                q = deque()
                q.append((i, j, 0))
                local_visited = [[False] * n for _ in range(n)]
                local_visited[i][j] = True  # BFS에서 같은 위치를 여러 번 방문하지 않도록 체크

                found = False  # 다른 대륙을 찾았는지 확인하는 변수

                while q and not found:  # 다른 대륙을 찾으면 종료
                    iy, ix, dis = q.popleft()

                    for ny, nx in move:
                        y, x = iy + ny, ix + nx
                        if 0 <= y < n and 0 <= x < n and not local_visited[y][x]:
                            local_visited[y][x] = True
                            # 바다를 건너는 경우
                            if maps[y][x] == 0:
                                q.append((y, x, dis + 1))
                            # 다른 대륙을 발견한 경우
                            elif visited[y][x] > 0 and visited[y][x] != current_continent:
                                answer = min(answer, dis)  # 최소 거리 갱신
                                found = True  # 다른 대륙 찾음 -> 현재 BFS 종료
                                break  # 내부 for 루프 탈출

    return answer  # 모든 BFS 탐색이 끝난 후 최단 거리 반환


def main():
    n = int(input())  # 지도의 크기
    maps = [list(map(int, input().split())) for _ in range(n)]  # 지도
    print(bfs(n, maps))


main()
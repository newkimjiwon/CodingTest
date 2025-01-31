from collections import deque

# 상 하 좌 우 이동
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def design(n, l, r, continents):
    answer = 0  # 인구 이동 횟수

    while True:
        # 방문 처리를 위한 변수
        visited = [[False] * n for _ in range(n)]

        is_moved = False  # 이동이 일어났는지 확인하는 변수

        for y in range(n):
            for x in range(n):
                if not visited[y][x]:  # 방문하지 않은 경우 BFS 실행
                    if bfs(continents, visited, l, r, n, y, x):
                        is_moved = True  # 하나라도 이동이 일어났다면 True

        if not is_moved:  # 이동이 없으면 종료
            break
        answer += 1  # 이동 횟수 증가

    return answer


def bfs(continents, visited, l, r, n, start_y, start_x):
    dq = deque()  # bfs Algorithm
    dq.append((start_y, start_x))
    visited[start_y][start_x] = True  # 방문 체크

    union = [(start_y, start_x)]  # 연합 국가 좌표 저장
    total_population = continents[start_y][start_x]  # 연합 총 인구
    count = 1  # 연합 국가 수

    while dq:
        y, x = dq.popleft()

        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                # 절대값을 이용
                diff = abs(continents[y][x] - continents[ny][nx])
                if l <= diff <= r:
                    visited[ny][nx] = True
                    dq.append((ny, nx))
                    union.append((ny, nx))
                    total_population += continents[ny][nx]
                    count += 1

    if count > 1:  # 연합이 존재할 경우 인구 이동
        new_population = total_population // count
        for uy, ux in union:
            continents[uy][ux] = new_population
        return True  # 연합이 형성됨을 의미

    return False  # 연합이 없었음을 의미


def main():
    # 입력 처리
    n, l, r = map(int, input().split())
    continents = [list(map(int, input().split())) for _ in range(n)]

    # 결과 출력
    print(design(n, l, r, continents))


# 실행
main()
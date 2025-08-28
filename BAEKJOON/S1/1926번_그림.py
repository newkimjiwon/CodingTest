from collections import deque


def solution(n, m, images):
    count, max_value = 0, 0

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우
    visited = [[False] * m for _ in range(n)]  # 방문 처리 배열

    for i in range(n):
        for ii in range(m):
            if images[i][ii] == 1 and not visited[i][ii]:
                count += 1
                visited[i][ii] = True

                dq = deque([(i, ii)])  # 시작
                current = 1

                while dq:
                    ny, nx = dq.popleft()

                    for iy, ix in move:
                        y = ny + iy
                        x = nx + ix
                        
                        if 0 <= y < n and 0 <= x < m:
                            if images[y][x] == 1 and not visited[y][x]:
                                current += 1
                                dq.append((y, x))
                                visited[y][x] = True
                
                max_value = max(max_value, current)

    return count, max_value


if __name__=="__main__":
    n, m = map(int, input().split())

    image = [list(map(int, input().split())) for _ in range(n)]  # 그림

    answer_1, answer_2 = solution(n, m, image)

    print(answer_1)
    print(answer_2)
from collections import deque


# 상 하 좌 우 움직이는거(전역)
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 사람
def normal(picture, n):
    # 나눠진 부분
    part = 0

    # 부분을 나누기 위한 배열
    visited = [[False] * n for _ in range(n)]

    # deque를 이용한 BFS함수
    dq = deque()

    # 모든 상태를 확인
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 현재의 색상을 저장
                current = picture[i][j]

                # 현재 위치를 저장
                dq.append((i, j))
                visited[i][j] = True

                while dq:
                    # 전환
                    iy, ix = dq.popleft()

                    for ny, nx in move:
                        y = iy + ny
                        x = ix + nx
                        if 0 <= y < n and 0 <= x < n and not visited[y][x]:
                            if picture[y][x] == current:
                                visited[y][x] = True
                                dq.append((y, x))

                part += 1

    return part


# 적록색약 사람
def color_blindness(picture, n):
    # 나눠진 부분
    part = 0

    # 부분을 나누기 위한 배열
    visited = [[False] * n for _ in range(n)]

    # deque를 이용한 BFS함수
    dq = deque()

    # 모든 상태를 확인
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 현재의 색상을 저장
                current = picture[i][j]

                # 현재 위치를 저장
                dq.append((i, j))
                visited[i][j] = True

                while dq:
                    # 전환
                    iy, ix = dq.popleft()

                    for ny, nx in move:
                        y = iy + ny
                        x = ix + nx
                        if 0 <= y < n and 0 <= x < n and not visited[y][x]:
                            if 'R' == current or 'G' == current:
                                if picture[y][x] == 'R' or picture[y][x] == 'G':
                                    visited[y][x] = True
                                    dq.append((y, x))
                            elif 'B' == current:
                                if picture[y][x] == 'B':
                                    visited[y][x] = True
                                    dq.append((y, x))

                part += 1

    return part


def main():
    # n는 그림의 사이즈
    n = int(input())

    # 그림
    picture = [list(input()) for _ in range(n)]

    # 결과 값
    answer = []

    answer.append(normal(picture, n))
    answer.append(color_blindness(picture, n))

    for i in answer:
        print(i, end = ' ')


# main 함수
if __name__=="__main__":
    main()
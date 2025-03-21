from collections import deque


# d가 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽을 바라 본다
machine_move = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
search = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우


def room_result(n, m, r, c, d, room):
    answer = 1 # 결과 값

    cleaner = [[False] * m for _ in range(n)]  # 청소 확인

    dq = deque([(r, c, d)])  # deque
    cleaner[r][c] = True  # 처음 위치는 무조건 청소한다. 1법칙

    while dq:
        iy, ix, direction = dq.popleft()  # 현재 위치와 방향을 가져옴
        check = False  # 주변에 청소할 구역이 있는지 확인할 플래그

        # 현재 칸의 주변 4칸 중 청소되지 않은 곳이 있는지 탐색
        for ny, nx in search:
            y = iy + ny
            x = ix + nx
            if 0 <= y < n and 0 <= x < m and room[y][x] == 0 and not cleaner[y][x]:
                check = True  # 청소할 구역이 있음
                break  # 더 이상 탐색할 필요 없음

        if check:
            # 주변에 청소할 곳이 있으면 반시계 방향으로 회전하며 한 칸씩 탐색
            for _ in range(4):
                direction = (direction - 1) % 4  # 반시계 방향 90도 회전
                ny, nx = machine_move[direction]
                y = iy + ny
                x = ix + nx
                if 0 <= y < n and 0 <= x < m and room[y][x] == 0 and not cleaner[y][x]:
                    cleaner[y][x] = True  # 청소 처리
                    answer += 1  # 청소한 칸 수 증가
                    dq.append((y, x, direction))  # 새로운 위치와 방향 저장
                    break  # 다음 단계로 넘어감
        else:
            # 주변에 청소할 곳이 없다면, 후진 시도
            back_dir = (direction + 2) % 4  # 현재 방향의 반대 방향 계산
            ny, nx = machine_move[back_dir]
            y = iy + ny
            x = ix + nx
            if 0 <= y < n and 0 <= x < m and room[y][x] == 0:
                dq.append((y, x, direction))  # 후진은 방향 유지
            else:
                return answer  # 후진 불가능(벽) → 작동 종료


def main():
    n, m = map(int, input().split())  # 방 크기

    r, c, d = map(int, input().split())  # 좌표, 방향

    room = [list(map(int, input().split())) for _ in range(n)]  # 방 크기

    print(room_result(n, m, r, c, d, room))


main()
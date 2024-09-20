from collections import deque

def bfs(ch):
    q = deque()
    # 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수
    final_count = -1
    # 시간
    time = 0
    # 상 하 좌 우로 움직여야함
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while True:
        # 매 초마다 녹아가는 치즈의 수를 구함
        count_cheeze = 0
        # 방문처리
        visit = [[0] * len(ch[0]) for _ in range(len(ch))]
        q.append((0, 0))
        visit[0][0] = 1  # 외부 공기로 방문 처리

        while q:
            iy, ix = q.popleft()
            for dy, dx in move:
                y = iy + dy
                x = ix + dx
                if 0 <= y < len(ch) and 0 <= x < len(ch[0]) and not visit[y][x]:
                    if ch[y][x] == 1:  # 치즈가 있는 칸
                        visit[y][x] = 1  # 방문 처리
                        count_cheeze += 1
                    elif ch[y][x] == 0:  # 외부 공기와 접촉하는 빈 칸
                        visit[y][x] = 1
                        q.append((y, x))

        # 더 이상 녹을 치즈가 없으면 코드를 종료한다.
        if count_cheeze == 0:
            break

        # 녹아야하는 치즈를 체크하고 그걸 반영한다
        for i in range(len(ch)):
            for j in range(len(ch[i])):
                if ch[i][j] == 1 and visit[i][j]:  # 방문한 치즈는 외부 공기와 접촉
                    ch[i][j] = 0  # 녹은 치즈로 바꿈

        # 1초가 흘렀음
        time += 1
        # 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수
        final_count = count_cheeze

    print(time)
    return final_count

# 치즈의 가로 세로 길이
n, m = map(int, input().split())

# 치즈
cheeze = [list(map(int, input().split())) * 1 for _ in range(n)]
"""
예시
cheeze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""

# BFS로 처리한 결과 출력
final_count = bfs(cheeze)
print(final_count)
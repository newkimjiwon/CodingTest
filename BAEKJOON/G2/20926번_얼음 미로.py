from heapq import heappush, heappop


# 상 하 좌 우
move = [(0, 1), (0, -1), (-1 ,0), (1, 0)]


def solution(maps):
    # 시작/도착 좌표 찾기
    tera_y = tera_x = goal_y = goal_x = 0
    H, W = len(maps), len(maps[0])
    for i in range(H):
        for ii in range(W):
            if maps[i][ii] == 'E':
                goal_y, goal_x = i, ii
            if maps[i][ii] == 'T':
                tera_y, tera_x = i, ii

    # 다익스트라: 좌표별 최소 비용
    INF = 10**18
    dist = [[INF] * W for _ in range(H)]
    dist[tera_y][tera_x] = 0

    # 우선순위 큐(비용, y, x)
    pq = []
    heappush(pq, (0, tera_y, tera_x))

    while pq:
        cur_cost, ry, rx = heappop(pq)
        if cur_cost != dist[ry][rx]:
            continue
        if (ry, rx) == (goal_y, goal_x):
            return cur_cost  # 최단 비용 확정

        for iy, ix in move:
            res = r_move(maps, ry, rx, iy, ix)  # 원래 r_move 유지
            if res is None:
                continue
            y, x, c_dis = res
            nd = cur_cost + c_dis
            if nd < dist[y][x]:
                dist[y][x] = nd
                heappush(pq, (nd, y, x))

    return -1  # 도달 불가


def r_move(maps, ry, rx, my, mx):
    """
    (ry,rx)에서 (my,mx)로 미끄러졌을 때의 도착 좌표와 누적 시간 반환.
    - 시작 타일 비용 제외
    - 출구(E) 타일 비용 제외
    - 구멍(H)·절벽은 None (이동 불가)
    - 바위(R)는 직전 칸에서 멈춤
    """
    H, W = len(maps), len(maps[0])
    y, x, dis = ry, rx, 0

    while True:
        # 이동 전 위치
        py, px = y, x
        # 한 칸 이동
        y += my
        x += mx

        # 절벽
        if y < 0 or y >= H or x < 0 or x >= W:
            return None
        cell = maps[y][x]

        # 구멍
        if cell == 'H':
            return None
        # 바위 → 직전 칸에서 멈춤
        if cell == 'R':
            return (py, px, dis)
        # 출구 → 출구 비용 제외
        if cell == 'E':
            return (y, x, dis)
        # 숫자면 비용 누적 (시작 타일은 이미 제외됨)
        if '0' <= cell <= '9':
            dis += ord(cell) - ord('0')
        # 'T'는 시작 지점(비용 0), 그냥 통과


if __name__=="__main__":
    w, h = map(int, input().split())
    maps = [list(input().strip()) for _ in range(h)]
    print(solution(maps))
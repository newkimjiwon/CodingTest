# 깊은 복사
import copy

# CCTV별 감시 방향 정의 (상, 하, 좌, 우)
directions = {
    1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],  # 단방향
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],  # 양방향
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],  # 직각 방향
    4: [[(-1, 0), (0, 1), (0, -1)], [(0, 1), (1, 0), (-1, 0)], [(1, 0), (0, -1), (0, 1)],
        [(0, -1), (-1, 0), (1, 0)]],  # 세 방향
    5: [[(0, 1), (0, -1), (1, 0), (-1, 0)]]  # 네 방향 모두
}


def move_search(cctv_number, simulation_case, n, m, position, direction_set):
    """CCTV 감시 영역을 표시"""
    y, x = position
    for dy, dx in direction_set:
        ny, nx = y, x
        while True:
            ny += dy
            nx += dx
            if 0 <= ny < n and 0 <= nx < m:
                if simulation_case[ny][nx] == 6:  # 벽
                    break
                if simulation_case[ny][nx] == 0:  # 감시 가능한 영역
                    simulation_case[ny][nx] = '#'
            else:  # 범위를 벗어나면 종료
                break


def dfs(depth, cctv_index, office, n, m, result):
    """DFS로 모든 CCTV 방향 조합 탐색"""
    if depth == len(cctv_index):  # 모든 CCTV를 처리한 경우
        # 사각지대 계산
        blind_spots = sum(row.count(0) for row in office)
        result[0] = min(result[0], blind_spots)
        return

    # 현재 CCTV 정보
    y, x = cctv_index[depth]
    cctv_number = office[y][x]

    # 모든 방향에 대해 시뮬레이션
    for direction_set in directions[cctv_number]:
        simulation = copy.deepcopy(office)
        move_search(cctv_number, simulation, n, m, (y, x), direction_set)
        dfs(depth + 1, cctv_index, simulation, n, m, result)


def cctv(offices, n, m):
    # CCTV 위치 저장
    cctv_index = []
    for i in range(n):
        for j in range(m):
            if offices[i][j] != 0 and offices[i][j] != 6:
                cctv_index.append((i, j))

    # 결과 초기화 (사각지대 최솟값)
    result = [float('inf')]
    dfs(0, cctv_index, offices, n, m, result)
    return result[0]


def main():
    # 입력 처리
    n, m = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(n)]

    # 사각지대 최소값 계산
    answer = cctv(office, n, m)
    print(answer)


main()
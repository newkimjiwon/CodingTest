from collections import deque


def solution(virus_map, s, target_x, target_y, n):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 초기 바이러스 위치 수집 및 정렬
    initial = []
    for y in range(n):
        for x in range(n):
            if virus_map[y][x] != 0:
                initial.append((virus_map[y][x], 0, y, x))  # (virus 번호, 시간, y, x)

    # 바이러스 번호 오름차순으로 정렬 후 큐에 넣기
    dq = deque(sorted(initial))

    while dq:
        virus_type, time, y, x = dq.popleft()

        if time == s:
            break

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and virus_map[ny][nx] == 0:
                virus_map[ny][nx] = virus_type
                dq.append((virus_type, time + 1, ny, nx))

    return virus_map[target_y - 1][target_x - 1]


def main():
    n, k = map(int, input().split())

    virus = [list(map(int, input().split())) for _ in range(n)]

    s, y, x = map(int, input().split())

    print(solution(virus, s, x, y, n))


if __name__=="__main__":
    main()
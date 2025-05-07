from collections import deque


# 상하좌우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 섬을 구분하고 번호를 붙이는 함수
def label_islands(bridge, n, m):
    land = 1
    visited = [[False] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if not visited[y][x] and bridge[y][x] == 1:
                dq = deque([(y, x)])
                bridge[y][x] = land
                visited[y][x] = True

                while dq:
                    ny, nx = dq.popleft()
                    for dy, dx in move:
                        my, mx = ny + dy, nx + dx
                        if 0 <= my < n and 0 <= mx < m and not visited[my][mx] and bridge[my][mx] == 1:
                            bridge[my][mx] = land
                            visited[my][mx] = True
                            dq.append((my, mx))
                land += 1
    return land - 1  # 실제 섬 개수


# 각 섬에서 다른 섬으로 연결 가능한 다리(길이 ≥ 2)를 찾는다
def find_bridges(bridge, n, m, land_cnt):
    INF = int(1e9)
    min_dis = [[INF] * (land_cnt + 1) for _ in range(land_cnt + 1)]

    for y in range(n):
        for x in range(m):
            if bridge[y][x] > 0:
                current = bridge[y][x]
                for dy, dx in move:
                    ny, nx = y, x
                    dist = 0
                    while True:
                        ny += dy
                        nx += dx
                        if not (0 <= ny < n and 0 <= nx < m):
                            break
                        if bridge[ny][nx] == current:
                            break
                        if bridge[ny][nx] == 0:
                            dist += 1
                            continue
                        if dist >= 2 and bridge[ny][nx] != current:
                            target = bridge[ny][nx]
                            min_dis[current][target] = min(min_dis[current][target], dist)
                            min_dis[target][current] = min(min_dis[target][current], dist)
                            break
                        else:
                            break
    return min_dis


# 섬 간의 연결 비용(다리 길이)을 간선으로 보고 MST 수행
def kruskal(min_dis, land_cnt):
    edges = []
    for i in range(1, land_cnt + 1):
        for j in range(i + 1, land_cnt + 1):
            if min_dis[i][j] != int(1e9):
                edges.append((min_dis[i][j], i, j))

    edges.sort()
    parent = [i for i in range(land_cnt + 1)]

    def find(u):
        while u != parent[u]:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        parent[v_root] = u_root
        return True

    total = 0
    count = 0
    for cost, a, b in edges:
        if union(a, b):
            total += cost
            count += 1

    if count == land_cnt - 1:
        return total
    else:
        return -1


# MST 결과가 모든 섬을 연결하면 총 비용 반환, 아니면 -1
def solution(bridge, n, m):
    land_cnt = label_islands(bridge, n, m)
    min_dis = find_bridges(bridge, n, m, land_cnt)
    return kruskal(min_dis, land_cnt)


# 메인 함수
def main():
    n, m = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(n)]
    print(solution(bridge, n, m))


if __name__ == "__main__":
    main()
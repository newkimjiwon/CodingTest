import heapq


INF = int(1e9)  # 최대값
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 움직이는 배열


def solution(N, maps):
    heap = []  # 최소 힙

    distance = [[1e9] * N for _ in range(N)]  # 최대 길이
    distance[0][0] = maps[0][0]  # 현재 지불

    heapq.heappush(heap, (maps[0][0], 0, 0))  # dis, y, x

    while heap:
        dis, iy, ix = heapq.heappop(heap)  # heap 배열 출력

        if dis > distance[iy][ix]:
            continue

        for dy, dx in move:
            y, x = dy + iy, dx + ix  # 다음 방문 지점
            if 0 <= y < N and 0 <= x < N:
                next_distance = maps[y][x] + dis # 다음 지불
                if next_distance < distance[y][x]:
                    distance[y][x] = next_distance  # 짧은 거리 갱신
                    heapq.heappush(heap, (next_distance, y, x))


    return distance[N - 1][N - 1]


def main():
    # 결과
    result = []

    while True:
        N = int(input())

        if N == 0:  # N이 0인 경우 종료
            break

        # 정답을 출력
        maps = [list(map(int, input().split())) for _ in range(N)]
        result.append(solution(N, maps))
    
    for i in range(1, len(result) + 1):
        print(f'Problem {i}: {result[i - 1]}')


if __name__=="__main__":
    main()        
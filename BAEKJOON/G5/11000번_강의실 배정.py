import heapq

def min_classrooms_needed(n, intervals):
    if not intervals:
        return 0

    # 수업을 시작 시간 기준으로 정렬
    intervals.sort(key=lambda x: x[0])

    # 우선순위 큐 (종료 시간을 기준으로)
    end_times = []
    heapq.heappush(end_times, intervals[0][1])

    for i in range(1, n):
        start, end = intervals[i]

        # 현재 수업이 가장 빨리 끝나는 수업이 끝난 후 시작할 수 있다면 방 재사용
        if end_times[0] <= start:
            heapq.heappop(end_times)

        # 현재 수업의 종료 시간을 우선순위 큐에 추가
        heapq.heappush(end_times, end)

    return len(end_times)

# 입력 처리
N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

print(min_classrooms_needed(N, intervals))
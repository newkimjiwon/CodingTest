def solution(n, arr):
    # 1. 도착 시간 기준으로 정렬
    arr.sort()
    
    # 2. 현재 시간 초기화
    current_time = 0

    # 3. 각 소 처리
    for arrival, duration in arr:
        if current_time < arrival:
            current_time = arrival
        current_time += duration

    return current_time

if __name__ == "__main__":
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, arr))
from collections import deque


def solution(n, k):
    answer = 0

    # 방문 처리
    visited = [False] * 100001

    dq = deque([(n, 0)])  # 시작 위치와 몇 번 바뀌는 지 변수를 기입

    while dq:
        current, time = dq.popleft()

        if current == k:
            return time

        # 순간이동: 0초 걸리므로 먼저 탐색
        if 0 <= current * 2 <= 100000 and not visited[current * 2]:
            visited[current * 2] = True
            dq.appendleft((current * 2, time))  # 0초 -> 우선 탐색

        # 걷기: 1초 걸리므로 뒤에 탐색
        if 0 <= current - 1 <= 100000 and not visited[current - 1]:
            visited[current - 1] = True
            dq.append((current - 1, time + 1))

        if 0 <= current + 1 <= 100000 and not visited[current + 1]:
            visited[current + 1] = True
            dq.append((current + 1, time + 1))

    # 모든 경우가 없다면
    return 0


def main():
    n, k = map(int, input().split())

    print(solution(n, k))


if __name__=="__main__":
    main()
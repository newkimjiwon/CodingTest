from collections import deque


def solution(bridge, start, end, n):
    if start == end:  # 시작과 도착이 같으면 점프할 필요 없음
        return 0

    if bridge[start] == 0:  # 시작 지점의 점프 값이 0이면 이동 불가
        return -1

    dq = deque()
    dq.append((start, 0))  # 시작 지점, 점프 횟수 (0부터 시작)
    visited = [False] * (n + 1)
    visited[start] = True  # 시작 지점 방문 체크

    while dq:
        current, attempts = dq.popleft()  # 현재 위치, 점프 횟수
        jump = bridge[current]  # 현재 위치에서 점프할 수 있는 거리

        # 오른쪽 방향 점프
        for m in range(1, n + 1):
            possible = current + jump * m
            if possible > n:  # 범위 초과하면 중단
                break
            if possible == end:  # 도착 지점이면 점프 횟수 반환
                return attempts + 1
            if not visited[possible]:
                dq.append((possible, attempts + 1))
                visited[possible] = True  # 방문 체크

        # 왼쪽 방향 점프
        for m in range(1, n + 1):
            possible = current - jump * m
            if possible < 1:  # 범위를 초과하면 중단
                break
            if possible == end:  # 도착 지점이면 점프 횟수 반환
                return attempts + 1
            if not visited[possible]:
                dq.append((possible, attempts + 1))
                visited[possible] = True  # 방문 체크

    return -1  # 도착 지점에 도달할 수 없는 경우


def main():
    n = int(input())  # 징검다리 개수
    bridge = [0] + list(map(int, input().split()))  # 인덱스 1부터 시작하도록 배열 확장
    start, end = map(int, input().split())  # 시작 위치와 도착 위치 입력

    print(solution(bridge, start, end, n))


if __name__=="__main__":
    main()
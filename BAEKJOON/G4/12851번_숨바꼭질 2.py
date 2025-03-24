from collections import deque


def bfs(n, k):
    answer = 0  # 방법의 수
    times = [100001] * 100001  # 각 위치에 도달하는 최소 시간, 최대 시간으로 초기화

    dq = deque([(n, 0)])  # 큐에 (위치, 시간) 형태로 삽입
    times[n] = 0  # 수빈이의 시작 위치 시간은 0초
    ways = [0] * 100001  # 각 위치에 도달하는 방법의 수
    ways[n] = 1  # 시작 위치는 방법의 수가 1

    while dq:
        value, seconds = dq.popleft()  # 위치와 현재 시간을 가져옴

        if value == k:  # 동생을 찾았다면
            if seconds < times[k]:
                times[k] = seconds
                answer = ways[k]  # 방법의 수 갱신
            elif seconds == times[k]:
                answer += ways[k]  # 같은 시간에 여러 방법이 있을 수 있음

        # 이동 가능한 세 가지 경우 (X-1, X+1, 2*X)
        for next_pos in [value - 1, value + 1, value * 2]:
            if 0 <= next_pos <= 100000:  # 유효한 범위 내에서만 이동
                if times[next_pos] == 100001:  # 아직 방문하지 않은 곳
                    times[next_pos] = seconds + 1
                    ways[next_pos] = ways[value]  # 처음 도달하는 경우
                    dq.append((next_pos, seconds + 1))
                elif times[next_pos] == seconds + 1:  # 최소 시간으로 도달한 경우
                    ways[next_pos] += ways[value]  # 방법의 수 누적

    print(times[k])  # 동생의 위치에 도달하는 최소 시간
    print(answer)  # 최소 시간으로 도달하는 방법의 수


def main():
    n, k = map(int, input().split())  # n: 수빈이 위치, k: 동생 위치
    bfs(n, k)

main()
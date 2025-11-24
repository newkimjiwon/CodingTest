from collections import deque


def solution():
    N, K = map(int, input().split())

    visited = [False] * (100001)  # 방문 처리
    parent = [-1] * 100001  # 역추적

    # 큐를 이용하여 방문처리
    dq = deque()

    dq.append((N, 0))  # 시작 위치, 이동거리
    visited[N] = True

    while dq:
        current, dis = dq.popleft()

        # 결과 출력
        if current == K:
            print(dis)

            path = []
            temp = K
            while temp != -1:
                path.append(temp)
                temp = parent[temp]
            print(*path[::-1])
            return

        plus = current + 1
        minus = current - 1
        multiplication = current * 2

        # 이동 시작
        if 0 <= plus < 100001 and not visited[plus]:
            visited[plus] = True
            parent[plus] = current
            dq.append((plus, dis + 1))

        if 0 <= minus < 100001 and not visited[minus]:
            visited[minus] = True
            parent[minus] = current
            dq.append((minus, dis + 1))

        if 0 <= multiplication < 100001 and not visited[multiplication]:
            visited[multiplication] = True
            parent[multiplication] = current
            dq.append((multiplication, dis + 1))
        

if __name__=="__main__":
    solution()
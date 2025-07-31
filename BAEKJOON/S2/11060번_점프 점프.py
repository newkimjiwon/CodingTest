from collections import deque


def solution():
    n = int(input())
    jumps = list(map(int, input().split()))

    visited = [False] * n
    q = deque()
    q.append((0, 0))  # (위치, 점프 수)
    visited[0] = True

    while q:
        location, move = q.popleft()

        # 마지막 칸에 도달하면
        if location == n - 1:
            print(move)
            return

        for next_loc in range(location + 1, location + jumps[location] + 1):
            if next_loc < n and not visited[next_loc]:
                visited[next_loc] = True
                q.append((next_loc, move + 1))

    # 도달 불가
    print(-1)


if __name__=="__main__":
    solution()

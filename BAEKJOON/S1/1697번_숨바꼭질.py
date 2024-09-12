from collections import deque

def find(n, k):
    if n == k:
        return 0

    visited = set()
    queue = deque([(n, 0)])
    visited.add(n)

    while queue:
        current, result = queue.popleft()

        if current == k:
            return result

        next_positions = [current - 1, current + 1, current * 2]
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, result + 1))

    return -1  # 이 줄은 도달하지 않을 것입니다.


N, K = map(int, input().split())
print(find(N, K))
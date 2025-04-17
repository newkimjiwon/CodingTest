def dfs(level, start):
    prev_num = 0
    if level == m:
        print(*result)
        return
    for i in range(start, n):
        if not visited[i] and nums[i] != prev_num:
            visited[i] = True
            result[level] = nums[i]
            prev_num = nums[i]
            dfs(level + 1, i + 1)
            visited[i] = False


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    visited = [False] * n
    result = [0] * m
    dfs(0, 0)
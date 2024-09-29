def dfs(p, result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(len(p)):
        result.append(p[i])
        dfs(p, result)
        result.pop()

n, m = map(int, input().split())

per = [i for i in range(1, n + 1)]

result = []

dfs(per, result)
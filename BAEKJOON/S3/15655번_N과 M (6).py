def dfs(cu, n, m, sequence, visited, start):
    if len(cu) == m:
        print(' '.join(cu))
        return

    for i in range(start, n):
        if not visited[i]:
            cu.append(str(sequence[i]))
            visited[i] = True
            dfs(cu, n, m, sequence, visited, i)
            visited[i] = False
            cu.pop()


def main():
    n, m = map(int, input().split())
    sequence = sorted(list(map(int, input().split())))

    visited = [False] * n

    dfs([], n, m, sequence, visited, 0)


main()
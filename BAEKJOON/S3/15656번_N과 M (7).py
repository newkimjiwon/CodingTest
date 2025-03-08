def dfs(cu, n, m, se):
    if len(cu) == m:
        print(' '.join(cu))
        return
    
    for i in range(n):
        cu.append(str(se[i]))
        dfs(cu, n, m, se)
        cu.pop()


def main():
    n, m = map(int ,input().split())

    sequence = sorted(list(map(int, input().split())))

    dfs([], n, m, sequence)


main()
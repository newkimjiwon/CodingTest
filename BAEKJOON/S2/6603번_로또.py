def dfs(lotto, start, current):
    if len(current) == 6:
        print(' '.join(current))
        return


    for i in range(start, len(lotto)):
        current.append(lotto[i])
        dfs(lotto, i + 1, current)
        current.pop()


def main():
    while True:
        lotto = list(map(str, input().split()))

        if lotto[0] == '0':
            break

        dfs(lotto, 1, [])
        print()


if __name__=='__main__':
    main()
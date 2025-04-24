def main():
    # 좌표
    n = int(input())

    coordinate = [list(map(int, input().split())) for _ in range(n)]

    coordinate.sort(key = lambda x: (x[0], x[1]))

    for i, j in coordinate:
        print(i, j)


if __name__=='__main__':
    main()
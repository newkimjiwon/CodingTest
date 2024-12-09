def main():
    n = int(input())

    for i in range(n, 0, -1):
        star = ''
        empty = ''
        for _ in range(n, i, -1):
            empty += ' '
        for _ in range(i):
            star += '*'
        print(empty + star)

main()
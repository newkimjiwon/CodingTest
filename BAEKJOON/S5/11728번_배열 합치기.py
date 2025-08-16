if __name__=="__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = a + b
    a.sort()

    for i in a:
        print(i, end = ' ')
def main():
    a, b = map(int, input().split())

    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    set_a = A - B
    set_b = B - A

    print(len(set_a) + len(set_b))


if __name__=="__main__":
    main()
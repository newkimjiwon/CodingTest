if __name__ == "__main__":
    # 민국이
    minguk = sum(list(map(int, input().split())))
    # 만세
    manseo = sum(list(map(int, input().split())))

    if minguk > manseo:
        print(minguk)
    elif minguk < manseo:
        print(manseo)
    else:
        print(minguk)
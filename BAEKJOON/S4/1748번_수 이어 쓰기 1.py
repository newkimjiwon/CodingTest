def main():
    n = int(input())  # 1부터 N까지의 숫자

    len_n = len(str(n))

    count = 0

    for i in range(len_n - 1):
        # 1 ~ 9     = 9
        # 10 ~ 99   = 90
        # 100 ~ 999 = 900
        # ...
        count += 9 * 10 ** i * (i + 1)

    print(count + (n - 10 ** (len_n - 1) + 1) * len_n)


if __name__=="__main__":
    main()
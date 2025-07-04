def main():
    n = int(input())  # 거스름돈

    c500 = n // 5  # 5원
    n %= 5  # 5원 후 거스름돈

    if n == 0:
        print(c500)
        return
    
    if n % 2 == 0:
        c100 = n // 2
        print(c500 + c100)
        return
    else:
        for i in range(1, c500 + 1):
            c500 -= i
            n += i * 5
            if n % 2 == 0:
                c100 = n // 2
                print(c500 + c100)
                return
            c500 += i
    
    print(-1)

main()
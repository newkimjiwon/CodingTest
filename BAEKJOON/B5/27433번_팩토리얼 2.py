if __name__=="__main__":
    N = int(input())

    if N == 0:
        print(1)
    else:
        count = 1

        for i in range(1, N + 1):
            count *= i
        print(count)
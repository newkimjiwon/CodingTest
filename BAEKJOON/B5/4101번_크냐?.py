if __name__ == "__main__":
    while True:
        # 첫 번째와 두 번째의 수
        a, b = map(int, input().split())

        if a == 0 and b == 0:
            break
        else:
            if a > b:
                print('Yes')
            else:
                print('No')
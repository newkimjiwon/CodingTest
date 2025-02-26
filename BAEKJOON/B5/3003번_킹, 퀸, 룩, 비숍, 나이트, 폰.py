if __name__=="__main__":
    p = list(map(int, input().split()))  # 피스

    chess = [1, 1, 2, 2, 2, 8]

    for i in range(len(chess)):
        chess[i] = chess[i] - p[i]

    for i in chess:
        print(i, end = ' ')
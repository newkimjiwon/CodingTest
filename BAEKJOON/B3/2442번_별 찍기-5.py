if __name__=="__main__":
    # 별의 개수
    n = int(input())

    # 탑의 높이
    for i in range(1, n + 1):
        null_1 = ''
        start_1 = ''
        start_2 = ''

        for j in range(n, i, -1):
            null_1 += ' '
        
        for j in range(0, i):
            start_1 += '*'
        
        for k in range(1, i):
            start_2 += '*'
        
        print(null_1 + start_1 + start_2)


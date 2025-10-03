if __name__=="__main__":
    arr = [list(map(int, input().split())) for _ in range(9)]  # 데이터

    max_value = -1

    y, x = 0, 0

    for ry in range(len(arr)):
        for rx in range(len(arr[ry])):
            if arr[ry][rx] > max_value:
                max_value = arr[ry][rx]
                y, x = ry + 1, rx + 1
    
    print(max_value)
    print(y, x)
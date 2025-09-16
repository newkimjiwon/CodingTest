if __name__=="__main__":
    arr = [int(input()) for _ in range(9)]

    # 정렬
    arr.sort()

    sum = sum(arr)

    for i in range(9):
        for ii in range(i + 1, 9):
            if sum - arr[i] - arr[ii] == 100:
                for iii in range(9):
                    if iii == i or iii == ii:
                       pass
                    else:
                       print(arr[iii]) 
                exit()
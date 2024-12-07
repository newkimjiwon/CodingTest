def hansu(i):
    han = list(str(i))

    if len(han) == 1:
        return True
    elif len(han) == 2:
        return True
    else:
        one = int(han[0]) - int(han[1])
        two = int(han[1]) - int(han[2])
        # 등차수열 일 경우 True
        if one == two:
            return True
        else:
            return False

def main():
    # 등차수열
    n = int(input())

    # 몇 개인지 카운트
    count = 0

    for i in range(1, n + 1):
        if hansu(i):
            count += 1
    
    print(count)

main()
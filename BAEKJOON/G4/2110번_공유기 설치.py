def can_place(routers, c, d):
    count = 1
    last = routers[0]

    for i in router[1:]:
        if i - last >= d:
            count += 1
            last = i

            if count >= c:
                return True
            
    return False


if __name__=="__main__":
    n, c = map(int, input().split())

    router = [int(input()) for _ in range(n)]  # 공유기

    router.sort()  # 오름차순으로 정렬

    left = 1
    right = router[-1] - router[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 후보 간격
        if can_place(router, c, mid):
            answer = mid           # 가능하면 간격을 키워본다
            left = mid + 1
        else:
            right = mid - 1        # 불가능하면 간격을 줄인다

    print(answer)
if __name__=="__main__":
    # N개의 달걀이 있고, 그의 잠재적인 고객은 총 M명
    n, m = map(int, input().split())

    # 각각의 i번째 고객은 각자 달걀 하나를 Pi 가격 이하로 살 수 있다고 밝혔다.
    # 경래는 영양란이라 속인 죄책감에 한 고객에게 두 개 이상의 달걀은 팔지 않기로 하였다.
    # 하지만 위의 규칙 하에 수익은 최대로 올리고 싶기에 얼마로 팔지 고민하고 있다.
    # 즉, A가격에 달걀을 판다고 하면 Pi가 A가격보다 크거나 같은 모든 고객은 달걀을 산다는 뜻이다. (물론 달걀 총 수량을 초과하여 팔 수 는 없다)
    price = [int(input()) for _ in range(m)]

    # 오름차순으로 정렬
    price.sort()
    # 총 가격
    total = 0
    # 현재 계란 가격
    current = 0

    for i in range(m):
        cnt = m - i

        if n <= cnt:
            total_sum = n * price[i]
        else:
            total_sum = cnt * price[i]

        if total_sum > total:
            total = total_sum
            current = price[i]

    print(f'{current} {total}')
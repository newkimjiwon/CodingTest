import sys


def solution():
    input = sys.stdin.readline
    # 개수
    n = int(input())

    # 거리
    dis = list(map(int, input().split()))
    # 가격
    price = list(map(int, input().split()))

    # 총 금액
    answer = 0
    # 처음 금액
    current_price = price[0]

    for i in range(n - 1):
        # 현재 주유소가 더 싸다면 가격 갱신
        if current_price > price[i]:
            current_price = price[i]
        answer += current_price * dis[i]
    
    print(answer)


solution()
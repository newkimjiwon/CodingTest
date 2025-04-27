def solution():
    # 총 가격
    total = int(input())

    for _ in range(9):
        price = int(input())
        total -= price
    
    print(total)


solution()
if __name__=="__main__":
    # 햄버거
    ham = [int(input()) for _ in range(3)]

    # 음료수
    drink = [int(input()) for _ in range(2)]

    print(min(ham) + min(drink) - 50)
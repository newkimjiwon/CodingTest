if __name__=="__main__":
    # n, m의 값을 대입
    n, m = map(int, input().split())

    # 두 유명도 차이를 출력한다.
    result = n - m

    # 절대값으로 출력해야하므로 음수일 경우 양수로 전환한다.
    if result < 0:
        result = -result
        print(result)
    else:
        print(result)
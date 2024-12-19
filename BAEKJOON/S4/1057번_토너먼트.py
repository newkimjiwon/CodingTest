def main():
    # 입력
    n, kim, lim = map(int, input().split())

    # 라운드 초기화
    round = 0

    # 두 번호가 같아질 때까지 반복
    while kim != lim:
        kim = (kim + 1) // 2
        lim = (lim + 1) // 2
        round += 1

    print(round)

main()
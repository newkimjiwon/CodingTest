def solution():
    n = int(input())

    paper = [[0] * 101 for _ in range(101)]  # 도화지의 크기는 100으로 고정되어 있음

    # 색종이를 붙일 위치를 선정
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(b, b + 10):
            for j in range(a, a + 10):
                paper[i][j] = 1

    # 총 넓이를 구한다.
    answer = 0

    # 색종이를 붙인 곳을 체크
    for i in range(101):
        for j in range(101):
            if paper[i][j] == 1:
                answer += 1

    print(answer)


if __name__=="__main__":
    solution()
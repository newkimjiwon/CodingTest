def main():
    #  n = 세로 길이, m = 가로 길이
    n, m = map(int, input().split())

    # 체스판
    chess = [list(input()) for _ in range(n)]

    # 답
    answer = []

    # 모든 체스판을 확인 하는 과정
    # 7로 자르면 모든 체스판을 확인 할 수 있다.
    for i in range(n - 7):
        for j in range(m - 7):
            white_count = 0
            black_count = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if (k + l) % 2 == 0:
                        if chess[k][l] != 'W':  # W가 아니면, 즉 B이면
                            white_count += 1  # W로 칠하는 갯수
                        else:  # W일 때
                            black_count += 1  # B로 칠하는 갯수
                    else:  # 홀수인 경우
                        if chess[k][l] != 'W':  # W가 아니면, 즉 B이면
                            black_count += 1  # B로 칠하는 갯수
                        else:
                            white_count += 1  # W로 칠하는 갯수
            answer.append(white_count)
            answer.append(black_count)
    # 정답 출력
    print(min(answer))

main()
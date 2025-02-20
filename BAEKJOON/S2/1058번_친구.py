
def solution(n, friend):
    inside = 0  # 인싸 친구의 수

    for me in range(n):
        # 친구 수를 체크하는 리스트
        check = [False] * n

        for i in range(n):
            # 내가 아니면서 친구인 사람을 발견 (i는 me의 친구)
            if me != i and friend[me][i] == 'Y':
                check[i] = True
                # 친구의 친구를 찾기
                for j in range(n):
                    if me != j and friend[i][j] == 'Y':
                        check[j] = True

        # 더 많은 사람이 생기면 갱신한다.
        inside = max(inside, check.count(True))

    return inside


def main():
    # 친구의 수
    n = int(input())

    # 친구
    friend = [list(input()) for _ in range(n)]

    print(solution(n, friend))


if __name__=="__main__":
    main()
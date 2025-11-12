def solution(bingo, moderator):
    bingo_Arr = []

    left = []
    right = []

    # 1. 빙고가 나올 수 있는 경우의 수
    for i in range(len(bingo)):
        bingo_Arr.append(bingo[i])

        left.append(bingo[i][i])
        right.append(bingo[i][len(bingo) - 1 - i])

        tem = []
        for j in range(len(bingo)):
            tem.append(bingo[j][i])
        
        bingo_Arr.append(tem)
    
    bingo_Arr.append(left)
    bingo_Arr.append(right)

    # 2. 숫자를 부르면 확인 시작
    called = set()  # 부른 숫자 저장
    count = 0

    # 사회자가 숫자를 하나씩 부름
    for i in range(5):
        for j in range(5):
            count += 1
            called.add(moderator[i][j])

            # 빙고 줄이 몇 개인지 계산
            bingo_count = 0
            for line in bingo_Arr:
                line_complete = True  # 이 줄이 완성됐는지 여부
                for num in line:
                    if num not in called:
                        line_complete = False
                        break  # 하나라도 안 불린 숫자가 있으면 종료
                if line_complete:
                    bingo_count += 1

            # 3줄 이상이면 즉시 종료
            if bingo_count >= 3:
                return count

    return count


if __name__=="__main__":
    
    bingo = [list(map(int, input().split())) for _ in range(5)]  # 빙고판 생성
    
    moderator = [list(map(int, input().split())) for _ in range(5)]  # 사회자가 부르는 내용
    
    """
    bingo = [[11, 12, 2, 24, 10],
            [16, 1, 13, 3, 25],
            [6, 20, 5, 21, 17],
            [19, 4, 8, 14, 9],
            [22, 15, 7, 23, 18]]

    moderator = [[5, 10, 7, 16, 2],
                [4, 22, 8, 17, 13],
                [3, 18, 1, 6, 25],
                [12, 19, 23, 14, 21],
                [11, 24, 9, 20, 15]]
    """

    print(solution(bingo, moderator))
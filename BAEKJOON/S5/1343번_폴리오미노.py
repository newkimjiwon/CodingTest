if __name__ == "__main__":
    board = input().strip()  # 입력받은 보드 문자열
    answer = ""              # 최종 결과 문자열 초기화
    i = 0                    # 문자열을 순회할 인덱스
    possible = True          # 변환 가능 여부를 저장하는 변수

    # 보드 문자열의 모든 문자를 순회
    while i < len(board):
        if board[i] == 'X':
            j = i
            # 연속된 'X' 구간의 길이를 구함
            while j < len(board) and board[j] == 'X':
                j += 1
            count = j - i  # 연속된 'X'의 개수

            # 'X'의 개수가 홀수이면 변환 불가능하므로 종료
            if count % 2 != 0:
                possible = False
                break

            # 가능한 만큼 "AAAA" 사용 후, 남은 2개는 "BB" 사용
            answer += "AAAA" * (count // 4) + "BB" * ((count % 4) // 2)
            i = j  # 연속 구간을 건너뜀
        else:
            # '.'인 경우 그대로 결과에 추가
            answer += '.'
            i += 1

    # 변환이 가능하면 결과 출력, 불가능하면 -1 출력
    print(answer if possible else -1)

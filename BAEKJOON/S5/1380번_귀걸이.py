if __name__=="__main__":
    count = 1  # 시나리오 번호

    while True:
        n = int(input())  # 여학생 수

        if n == 0:  # n == 0 인경우 종료한다.
            break

        student = {i: 0 for i in range(1, n + 1)}  # 학생

        for i in range(1, n + 1):  # 여학생 이름 입력
            name = input()
            student[i] = name  # 번호: 키, 이름 값

        wm = {i: 0 for i in range(1, n + 1)}  # 여학생 

        for _ in range(n * 2 - 1):  # 압수
            number, status = map(str, input().split())  # 번호와 상태
            if status == 'A' or status == 'B':  # 한 번이라도 나오면 체크
                wm[int(number)] += 1
        
        for i in range(1, n + 1):
            if wm[i] < 2:  # 2보다 작으면 돌려 받지 못한 것이다.
                print(f'{count} {student[i]}')
        
        count += 1
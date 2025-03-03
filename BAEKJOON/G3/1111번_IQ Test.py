if __name__ == "__main__":
    n = int(input())  # 정수의 개수
    test = list(map(int, input().split()))  # 리스트

    if n == 1:
        print("A")
    elif n == 2:
        if test[0] == test[1]:  
            print(test[0])  # 같은 숫자면 다음 수도 동일
        else:
            print("A")  # 경우의 수가 많아 결정 불가능
    else:
        # 첫 번째 두 항으로 a, b 계산
        if test[1] - test[0] == 0:  # 0으로 나누는 경우 방지
            a = 0
            b = test[1]  # 모든 수가 같은 경우
        else:
            if (test[2] - test[1]) % (test[1] - test[0]) != 0:  # a가 정수가 아닌 경우
                print("B")
                exit()  # 프로그램 종료
            
            a = (test[2] - test[1]) // (test[1] - test[0])  # 정수 나눗셈
            b = test[1] - test[0] * a

        # 등차수열이 성립하는지 확인
        valid = True
        for i in range(n - 1):
            if test[i + 1] != test[i] * a + b:
                valid = False
                break

        if valid:
            print(test[-1] * a + b)  # 다음 수 예측
        else:
            print("B")
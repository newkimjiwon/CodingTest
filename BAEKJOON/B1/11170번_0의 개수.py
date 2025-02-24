if __name__=="__main__":
    n = int(input())  # 숫자 범위

    result = []  # 결과 값

    for _ in range(n):
        n, m = map(int, input().split())  # 시작, 끝 범위

        current_result = 0  # 현재 결과 값

        for i in range(n, m + 1):
            current = list(str(i))
            for j in current:
                if j == '0':
                     current_result += 1
        
        result.append(current_result)

    for i in result:
        print(i)
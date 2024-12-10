def main():
    # X번째 분수를 찾기
    x = int(input())

    # 현재 몇 번째 숫자까지 도달했는지 확인하기 위한 변수
    arr = 0
    # 현재 분수의 대각선 번호 (1부터 시작)
    diagonal = 1

    # X가 포함된 대각선을 찾음
    while arr + diagonal < x:
        arr += diagonal
        diagonal += 1

    # X가 대각선의 몇 번째 위치인지 계산
    offset = x - arr

    # 대각선 번호가 홀수인 경우: 분자는 대각선 번호에서 시작하여 감소, 분모는 1에서 시작하여 증가
    if diagonal % 2 == 1:
        numerator = diagonal - (offset - 1)
        denominator = offset
    # 대각선 번호가 짝수인 경우: 분모는 대각선 번호에서 시작하여 감소, 분자는 1에서 시작하여 증가
    else:
        numerator = offset
        denominator = diagonal - (offset - 1)

    # 결과 출력
    print(f"{numerator}/{denominator}")

main()
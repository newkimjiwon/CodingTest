N = input()

digits = list(N)
digits.sort(reverse=True)  # 가장 큰 수를 만들기 위해 내림차순 정렬

if '0' not in digits:  # 0이 없으면 10의 배수가 아님 → 30의 배수도 아님
    print(-1)
elif sum(map(int, digits)) % 3 != 0:  # 자릿수 합이 3의 배수가 아니면 3의 배수가 아님
    print(-1)
else:
    print(''.join(digits))  # 조건 만족 → 가장 큰 수 출력
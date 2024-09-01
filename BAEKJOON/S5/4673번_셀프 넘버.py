def d(n):
    # n과 n의 각 자릿수를 더하는 함수
    return n + sum(int(digit) for digit in str(n))

# 1부터 10000까지의 숫자에 대해 생성된 숫자를 추적할 집합
generated_numbers = set()

# 1부터 10000까지의 모든 숫자에 대해 d(n)을 계산
for i in range(1, 10001):
    generated_number = d(i)
    if generated_number <= 10000:  # 10000 이하의 숫자만 추적
        generated_numbers.add(generated_number)

# 셀프 넘버는 1부터 10000까지의 숫자 중 generated_numbers에 없는 숫자
for i in range(1, 10001):
    if i not in generated_numbers:
        print(i)
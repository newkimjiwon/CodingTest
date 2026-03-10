import math
import sys

# 입력을 "n:m" 형태로 받아서 ":"를 기준으로 분리합니다.
input_data = sys.stdin.readline().strip().split(':')

# 분리된 문자열을 정수형으로 변환합니다.
n = int(input_data[0])
m = int(input_data[1])

# n과 m의 최대공약수를 구합니다.
common_divisor = math.gcd(n, m)

# 각각의 수를 최대공약수로 나누어 약분된 결과를 출력합니다.
# 정수 나눗셈(//)을 사용하여 결과가 실수형이 되지 않도록 합니다.
print(f"{n // common_divisor}:{m // common_divisor}")
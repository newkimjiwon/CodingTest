import sys

# sys.stdin.readline()은 한 줄을 읽어오므로 split()을 사용해 공백으로 구분
A, B = map(int, sys.stdin.readline().split())

# 64비트 정수형은 파이썬에서 자동으로 처리되므로 별도 설정 불필요
result = (A + B) * (A - B)

print(result)
# n개의 정수
n = int(input())

# 정수의 모임
integers = list(map(int, input().split()))

print(min(integers), max(integers))
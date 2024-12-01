# 정수의 모임
integers = [int(input()) for _ in range(9)]

# 최댓값 출력
max_number = max(integers)

print(max_number)
print(integers.index(max_number) + 1)
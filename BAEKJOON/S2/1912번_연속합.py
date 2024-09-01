N = int(input())
numbers = list(map(int, input().split()))

# 첫 번째 원소로 초기화
current_sum = numbers[0]
max_sum = numbers[0]

# 두 번째 원소부터 순회
for i in range(1, N):
    current_sum = max(numbers[i], current_sum + numbers[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
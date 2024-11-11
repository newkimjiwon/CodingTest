n = int(input())

numbers = list(map(str, input()))

answer = 0

for n in numbers:
    answer += int(n)

print(answer)
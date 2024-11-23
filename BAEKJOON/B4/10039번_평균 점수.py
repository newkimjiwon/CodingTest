grade = []

for _ in range(5):
    i = int(input())
    if i < 40:
        grade.append(40)
    else:
        grade.append(i)

print(sum(grade) // 5)
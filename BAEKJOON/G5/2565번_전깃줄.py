n = int(input())

cross_line = [1] * n

electric_wire = []

idx = 0

for _ in range(n):
    AB = list(map(int, input().split()))
    electric_wire.append(AB)

electric_wire.sort()

for i in range(1, n):
    for j in range(0, i):
        if electric_wire[j][1] < electric_wire[i][1]:
            cross_line[i] = max(cross_line[i], cross_line[j] + 1)

print(n - max(cross_line))
x = int(input())

n = int(input())

receipt = []

for _ in range(n):
    a, b = map(int, input().split())
    receipt.append(a * b)

if x == sum(receipt):
    print("Yes")
else:
    print("No")
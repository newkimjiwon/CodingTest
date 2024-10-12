a = int(input())
b = int(input())

c = b

while c > 0:
    current = c % 10
    print(a * current)
    c //= 10

print(a * b)
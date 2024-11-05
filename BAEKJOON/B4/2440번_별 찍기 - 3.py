n = int(input())

for i in range(n, 0, -1):
    star = ''
    for _ in range(i):
        star += '*'
    print(star)
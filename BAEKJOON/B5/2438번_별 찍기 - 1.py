n = int(input())

for i in range(1, n + 1):
    star = ''
    for _ in range(i):
        star += '*'
    print(star)
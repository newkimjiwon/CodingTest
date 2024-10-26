n, k = map(int, input().split())

count = []

for i in range(1, (n // 2) + 1):
    if n % i == 0:
        count.append(i)

count.append(n)

if len(count) >= k:
    print(count[k - 1])
else:
    print(0)
N = int(input())

for i in range(N, 0, -1):
    result = ""
    for _ in range(i - 1):
        result += " "
    for _ in range(N - i + 1):
        result += "*"
    print(result)
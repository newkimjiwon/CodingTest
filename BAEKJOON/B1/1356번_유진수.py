N = input()

def solution(N):
    line = list(N)
    length = len(line)

    for i in range(1, length):
        left = 1
        right = 1

        for j in range(i):
            left *= int(line[j])

        for j in range(i, length):
            right *= int(line[j])

        if left == right:
            return "YES"
    return "NO"

print(solution(N))
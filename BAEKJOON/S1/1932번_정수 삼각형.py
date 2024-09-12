def solution(tr):
    for i in range(1, len(tr)):
        for j in range(len(tr[i])):
            if j == 0:
                tr[i][j] += tr[i - 1][0]
            elif j == len(tr[i]) - 1:
                tr[i][j] += tr[i - 1][-1]
            else:
                tr[i][j] += max(tr[i - 1][j - 1], tr[i - 1][j])
    return max(tr[-1])

n = int(input())

triangle = []

for _ in range(n):
    line = list(map(int, input().split()))
    triangle.append(line)

print(solution(triangle))
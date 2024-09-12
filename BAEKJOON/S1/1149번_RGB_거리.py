def solution(h: list):
    for i in range(len(h) - 2, -1, -1):
        for j in range(3):
            if j == 0:
                h[i][j] = min(h[i][j] + h[i + 1][1], h[i][j] + h[i + 1][2])
            elif j == 1:
                h[i][j] = min(h[i][j] + h[i + 1][0], h[i][j] + h[i + 1][2])
            elif j == 2:
                h[i][j] = min(h[i][j] + h[i + 1][0], h[i][j] + h[i + 1][1])

    return min(h[0])

n = int(input())

home = []

# 집을 볼 배열
for _ in range(n):
    line = list(map(int, input().split()))
    home.append(line)

print(solution(home))
import sys

game = sys.stdin.read()
white = 0
answer = 0

for i in game:
    if white % 2 == 0 and i == "F":
        answer += 1
    white += 1

print(answer)
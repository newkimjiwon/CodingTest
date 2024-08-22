import re

def solution(w):
    c = re.compile(r'(100+1+|01)+')
    return bool(c.fullmatch(w.strip()))

N = int(input())
result = []

for i in range(N):
    word = input()
    result.append(word)

for i in result:
    if solution(i):
        print("YES")
    else:
        print("NO")
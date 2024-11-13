# 일의 개수
n = int(input())

# 일 명단
works = [list(map(int, input().split())) for _ in range(n)]

works.sort(key = lambda x: x[1], reverse = True)

start = works[0][1] - works[0][0]

for i in range(1, len(works)):
    next_start, next_end = works[i]
    if next_end < start:
        start = next_end - next_start
    else:
        start -= next_start

if start > -1:
    print(start)
else:
    print(-1)
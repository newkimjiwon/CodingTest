N = int(input())

# 회원들을 담을 배열
member = []

for i in range(N):
    age, name = map(str, input().split())
    member.append([int(age), name, i])

member.sort(key = lambda x : (x[0], x[2]))

for a, b, c in member:
    print(a, end = " ")
    print(b)
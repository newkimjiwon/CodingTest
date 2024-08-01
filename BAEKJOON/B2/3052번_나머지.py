# 중복을 방지하기 위해서 set를 사용한다.
s = set()

for _ in range(10):
    N = int(input())
    s.add(N % 42)

print(len(s))